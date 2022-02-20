from inspect import getfullargspec
from types import FunctionType
import logging

def cast_hints(*args, **kwargs):

	cast_none = True
	strict = False

	if 'cast_none' in kwargs:
		cast_none = kwargs['cast_none']
	if 'strict' in kwargs:
		strict = kwargs['strict']


	def outer(func):

		spec = getfullargspec(func)

		def wrapper(*args, **kwargs):
			new_args = []
			new_kwargs = {}
			for i in range(len(args)):
				arg_name = spec.args[i]
				passed_value = args[i]

				if (cast_none or passed_value is not None) and \
				arg_name in spec.annotations and not \
				isinstance(passed_value, spec.annotations[arg_name]):
					try:
						passed_value = spec.annotations[arg_name](passed_value)
					except Exception as e:
						if strict:
							raise TypeError(f'Could not convert {arg_name} to {spec.annotations[arg_name]}. {e}')
						logging.warning(f'Could not convert {arg_name} to {spec.annotations[arg_name]}. {e}')

				new_args.append(passed_value)

			for arg_name in kwargs:
				passed_value = kwargs[arg_name] if arg_name in kwargs else None

				if (cast_none or passed_value is not None) and \
				arg_name in spec.annotations and not \
				isinstance(passed_value, spec.annotations[arg_name]):
					try:
						passed_value = spec.annotations[arg_name](passed_value)
					except Exception as e:
						if strict:
							raise TypeError(f'Could not convert {arg_name} to {spec.annotations[arg_name]}. {e}')
						logging.warning(f'Could not convert {arg_name} to {spec.annotations[arg_name]}. {e}')

				new_kwargs[arg_name] = passed_value

			return func(*new_args, **new_kwargs)

		return wrapper

	if isinstance(args[0] if len(args) > 0 else None, FunctionType):
		return outer(args[0])

	return outer

def strict_hints(func):
	spec = getfullargspec(func)

	def wrapper(*args, **kwargs):
		for i in range(len(args)):
			arg_name = spec.args[i]
			passed_value = args[i]

			if arg_name in spec.annotations and not \
			isinstance(passed_value, spec.annotations[arg_name]):
				raise TypeError(f'{arg_name} is not of type {spec.annotations[arg_name]}')

		for arg_name in kwargs:
			passed_value = kwargs[arg_name] if arg_name in kwargs else None

			if arg_name in spec.annotations and not \
			isinstance(passed_value, spec.annotations[arg_name]):
				raise TypeError(f'{arg_name} is not of type {spec.annotations[arg_name]}')

		return func(*args, **kwargs)

	return wrapper
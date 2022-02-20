# hintcast
Decorators that allow for automatic type-casting of arguments for a function or strict enforcement of type hints.

## Usage Summary
Import whatever decorators you want with an import statement like `from hintcast import cast_hints, strict_hints`.

### Casting Types
- To add automated type-casting to your function/method, use the `@cast_hints` decorator for your method. If a type cannot be cast, a warning will be logged.
- To attempt to cast but raise a TypeError exception if unable to, pass the keyword argument "strict". E.g. `@cast_hints(strict=True)`.
- To pass `None` values without casting, pass the keyword argument "cast_none". E.g. `@cast_hints(cast_none=False)`.

### Enforcing strict types
- You can also use the `@strict_hints` decorator. This will NOT attempt to cast the types, but will raise a ValueError if a type not matching your hint is passed.



## Usage Examples
### Casting Types

```
from hintcast import cast_hints

@cast_hints
def add_two(num: int, text: str):
    print(repr(num+2))
    print(repr(text+"2"))
```
Output
```
>>> add_two("3", 3)
5
'32'
>>> add_two("3", None)
5
'None2'
```

### Casting types without casting NoneType
```
from hintcast import cast_hints

@cast_hints(cast_none=False)
def add_two(num: int, text: str):
  print(repr(num+2))
  print(repr(text+"2"))
```
Output
```
>>> add_two("3", 3)
5
'32'
>>> add_two("3", None)
5
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```
### Casting types and raising TypeError when type could not be cast
```
from hintcast import cast_hints

@cast_hints(strict=True)
def add_two(num: int, text: str):
  print(repr(num+2))
  print(repr(tex+"2"))
```
Output
```
>>> add_two("3", 3)
5
'32'
>>> add_two("test", 3)
TypeError: Could not convert num to <class 'int'>. invalid literal for int() with base 10: 'test'
```
### Enforcing strict typing without casting
```
from hintcast import strict_hints

@strict_hints
def add_two(num: int, text: str):
  print(repr(num+2))
  print(repr(text+"2"))
```
Output
```
>>> add_two("3", 3)
TypeError: num is not of type <class 'int'>
>>> add_two(3, 3)
TypeError: text is not of type <class 'str'>
```

## Future Development Plans
- Test support for all primitive types
- Add support for checking function return type hints
- Add support for built-in non-primitive data structures such as arrays, lists, etc.
- Add support for hinting of types within lists, dictionaries, etc.
- Add ability to enforce typing project-wide

When all of the functionality above has been implemented and tested, the version number will be incremented to 1.0.0 and this project will leave beta status.

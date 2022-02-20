from distutils.core import setup

setup(
    name = 'hintcast',
    packages = ['hintcast'],
    version = '0.1.0',
    license = 'MIT',
    description = 'Decorators that allow for automatic type-casting of arguments for a function or strict enforcement of type hints.',
    author = 'David Carli-Arnold',
    author_email = 'davocarli@gmail.com',
    url = 'https://github.com/davocarli/hintcast',
    keywords = ['casting', 'typecast', 'type-cast', 'type-hints', 'hints', 'types', 'python', 'decorator'],
    install_requires = [],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
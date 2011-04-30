from setuptools import setup

setup(
    name = 'coded_exceptions',
    version = '0.1.0',
    py_modules = ['coded_exceptions'],

    # Metadata
    author = "Nikolay Zakharov",
    author_email = "nikolay@desh.su",
    description = "New base class for application exceptions: CodedException",
    long_description = (
        "Module provides new class to use as base "
        "class for exceptions. Any subclass of CodedException "
        "will have an unique class attribute 'code'. Such a code "
        "can be used to identify errors (for example, in api responses)"),
    keywords = "exception exceptions api",
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
    ],
)

'''
Module provides new base class for exceptions: CodedException.

Each subclass of CodedException have unique attribute 'code'.
If code is unspecified, it will be generated from class name
(see CodedExceptionMeta.make_code_from_name for details).

Unique constraint is controlled at the class creation time. If
exception class with same code was already defined somewhere and
thus registered in CodedExceptionMeta._registered_exceptions,
CodedExceptionExists will be raised.
'''
import re

class CodedExceptionExists(Exception):
    pass


class CodedExceptionMeta(type):

    _registered_exceptions = {}

    def __new__(cls, name, bases, attrs):
        new_class = super(CodedExceptionMeta, cls).__new__(
                                                    cls, name, bases, attrs)

        if bases[0] != Exception or len(bases) != 1:
            if 'code' in attrs:
                code = attrs['code']
                if code is not None:
                    cls.set_code_or_die(code, new_class)
            else: # code is ommited, trying to set it automatically
                code = cls.make_code_from_name(name)
                new_class.code = code
                cls.set_code_or_die(code, new_class)

        return new_class

    @classmethod
    def set_code_or_die(cls, code, new_class):
        old_class = cls._registered_exceptions.setdefault(code,
                                                            new_class)
        if old_class is not new_class:
            raise CodedExceptionExists(code, old_class, new_class)

    @staticmethod
    def make_code_from_name(name):
        '''
        Default code inducer.

        Example:
        >>> CodedExceptionMeta.make_code_from_name('SomeCustomValidationError')
        'some_custom_validation_error'
        '''
        canonical_name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name).lower()
        #if canonical_name.endswith('_error'):
        #    canonical_name = canonical_name[:-6]
        return canonical_name


class CodedException(Exception):
    __metaclass__ = CodedExceptionMeta
    code = 0
    # serializable error context
    context = None
    # human-readable message
    text_message = None

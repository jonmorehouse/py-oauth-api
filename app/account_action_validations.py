from method_missing import MethodMissingMetaClass 
from exceptions import ParamMissing

class AccountActionValidations:
    """ This class is an attempt at clearing up parameter dependencies before calling any code """

    __metaclass__ = MethodMissingMetaClass
    required_params = {
        "signup" : ["username", "phone_number", "password"]
    }

    @classmethod
    def method_missing(kls, method_name, params, **kw):
        
        """ Handle validations that are not specifically defined. Assumes that params is an immutable dict """
        required_params = kls.required_params.get(method_name)
        if not required_params: return True

        for param in required_params:
            if not params.get(param):
                raise ParamMissing(param)
                return False

        return True




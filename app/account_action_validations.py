from method_missing import MethodMissing

class AccountActionValidations:

    __metaclass__ = MethodMissing
    """ This class is an attempt at clearing up parameter dependencies before calling any code """
    required_params = {
    
        "signup" : ["username", "phone_number", "password"]
    }

    @staticmethod
    def method_missing(method_name):

        print "METHOD MISSING"


    @classmethod
    def has_required_params(cls, method_name, params):

        pass
        






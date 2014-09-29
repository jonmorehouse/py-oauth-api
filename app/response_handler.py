from account_actions import AccountActions
from account_action_validations import AccountActionValidations

def action_handler(method_name, form, **kw):

    """ Handle an action against the api, from start to end """
    validation_method = getattr(AccountActionValidations, method_name)
    if not validation_method(method_name, form, **kw): return

    action_method = getattr(AccountActions, method_name)
    return action_method(form = form, **kw)

     



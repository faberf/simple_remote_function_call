import simple_remote_function_call_server as srfcs

class GLOBAL:
    func_dict = {}


def register(func):
    GLOBAL.func_dict[func.__name__] = func
    return func


import inspect
import secure_remote_funciton_call_server as srfcs

class GLOBAL:
    func_dict = {}
    database = srfcs.Database()


def register_func(func):
    GLOBAL.func_dict[func.__name__] = func
    return func


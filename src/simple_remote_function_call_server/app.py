import flask
import pickle
import simple_remote_function_call_server as srfcs

CURRENT_VERSION = "0.1"

app = flask.Flask(__name__)

def pickled(func):
    return lambda *args, **kwargs: pickle.dumps(func(*args, **kwargs))

@app.route("/call", methods=['PUT'])
@pickled
def call():
    input = pickle.loads(flask.request.data)
    if input[0] != CURRENT_VERSION:
        return ("ERROR", Exception(f"Current Version {input[0]} does not match {CURRENT_VERSION}."))
    _, func_name, args, kwargs = input
    try:
        result = ("SUCCESS", srfcs.GLOBAL.func_dict[func_name](*args, **kwargs))
    except Exception as ex:
        result = ("ERROR", ex)
    return result


@srfcs.register
def hello_world(name="User"):
    return f"Hello {name}! You successfully executed a remote function call to hello_world!"
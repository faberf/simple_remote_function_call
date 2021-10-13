import flask
import hashlib
import pickle
import secure_remote_funciton_call_server as srfcs

CURRENT_VERSION = 1.0

app = flask.Flask(__name__)

@app.route("/call")
def call():
    input = pickle.loads(flask.request.data)
    if input[0] != CURRENT_VERSION:
        return pickle.dumps("ERROR: version_does_not_match")
    _, auth_info, func_name, args, kwargs = input
    user_id, rand_string, code = auth_info
    if authentify(auth_info):
        result = srfcs.GLOBAL.func_dict[func_name](*args, **kwargs)
    result = pickle.dumps(result)
    return result

def authentify(user_id, rand_string, code):
    user_key = srfcs.GLOBAL.database.get_user_key(user_id)
    should = hashlib.sha224(bytes(user_key) + bytes(rand_string)).hexdigest()
    return code == should
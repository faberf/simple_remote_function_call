import pickle
import http.client
import string
import random
import hashlib

CURRENT_VERSION = "0.1"

LEN = 10

def rand_string():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(LEN))

class Client:

    def __init__(self, user_id, key, server_url):
        self.user_id = user_id
        self.key = key
        self.server_url = server_url

    
    def call(self, func_name, *args, **kwargs):
        data = pickle.dumps((CURRENT_VERSION, self.make_auth(), func_name, args, kwargs))
        conn = http.client.HTTPConnection(self.server_url)
        conn.request("POST","/call",data)
        return pickle.loads(conn.getresponse())

    def make_ath(self):
        x = rand_string()
        return (self.user_id, x, hashlib.sha224(bytes(self.key) + bytes(x)).hexdigest())


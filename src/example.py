import simple_remote_function_call_client as srfcc


c = srfcc.Client("localhost", 5000)

print(c.hello_world("fynn"))

x = 1
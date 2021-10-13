import simple_remote_function_call as srfc


c = srfc.Client("localhost", 8080)

print(c.hello_world("Bob"))

print(c.custom())
# srfc.start_server()
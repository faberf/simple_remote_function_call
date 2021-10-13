from setuptools import setup
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
  
  
# specify requirements of your package here
REQUIREMENTS = ['flask']
  
# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.9',
    ]
  
# calling the setup function 
setup(name='mygmap',
      version='0.1',
      description='A simple remote function call server and client.',
      long_description=long_description,
      url='https://github.com/faberf/simple_remote_function_call/',
      author='Fynn Firouz Faber',
      author_email='faberf@ethz.ch',
      license='MIT',
      packages=['simple_remote_function_call_client', "simple_remote_function_call_server"],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='remote server client function'
      )
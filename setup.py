from distutils.core import setup

def requirements():
    with open('requirements.txt', 'r') as f:
        return f.readlines()

setup(
    name='horde-client',
    version='1.0',
    description='Python Interface for AIHorde',
    author='Rahul D Shettu',
    author_email='35rahuldshetty@gmail.com',
    url='https://github.com/rahuldshetty/horde-client.git',
    install_requires=requirements(),
    packages=['horde_client', 'examples'],
)
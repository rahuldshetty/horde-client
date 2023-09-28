from distutils.core import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()


setup(
    name='horde-client',
    version='1.0.3',
    description='Python Interface for AIHorde',
    author='Rahul D Shettu',
    author_email='35rahuldshetty@gmail.com',
    url='https://github.com/rahuldshetty/horde-client.git',
    install_requires=[
        'requests==2.27.1',
        'pydantic==2.3.0',
        'asyncio-requests==2.7.3',
        'langchain==0.0.291'
    ],
    packages=['horde_client'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
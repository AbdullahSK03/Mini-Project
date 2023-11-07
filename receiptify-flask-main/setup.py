from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
]

setup(
    name='Music.AI',
    version='1.0',
    description='An application that gets your top spotify tracks and turns them into a receipt',
    author='Abdullah Shaikh',
    author_email='abdullah.sajid1974@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
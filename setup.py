from setuptools import find_packages, setup

setup(
   name='getwit',
   packages=find_packages(),
   version='0.1',
   description='Library yang terhubung dengan Twitter API v2',
   author='Ahmad Afiq Fitrah, Niken Dwi Wahyu Cahyani, Erwid Mustofa Jadied',
   install_requires=['requests_oauthlib', 'requests'],
)

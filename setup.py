from setuptools import find_packages, setup

setup(
   name='getwit',
   packages=find_packages(),
   version='0.1',
   description='Getwit as an API-based Acquisition Tool for Twitter',
   author='Ahmad Afiq Fitrah, Niken Dwi Wahyu Cahyani, Erwid Mustofa Jadied',
   install_requires=['requests_oauthlib', 'requests'],
)

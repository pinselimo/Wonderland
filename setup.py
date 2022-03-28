from setuptools import setup

with open("README.md",'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements_lines = f.readlines()
install_requires = [r.strip() for r in requirements_lines]

setup(
   name='wonderland',
   version='0.01dev',
   description='Sanderson\'s (1992) Wonderland model implemented in Python',
   license="GNU AGPLv3",
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Simon Plakolb',
   author_email='simon.plakolb@uni-graz.at',
   url="https://www.behaviour.space/teaching_materials.html",
   packages=['wonderland'],
   install_requires=install_requires, # packages required
)

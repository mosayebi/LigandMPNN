from setuptools import setup, find_packages

__pkg_name__ = 'ligandmpnn'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name=__pkg_name__,
      version='0.0.1',
      packages=find_packages(),
      install_requires=requirements,
      zip_safe = False,
      entry_points = {
        'console_scripts': [
            '{0} = {0}:main'.format(__pkg_name__)
        ]
      }
    )

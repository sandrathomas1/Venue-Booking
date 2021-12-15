from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in venue/__init__.py
from venue import __version__ as version

setup(
	name="venue",
	version=version,
	description="Venue Booking",
	author="sandra thomas",
	author_email="sandrathomass404@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

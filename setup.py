from setuptools import setup

setup(
	name="week_schedule",
	version="1.0",
	author="Jacob Hilbert",
	author_email="jacob.hilbert.tree@gmail.com",
	packages=["week_schedule"],
	install_requires=[
		"numpy",
		"matplotlib"
	],
	license="LICENSE",
	description="Create schedule images of your weekly classes",
	zip_safe=False
)
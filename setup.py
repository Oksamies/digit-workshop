from setuptools import find_packages, setup

setup(
    name='digit_project',
    version='0.0.0',
    license='Proprietary',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[l for l in open("requirements.txt", "rt").readlines() if l and not l.startswith("#")],
    zip_safe=False,
)
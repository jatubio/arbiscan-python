from setuptools import setup

setup(
    name="arbiscan-python",
    version="0.1.0",
    description="A python API for arbiscan.com.",
    url="https://github.com/jatubio/arbiscan-python",
    author="Juan Antonio Tubio",
    author_email="jatubio@gmail.com",
    license="MIT",
    packages=[
        "arbiscan",
        "arbiscan.configs",
        "arbiscan.core",
        "arbiscan.enums",
        "arbiscan.modules",
        "arbiscan.utils",
    ],
    python_requires='>=3.8',
    install_requires=["aiohttp", "requests"],
    include_package_data=True,
    zip_safe=False,
)

from setuptools import setup, find_packages

setup(
    name="alist_v3",
    version="0.1.0",
    description="Write for alist V3",
    author="Iamk77",
    author_email="245958742@qq.com",
    # url="https://github.com/myusername/my_package",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    #classifiers=[
    #    "Programming Language :: Python :: 3",
    #    "License :: OSI Approved :: MIT License",
    #    "Operating System :: OS Independent",
    #],
)
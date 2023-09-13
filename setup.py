from setuptools import setup, find_packages

setup(
    name="alist_v3",
    version="0.1.0",
    description="Write for alist V3",
    author="Iamk77",
    author_email="chenyinfeng50@qq.com",
    url="https://github.com/IamK77/alist_v3",
    packages=find_packages(),
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License 2.0",
        "Operating System :: OS Independent",
    ],
)
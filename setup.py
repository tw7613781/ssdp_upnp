import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssdp_upnp",
    version="0.0.1",
    author="tw7613781",
    author_email="tw7613781@gmail.com",
    description="ssdp server and client of upnp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tw7613781/ssdp_upnp",
    packages=setuptools.find_packages(),
    install_requires=[
        'colorlog>=3.1.4'
    ]
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
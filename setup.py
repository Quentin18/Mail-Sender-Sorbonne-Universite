import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mailSenderSU",
    version="0.0.1",
    author="Quentin Deschamps",
    author_email="quentindeschamps18@gmail.com",
    description="Mail sender for Sorbonne Universite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite",
    packages=setuptools.find_packages(),
    install_requires=['sphinx', 'os', 'tkinter', 'click', 'smtplib', 'email'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points="""
    [console_scripts]
    mailSenderSU=mailSenderSU.mailSenderSU:main
    """,
)

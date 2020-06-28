import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='mailSenderSU',
    version='0.1.0',
    description='Mail sender for Sorbonne-University',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quentin Deschamps',
    author_email='quentindeschamps18@gmail.com',
    url='https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite',
    packages=['mailSenderSU', 'mailSenderSU.src'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Communications :: Email'
    ],
    license='MIT',
    keywords='mail sender python sorbonne-university',
    project_urls={
        'Documentation': '',
        'Travis':
        'https://travis-ci.org/Quentin18/Mail-Sender-Sorbonne-Universite/',
        'Source Code':
        'https://github.com/Quentin18/Mail-Sender-Sorbonne-Universite/',
    },
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        mailSenderSU=mailSenderSU.__main__:main
    ''',
    python_requires='>=3.6',
)

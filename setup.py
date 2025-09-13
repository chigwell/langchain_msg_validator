from setuptools import setup, find_packages

setup(
    name='langchain_msg_validator',
    version='2024.5.1',
    author='Eugene Evstafev',
    author_email='hi@eugene.plus',
    description='A simple validator for Langchain messages.',
    long_description='A simple validator for Langchain messages.',
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/langchain_msg_validator',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
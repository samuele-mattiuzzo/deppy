from setuptools import setup, find_packages

setup(
    name="deppy",
    version="0.0.1",
    author="Samuele Mattiuzzo",
    author_email="samumatt@gmail.com",
    description="""
    A comprehensive tool for analyzing and managing Python dependencies,
    ensuring security, compatibility, and license compliance.
    """,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/samuele-mattiuzzo/deppy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Build Tools",
        "Intended Audience :: Developers",
        "Development Status ::  1 - Planning",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add the required dependencies here
        'click',
        'requests',
        'packaging',
        'pydantic'
    ],
    entry_points={
        "console_scripts": [
            "deppy=deppy.cli:main",
        ],
    },
    include_package_data=True,
)

from setuptools import setup, find_packages

__version__ = "0.1.42"

setup(
    name="Maisie",
    version=__version__,
    description="User-oriented system for painless managing, storing, sharing, organizing and deploying Machine Learning models.",
    long_description=open("README.rst").read(),
    author="Zofia Kochutek, Łukasz Kleczaj, Marek Kochanowski",
    author_email="support@maisie.dev",
    url="https://github.com/nokia-wroclaw/innovativeproject-ml-models-management",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click>=7.0",
        "gitpython>=2.1.1",
        "requests>=2.22.0",
        "coloredlogs>=10.0",
        "pyyaml>=5.1.1",
        "terminaltables>=3.1.0",
        "ago>=0.0.93",
        "python-dateutil>=2.8.0",
    ],
    entry_points={
        "console_scripts": [
            "mai = maisie.interface:cli",
            "maisie = maisie.interface:cli",
        ]
    },
    package_data={"": ["logging.yaml"]},
    license="MIT",
    classifiers=(
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Communications :: File Sharing",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: System :: Archiving :: Backup",
        "Typing :: Typed",
    ),
)

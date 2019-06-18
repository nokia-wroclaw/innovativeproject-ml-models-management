from setuptools import setup, find_packages

__version__ = "0.1.1"

setup(
    name="Maisie",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "gitpython",
        "requests",
        "coloredlogs",
        "pyyaml",
        "terminaltables",
        "ago",
        "python-dateutil",
    ],
    entry_points={
        "console_scripts": [
            "mai = maisie.interface:cli",
            "maisie = maisie.interface:cli",
        ]
    },
    package_data={"": ["logging.yaml"]},
)

from setuptools import setup, find_packages

setup(
    name="Maisie",
    version="0.1.1",
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

Maisie - ML Models Management System
####################################

.. contents:: \

.. section-numbering::


Features
========

Could archiving, storing, managing and organizing machine learning models be done efficiently and with great focus on user experience? Sure, Maisie does just that. 

Maisie is a friendly, easy to use assistant that consists of:

- Web Application written in React
- Backend API written in Python, Flask
- Client Application/Package written in Python and hosted on PyPI

It integrates seamlessly with your favorite tools and provides you with all the important data, such as:

- Git revisions for all trained models, as well as information about source branches
- Searchable, filterable hyperparameters, parameters and metrics
- A single identifying dataset name, as well as an optional description
- Permanent URLs for easy sharing and downloading of stored models

Installing
==========

You can get the most current package from `PyPI <https://pypi.org/project/Maisie/>`_

.. code-block:: bash

    $ pip install Maisie

Using it in your training environment is fairly straightforward:

.. code-block:: python

    import maisie
    from sklearn.externals import joblib

    # Define your model here

    model.fit(X, y)
    model_filename = "example_model.pkl"
    joblib.dump(model, model_filename)

    # Define your metrics, fetch parameters and hyperparameters

    models = maisie.Models()
    models.upload(
        name="My first uploaded model",
        filename=model_filename,
        dataset_name="Singly Identifying Dataset Name",
        metrics={"accuracy": accuracy},
        hyperparameters=hyperparameters,
        parameters=parameters,
    )

Deploying
=========

Using docker-compose
--------------------

This repository provides a pre-configured ``docker-compose.yml`` file that contains sensible default options. 

Before starting the containers, you should create a local ``.env`` file using the included ``.env.sample``.

To start up all services, run:

.. code-block:: bash

    $ docker-compose up

To stop your services, you can press Ctrl+C/Ctrl+D. If you started the services in the background using  ``docker-compose up -d``, the correct way to do this would be:

.. code-block:: bash

    $ docker-compose stop

You can learn more about Docker Compose by `clicking here <https://docs.docker.com/compose/>`_.

Fetching individual images
--------------------------

Both frontend and backend images are automatically published to `Docker Hub <https://hub.docker.com>`_ as soon as new stable release is made available.

Links

- `Frontend image on Docker Hub <https://hub.docker.com/r/kochanowski/maisie>`_
- `Backend image on Docker Hub <https://hub.docker.com/r/kochanowski/maisie>`_
- ...other services

For reference, you can look at the `sample Ansible playbook <#>`_ that deploys all containers to a specified host using the locally configured ``.env`` file.

Contributing
============

Getting started
---------------

1. Clone the repository from the ``develop`` branch

.. code-block:: bash

    $ git clone -b develop git@github.com:nokia-wroclaw/innovativeproject-ml-models-management.git

2. Install `pre-commit <https://pre-commit.com/#install>`_

3. Inside the project's root directory install all required githooks:

.. code-block:: bash

    $ pre-commit install

4. To start all required services for local development, run:

.. code-block:: bash

    $ docker-compose up

5. You're all set up!

Fixing existing issues
----------------------

1. Pick one of the `open issues <https://github.com/nokia-wroclaw/innovativeproject-ml-models-management/issues>`_ or `create a new one <https://github.com/nokia-wroclaw/innovativeproject-ml-models-management/issues/new>`_

2. Create a new branch named ``issue-[number]-[short description]`` derived from the ``develop`` branch, for example

.. code-block:: bash

    $ git checkout -b issue-42-project-removal-permissions develop

3. Make sure your implementation fixes the actual problem and is well tested. 

Implementing new features
-------------------------

When implementing new features, you should start by creating a new branch named ``feature-[short description]`` derived from the ``develop`` branch, for example

.. code-block:: bash

    $ git checkout -b feature-new-user-profile develop


Commiting the changes
---------------------

To run all tests and check whether all required pre-commit githooks are satisfied, run 

.. code-block:: bash

    $ pre-commit run --all-files

Your commit message should briefly summarize the changes (if possible) in plain English. To learn how to write a proper commit message, check out `this article <https://juffalow.com/other/write-good-git-commit-message>`_.

When ready, create a new pull request compared with the ``develop`` branch set as a base branch.

Documentation
=============

For the lastest stable release, the documentation can be seen at `docs.maisie.dev <https://docs.maisie.dev>`_.

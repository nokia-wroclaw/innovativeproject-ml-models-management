ML Models Management System
###########################

.. contents:: \

.. section-numbering::


Features
========

TODO: next milestone
--------------------

- basic web ui
    - login/register
    - browse/filter/sort projects
    - browse/filter/sort models in project
    - connect/create project
- CLI
- REST API
- project
    - every project is conncted with exactly one repo if any
        - if project is connected to repo every model is attached to exactly one commit
    - gitlab integration
        - project might be connected to gitlab repo
            - read/write permisions are imported form repo
- model
    - every model consists of
        - dataset name
        - model name (useful if multiple models are being developed simultaneously in one project)
        - commit id (optional)
        - parameters (float, string or json)
        - hiperparameters (float, string or json)
        - results (always float, results such as accuracy)

Installing
==========

You can get the most current package from `PyPI <https://test.pypi.org/>`_

.. code-block:: bash

    $ pip install mlmm-TODO

Using it in your training environment is fairly straightforward:

.. code-block:: python

    import mlmm-TODO

    mlmm = MLMM_TODO(token="")

    with mlmm(example=example) as models_management:
        # something
        models_management.upload(
            project=project, workspace=workspace, version=2
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

- `Frontend image on Docker Hub <https://hub.docker.com>`_
- `Backend image on Docker Hub <https://hub.docker.com>`_
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

For the lastest stable release, the documentation can be seen at **mlmm-TODO**.

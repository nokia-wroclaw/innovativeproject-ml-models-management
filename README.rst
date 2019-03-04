ML Models Management System
###########################

.. contents:: \

.. section-numbering::


Features
========

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

To stop your services, you can press Ctrl+C/Ctrl+D. If you started the services in the background using  ``docker-compose up -d``, the correct way is:

.. code-block:: bash

	$ docker-compose stop

You can learn more about Docker Compose by `clicking here <https://docs.docker.com/compose/>`_.

Fetching individual images
--------------------------

Both frontend and backend images are automatically published to `Docker Hub <https://hub.docker.com>`_ as soon as new stable release is made available.

Links

- `Frontend image on Docker Hub <https://hub.docker.com>`_
- `Backend image on Docker Hub <https://hub.docker.com>`_

Contributing
============

Getting started
---------------

1. Clone the repository from the ``develop`` branch

.. code-block:: bash

	$ git clone -b develop git@github.com:nokia-wroclaw/innovativeproject-ml-models-management.git

2. Install `pre-commit <https://pre-commit.com/#install>`_

3. Inside the project's root directory install all required githooks

.. code-block:: bash

	$ pre-commit install

4. Fire up required containers for local development

.. code-block:: bash

	$ docker-compose up

5. You're ready to go!

Fixing existing issues
----------------------

1. Pick one of the `open issues <https://github.com/nokia-wroclaw/innovativeproject-ml-models-management/issues>`_ or `create a new one <https://github.com/nokia-wroclaw/innovativeproject-ml-models-management/issues/new>`_

2. Create a new branch named ``issue-[number]-[short description]`` derived from the ``develop`` branch, for example

.. code-block:: bash

	$ git branch -b issue-42-project-removal-permissions develop

3. Make sure your implementation fixes the actual problem and is well tested. 

  In the final commit message you can use keywords such as *Resolves #42*, *Fixes #42* or *Closes #42* to automatically mark the issue closed)

4. After commiting the changes, create a pull request with the ``develop`` branch.

Implementing new features
-------------------------

1. Create a new branch named ``feature-[short description]`` derived from the ``develop`` branch, for example

.. code-block:: bash

	$ git branch -b feature-new-user-profile develop

2. After commiting the changes, create a pull request with the ``develop`` branch.

Documentation
=============

For the lastest stable release, the documentation can be seen at **mlmm-TODO**.
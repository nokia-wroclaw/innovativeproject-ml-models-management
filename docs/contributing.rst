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

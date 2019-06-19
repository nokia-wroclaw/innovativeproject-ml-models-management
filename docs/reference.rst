Full API Reference
==============

.. contents:: 
  :depth: 3

Backend API
-----------

Available Endpoints
~~~~~~~~~~~~~~~~~~~

.. qrefflask:: app:create_app()
  :undoc-static:

API Details
~~~~~~~~~~~

.. autoflask:: app:create_app()
  :endpoints:
  :order: path
  :undoc-static:


Client API
----------

Main Package Modules
~~~~~~~~~~~~~~~

.. automodule:: maisie.resources.models
    :members:
    :undoc-members:

.. automodule:: maisie.resources.projects
    :members:
    :undoc-members:

.. automodule:: maisie.resources.users
    :members:
    :undoc-members:

.. automodule:: maisie.resources.workspaces
    :members:
    :undoc-members:

Additional Package Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: maisie.core
    :members:
    :undoc-members:
    :private-members:
  
.. automodule:: maisie.utils.auth
    :members:
    :undoc-members:
    :private-members:

.. automodule:: maisie.utils.git
    :members:
    :undoc-members:
    :private-members:

.. automodule:: maisie.utils.logging
    :members:
    :undoc-members:
    :private-members:

.. automodule:: maisie.utils.misc
    :members:
    :undoc-members:
    :private-members:



Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. click:: maisie.interface:cli
  :prog: maisie
  :show-nested:
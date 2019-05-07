Full API Reference
==============

.. contents:: 
  :depth: 3

Client API
----------

Package Modules
~~~~~~~~~~~~~~~

.. automodule:: client.maisie.core
    :members:
    :undoc-members:

.. autoclass:: client.maisie.core.BaseAction

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. click:: maisie.interface:cli
  :prog: maisie
  :show-nested:

Backend API
-----------

Summary
~~~~~~~
.. qrefflask:: app:create_app()
  :undoc-static:

API Details
~~~~~~~~~~~

.. autoflask:: app:create_app()
  :undoc-static:
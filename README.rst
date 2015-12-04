djangocms-grid
==============

A Multi Column Plugin for django CMS, that uses a common grid system.


Installation
------------

This plugin requires `django CMS` 2.4 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-grid``.
* Add ``'djangocms_grid'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate djangocms_grid``.
  
If you are using Django 1.6 and South < 1.0.2, you must also add:

	'djangocms_grid': 'djangocms_grid.migrations_django',

to your ``settings.SOUTH_MIGRATION_MODULES``.


Configure your grid
-------------------

You can configure your grid using three numbers: total width of grid, number of
columns, and width of the gutter in between each column::

    DJANGOCMS_GRID_CONFIG = {
        'COLUMNS': 24,
        'TOTAL_WIDTH': 960,
        'GUTTER': 20,
    }

The above example is the default, which, incidentally, matches the widely used 960 grid.

Usage
-----

.. _virtualenv: http://www.virtualenv.org/en/latest/

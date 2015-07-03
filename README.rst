============
Django-sympa
============

.. image:: https://landscape.io/github/unistra/django-sympa/master/landscape.svg?style=flat
   :target: https://landscape.io/github/unistra/django-sympa/master
   :alt: Code Health

.. image:: https://secure.travis-ci.org/unistra/django-sympa.png?branch=master
    :target: https://travis-ci.org/unistra/django-sympa

.. image:: https://coveralls.io/repos/unistra/django-sympa/badge.png?branch=master
    :target: https://coveralls.io/r/unistra/django-sympa?branch=master

.. image:: https://img.shields.io/pypi/v/django-sympa.svg
    :target: https://crate.io/packages/django-sympa/

.. image:: https://img.shields.io/pypi/dm/django-sympa.svg
    :target: https://crate.io/packages/django-sympa/

Install
=======

With pip ::

    $> pip install django-sympa


In your django project, be sure that the ``auth`` application is installed : ::

    # settings.py
    INSTALLED_APPS = (
        ...,
        'django.contrib.auth',
        ...
    )

Add the ``sympa`` application to your project. ``INSTALLED_APPS`` looks like : ::

    # settings.py
    INSTALLED_APPS = (
        ...,
        'django.contrib.auth',
        ...,
        'sympa'
    )

Add a route to your base urls configuration : ::

    # urls.py

    urlpatterns = (
        ...
        url('^users.sympa$', 'sympa.views.users', name='sympa_users'),
        ...
    )

That's it !

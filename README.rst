==========================
django-icelandic-addresses
==========================

.. image:: https://badge.fury.io/py/django-icelandic-addresses.png
    :target: http://badge.fury.io/py/django-icelandic-addresses

.. image:: https://travis-ci.org/StefanKjartansson/django-icelandic-addresses.png?branch=master
        :target: https://travis-ci.org/StefanKjartansson/django-icelandic-addresses

.. image:: https://pypip.in/d/django-icelandic-addresses/badge.png
        :target: https://crate.io/packages/django-icelandic-addresses?version=latest


Django app containing a list of Icelandic addresses


Getting It
==========

You can get django-icelandic-addresses by using pip or easy_install::

 $ pip install django-icelandic-addresses
 or
 $ easy_install django-icelandic-addresses


Installing It
=============

To enable `ice_addresses` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file::

 INSTALLED_APPS = (
     ...
     'ice_addresses',
     ...
 )


Using It
========

Run migrations::

 $ python manage.py migrate ice_addresses

Import data from staðfangaskrá::

 $ python manage.py import_ice_addresses


And in code::

    from ice_addresses.models import Address, Street

    laugavegur_1 = Address.objects.filter(
        street=Street.objects \
            .filter(name_nominative='Laugavegur') \
            .filter(postcode__id=101),
        house_number=1)

TODO
====

* Address form

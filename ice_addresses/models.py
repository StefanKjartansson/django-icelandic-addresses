#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class PostCode(models.Model):
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return '%d' % self.id


@python_2_unicode_compatible
class Street(models.Model):
    postcode = models.ForeignKey(PostCode)
    name_nominative = models.CharField(max_length=48, db_index=True)
    name_genitive = models.CharField(max_length=48, db_index=True)

    def __str__(self):
        return '%s, %s' % (self.name_nominative, str(self.postcode))


@python_2_unicode_compatible
class Address(models.Model):
    street = models.ForeignKey(Street)
    house_number = models.IntegerField(default=0)
    house_characters = models.CharField(max_length=3, default='')
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        s = "%s " % self.street.name_nominative
        if self.house_number > 0:
            s += (str(self.house_number))
        s += self.house_characters
        s += ", %s" % str(self.street.postcode)
        return s

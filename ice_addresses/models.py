#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.db import models


class PostCode(models.Model):
    id = models.IntegerField(primary_key=True)


class Street(models.Model):
    postcode = models.ForeignKey(PostCode)
    name_nominative = models.CharField(max_length=48, db_index=True)
    name_genitive = models.CharField(max_length=48, db_index=True)


class Address(models.Model):
    street = models.ForeignKey(Street)
    house_number = models.IntegerField(default=0)
    house_characters = models.CharField(max_length=1, default='')
    lon = models.FloatField()
    lat = models.FloatField()

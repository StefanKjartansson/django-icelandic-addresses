#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.core.management import call_command
from django.test import TestCase

from .models import Address, Street


class ImportIceAddressTestCase(TestCase):

    def test_run_mgmt_command(self, **kwargs):
        call_command('import_ice_addresses',
                     interactive=False,
                     verbosity='0',
                     **kwargs)

        c = Address.objects.filter(
            street=Street.objects \
                .filter(name_nominative='Laugavegur') \
                .filter(postcode__id=101),
            house_number=1).count()

        self.assertGreater(c, 0)

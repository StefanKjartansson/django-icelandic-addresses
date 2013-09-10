#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.core.management import call_command
from django.test import TestCase

from .models import Address, Street
from .utils import address_exists, string_to_address


test_addresses = [
    'Vatnsstígur 3b, 101',
    'Vatnsstígur 3b, 101 Reykjavík',
    'Stóra-Hofi, 851',
    'Stóra-Hofi, 851 Hellu (dreifbýli)',
]


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

        result, id = address_exists('Laugavegur', 101, 1)

        self.assertTrue(result)

        a = Address.objects.get(pk=id)

        self.assertEqual(str(a), "Laugavegur 1, 101")

        for x in test_addresses:
            self.assertIsNotNone(string_to_address(x))

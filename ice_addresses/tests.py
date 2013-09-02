#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

import os
import tempfile
import shutil

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class ImportIceAddressTestCase(TestCase):

    def test_run_mgmt_command(self, **kwargs):
        call_command('import_ice_addresses',
                     interactive=False,
                     verbosity='0',
                     **kwargs)

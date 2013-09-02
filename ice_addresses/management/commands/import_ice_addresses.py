#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from optparse import make_option

from django.core.management.base import NoArgsCommand

from ...importers.csv import import_csv


class Command(NoArgsCommand):

    option_list = NoArgsCommand.option_list + (
        make_option('--filename',
            action='store',
            dest='filename',
            default=None,
            help='Custom filename'),
        )

    def handle_noargs(self, *args, **options):
        c = import_csv(options.get('filename'))
        self.stdout.write('%d records imported\n' % c)

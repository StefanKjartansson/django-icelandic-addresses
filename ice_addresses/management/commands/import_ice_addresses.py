#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

from optparse import make_option

from django.core.management.base import NoArgsCommand

from ...importers.csv import import_csv
from ...models import Address


class Command(NoArgsCommand):

    option_list = NoArgsCommand.option_list + (
        make_option('--filename',
            action='store',
            dest='filename',
            default=None,
            help='Custom filename'),
        make_option('--no-override',
            action='store_true',
            dest='no_override',
            default=False,
            help='If supplied, checks to see if there is already data in the db'),
        )

    def handle_noargs(self, *args, **options):
        if options.get('no_override') and Address.objects.count() > 0:
            self.stdout.write('data already exists')
            return
        c = import_csv(options.get('filename'))
        self.stdout.write('%d records imported\n' % c)

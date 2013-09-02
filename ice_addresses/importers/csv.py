#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

import decimal
import os
import codecs
import csv

from ..models import PostCode, Street, Address
from ..geo import isnet93_to_wgs84


DATA_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, 'data')


def csv_unireader(f, encoding="utf-8"):
    r = csv.reader(codecs.iterencode(codecs.iterdecode(f, encoding), 'utf-8'),
        delimiter=b'|', quotechar=b'"')
    for row in r:
        yield [e.decode("utf-8") for e in row]


def import_csv(filename=None):

    uniques = set()

    if not filename:
        filename = os.path.join(DATA_ROOT, 'Stadfangaskra_20130326.dsv')

    for fields in csv_unireader(open(filename), encoding='iso-8859-1'):

        if fields[0] == 'HNITNUM':
            continue

        try:
            postcode = int(fields[7])
        except ValueError:
            postcode = 0

        try:
            house_number = int(fields[10])
        except ValueError:
            house_number = 0

        point = isnet93_to_wgs84(
            float(fields[-2].replace(',', '.')),
            float(fields[-1].replace(',', '.')))

        uniques.add((
            postcode,
            fields[8].strip(),
            fields[9].strip(),
            house_number,
            fields[11].strip(),
            point['lat'],
            point['lng'],
        ))

    current_code = None
    pc = None
    current_names = None
    s = None

    for code, name1, name2, house_number, house_chars, lat, lng in sorted(uniques):

        if current_code != code:
            pc = PostCode(id=code)
            pc.save()
            current_code = code

        if current_names != (name1, name2):
            s = Street(
                postcode=pc,
                name_nominative=name1,
                name_genitive=name2)
            s.save()
            current_names = (name1, name2)

        Address(
            street=s,
            house_number=house_number,
            house_characters=house_chars,
            lat=lat,
            lon=lng).save()

    return len(uniques)

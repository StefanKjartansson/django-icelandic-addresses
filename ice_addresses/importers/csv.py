#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

import codecs
import csv
import os
import sys

from ..models import PostCode, Street, Address


DATA_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), os.pardir, 'data')
PY3 = (sys.version_info[0] > 2)


def csv_unireader(f, encoding="utf-8"):
    if PY3:
        f = codecs.open(f, encoding=encoding)
        r = csv.reader(f, delimiter='|', quotechar='"')
    else:
        r = csv.reader(
            codecs.iterencode(codecs.iterdecode(open(f), encoding), 'utf-8'),
            delimiter=b'|', quotechar=b'"')
    for row in r:
        if PY3:
            yield row
        else:
            yield [e.decode("utf-8") for e in row]


def import_csv(filename=None):

    uniques = set()

    if not filename:
        filename = os.path.join(DATA_ROOT, 'Stadfangaskra_20131028.dsv')

    for fields in csv_unireader(filename, encoding='iso-8859-1'):

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

        uniques.add((
            postcode,
            fields[8].strip(),
            fields[9].strip(),
            house_number,
            fields[11].strip(),
            float(fields[-2].replace(',', '.')),
            float(fields[-1].replace(',', '.')),
        ))

    uniques = sorted(uniques)

    def get_insert_method(model):

        if model.objects.count() > 0:
            return model.objects.get_or_create

        def _wrap(*args, **kwargs):
            return model.objects.create(*args, **kwargs), True

        return _wrap

    codes = {}
    _m = get_insert_method(PostCode)
    for c in set((i[0] for i in uniques)):
        pc, _ = _m(id=c)
        codes[c] = pc

    streets = {}
    _m = get_insert_method(Street)

    for key in set((i[0:3] for i in uniques)):
        pc, name1, name2 = key
        s, _ = _m(
            postcode=codes[pc],
            name_nominative=name1,
            name_genitive=name2)
        streets[key] = s

    _m = get_insert_method(Address)
    for code, name1, name2, house_number, house_chars, lat, lng in uniques:
        _m(street=streets[(code, name1, name2)],
           house_number=house_number,
           house_characters=house_chars,
           lat=lat,
           lon=lng)

    return len(uniques)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from __future__ import unicode_literals, print_function, absolute_import

import re

from .models import PostCode, Street, Address


re_postcode = re.compile('(\d{3})')
re_street = re.compile(u'((?<!\d)[a-zéýíóðáæö-]+)', re.U | re.I)
re_number = re.compile('(\d+[a-zA-Z]?)')


def address_exists(street_name, postcode, house_number=0, house_characters=''):

    try:
        postcode = int(postcode)
    except ValueError:
        return (False, 'Invalid postcode')

    if house_number != 0:
        try:
            house_number = int(house_number)
        except ValueError:
            return (False, 'Invalid house number')

    matches = Street.objects.filter(name_nominative=street_name) \
        .filter(postcode__id=postcode) | \
        Street.objects.filter(name_genitive=street_name) \
        .filter(postcode__id=postcode)

    if not matches:
        return (False, 'No street address found')

    # Filter out duplicates (same nominative & genitive)
    matches = set(matches)

    if len(matches) > 1:
        return (False, 'More than one street found for this postcode')

    try:
        a = Address.objects.get(
            street=matches.pop(),
            house_number=house_number,
            house_characters=house_characters)

        return (True, a.id)

    except Address.DoesNotExist:
        pass

    return (False, 'Address does not exist')


def string_to_address(string):
    """
    Tries to parse the input string and return a valid address
    """

    if len(string) == 0:
        return None

    # Find all 3 digit blocks
    postcode_matches = list(re_postcode.finditer(string))

    if not postcode_matches:
        return None

    # ignore any content that comes after the last postcode match
    string = string[:postcode_matches[-1].end()]

    # normalize the postcode list
    postcode_matches = [i.group() for i in postcode_matches]

    # Findall text content
    street_matches = re_street.findall(string)
    if not street_matches:
        return None

    # findall housenumber matches
    housenumber_matches = re_number.findall(string)

    if len(postcode_matches) == 1:
        # we can safely filter out the postcode
        # match since we have only one of those
        housenumber_matches = list(set(housenumber_matches) -
                                   set(postcode_matches))
        postcode_matches = postcode_matches[0]

    else:

        # more than one postcode, query the database.
        pc = PostCode.objects.filter(id__in=map(int, postcode_matches))
        if pc.count() > 2:
            return None
        postcode_matches = pc[0].id

    context = {}

    if housenumber_matches:
        # Can't do much if we have more than one housenumber match.
        if len(housenumber_matches) > 1:
            return None
        for p in [i for i in re.split('(\d+)', housenumber_matches[0]) if i]:
            try:
                int(p)
                context['house_number'] = p
            except ValueError:
                context['house_characters'] = p

    # Call the address_exists function
    result, id_msg = address_exists(
        ' '.join(street_matches),
        postcode_matches,
        **context)

    if not result:
        return None

    return Address.objects.get(pk=id_msg)

"""Module that have a function with a dict of cuntries this function recieve 
an argument iso code that itbe use to match code in dict and return it
"""


def get_country(iso_code=None):
    # Create dictionary with country name and their codes
    country_dict = {
        'DK': {
            'name': 'Denmark'
        },
        'DE': {
            'name': 'Germany'
        },
        'UK': {
            'name': 'United Kingdom'
        },
        'SE': {
            'name': 'Sweden'
        },
        'NO': {
            'name': 'Norway'
        }
    }

    if type(iso_code) != str:
        raise TypeError('iso_code need to be a string')
    elif len(iso_code) != 2:
        raise ValueError('iso_code need to be 2 characters long')

    # If parameter code is in dictionary return true else return false
    if iso_code in country_dict:
        return True, country_dict[iso_code]
    else:
        return False, None

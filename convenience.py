"""
convenience.py.

Just a miscellaneous mess of functions.
"""


IMMUTABLE_TYPES = (bool, int, float, tuple, str, frozenset, type(None))


def get_from_dict(keys, dict):
    """Gets value from dict. I.e. dict[key0][key1]..."""
    val = dict.copy()
    for key in keys:
        val = val[key]

    return val


def set_in_dict(keys, value=None, dict=None):
    """
    Sets value in dict. I.e. dict[key0][key1][key2]... = value
    If dict is None, then create a new dict. Default value is None.
    Will overwrite 'unassignable' types in dict if in path; types that won't
    allow you to assign a value.
    """
    if dict is None:
        d = {}
        # refer to d to keep whole dict; d is subset of dict
        dict = d
    else:
        d = dict

    for key in keys[:-1]:
        # This will overwrite unassignable types
        if key not in d.keys() or type(d[key]) in IMMUTABLE_TYPES + (set,):
            d[key] = {}
            d = d[key]
        # This preserves mutable values
        else:
            d = d.setdefault(key, {})

    d[keys[-1]] = value
    return dict

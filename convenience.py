"""
convenience.py.

Just a miscellaneous mess of functions.
"""


IMMUTABLE_TYPES = (bool, int, float, tuple, str, frozenset, type(None))


def get_from_dict(keys, dict):
    """Retrieves value from `dict` using `keys`.

    It's a neat way of obtaining a value from a dictionary without a mess of
    nested keys, especially when using variable keys.

    Parameters
    ----------
    keys : list of immutables
        List of keys in descending hierarchical order to search for in `dict`.
    dict : dict
        A dictionary

    Returns
    -------
    Any type

    """
    val = dict.copy()
    for key in keys:
        val = val[key]

    return val


def set_in_dict(keys, value=None, dict=None):
    """Sets `value` in `dict` using `keys`.

    It's a neat way of setting a value in a dictionary without a mess of
    nested keys, especially when using variable keys.

    Will create a new dict if `dict` is None. If a key somewhere along the path
    is mutable, it will be overwritten as an empty dict. If a key is
    non-existent, it will be set to an empty dict.

    Parameters
    ----------
    keys : list of immutables
        List of keys in descending hierarchical order to search for in `dict`.
    value : Any type, optional
        The value to be set in `dict` using `keys`. Defaults to None.
    dict : dict, optional
        The dictionary to be changed. Defaults to None. If `dict` is None, then
        creates dict.

    Returns
    -------
    dict
        Altered copy of `dict`. (is copy the right word?)

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

from flask_stupe import bson, dateutil


def boolean(value):
    """Parse the string ``"true"`` or ``"false"`` as a boolean (case
    insensitive). Also accepts ``"1"`` and ``"0"`` as ``True``/``False``
    (respectively). If the input is from the request JSON body, the type is
    already a native python boolean, and will be passed through without
    further parsing.

    This function belongs to https://github.com/flask-restful/flask-restful
    It is licensed under the BSD 3-clause "New" or "Revised" License
    https://github.com/flask-restful/flask-restful/blob/master/LICENSE
    """
    if isinstance(value, bool):
        return value

    if not value:
        raise ValueError("boolean type must be non-null")
    value = value.lower()
    if value in ('true', '1',):
        return True
    if value in ('false', '0',):
        return False
    raise ValueError("Invalid literal for boolean(): {0}".format(value))


def str_list(value):
    """Separate a string in multiple elements separated by comma."""
    if not value:
        return []
    return value.split(",")


__all__ = ["boolean", "str_list"]


if bson:
    def objectid_list(value):
        """Separate a string in multiple ObjectIds separated by comma."""
        return [bson.ObjectId(element) for element in str_list(value)]

    __all__.append("objectid_list")


if dateutil:
    def datetime(value):
        """Convert a string to a datetime"""
        return dateutil.parser.parse(value)

    def date(value):
        """Convert as string to a date"""
        return datetime(value).date()

    __all__.extend(["datetime", "date"])

def get_in(obj, path):
    """
    Get a nested property from a nested object or array.
    Returns the Symbol undefined when not found.
    """
    value = obj
    i = 0

    while i < len(path) and value is not undefined:
        key = path[i]

        if type(value) is dict:
            value = value[key] if key in value else undefined
        elif type(value) is list:
            index = int(key)
            value = value[index] if index < len(value) else undefined
        else:
            value = undefined

        i += 1

    return value


class Symbol(object):
    def __init__(self, name):
        self.name = name


undefined = Symbol("undefined")

 an inherited class-checking function
or an instance in the inherited class"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class
    or a class that the class in question inherits from"""
    if isinstance(obj, a_class):
        return True
    return False

"""
This file contains stuff for helper functions for making actual maths functions 
"""

class helper:

    def is_iterable(obj) -> bool:
        return hasattr(obj[0], "__iter__") and not isinstance(obj[0], (str, bytes))

    def to_number_list(obj):
        if len(obj) == 1 and helper.is_iterable(obj):
            return list(obj[0])
        return list(obj)
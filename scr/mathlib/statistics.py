from .exception import *
from .utility   import *

class Statistics:

    def mean(*args):
        numbers = helper.to_number_list(args)

        if not numbers:
            raise EmptyDataError("mean()")

        return sum(numbers) / len(numbers)
"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate how many minutes the lasagna still needs to bake.

    :param elapsed_bake_time: int - the number of minutes the lasagna has already baked.
    :return: int - remaining bake time in minutes.
    
    Example:
    >>> bake_time_remaining(30)
    10
    """

    return (EXPECTED_BAKE_TIME - elapsed_bake_time)

def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the total preparation time based on the number of layers.

    Each layer takes 2 minutes to prepare.

    :param number_of_layers: int - number of layers added to the lasagna.
    :return: int - total preparation time in minutes.

    Example:
    >>> preparation_time_in_minutes(3)
    6
    """
    return (number_of_layers*PREPARATION_TIME)
    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total time spent in the kitchen so far.

    This is the sum of the preparation time (based on the number of layers)
    and the time the lasagna has already spent baking.

    :param number_of_layers: int - number of layers added to the lasagna.
    :param elapsed_bake_time: int - minutes the lasagna has already baked.
    :return: int - total elapsed time in minutes.

    Example:
    >>> elapsed_time_in_minutes(3, 20)
    26
    """
    result = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return result
    


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

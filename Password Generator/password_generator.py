import random
from copy import copy
from string import ascii_letters, digits, punctuation


class Password:
    """
    A class for generating random passwords with varying levels of strength.

    Attributes:
        INPUT_UNIVERSE (dict): Character sets used for password generation, 
            containing 'numbers', 'letters', and 'punctuation'.
        DEFAULT_LENGTHS (dict): Default password lengths for each strength level 
            (low, mid, high).
    """

    INPUT_UNIVERSE = {
        'numbers': list(digits),
        'letters': list(ascii_letters),
        'punctuation': list(punctuation)
    }

    DEFAULT_LENGTHS = {
        'low': 8,
        'mid': 12,
        'high': 16
    }

    @classmethod
    def show_input_universe(cls):
        """
        Show the character sets used to generate passwords.
        
        Returns:
            dict: The available character sets for password generation.
        """
        return cls.INPUT_UNIVERSE

    def __init__(self, strength='mid', length=None):
        """
        Initialize a Password instance with the given strength and length.
        
        Parameters:
            strength (str): The desired strength level of the password ('low', 'mid', or 'high'). 
                Defaults to 'mid'.
            length (int, optional): The desired length of the password. 
                If not provided, the default length for the given strength is used.
        """
        self._strength = strength
        self._length = length

        self._generate()

    def _generate(self):
        """
        Generate a random password based on the given strength and length.
        
        Uses a combination of letters, numbers, and punctuation based on the strength level.
        """
        population = copy(self.INPUT_UNIVERSE['letters'])
        length = self._length or self.DEFAULT_LENGTHS.get(self._strength)

        if self._strength == 'high':
            population += self.INPUT_UNIVERSE['numbers'] + \
                self.INPUT_UNIVERSE['punctuation']
        else:
            population += self.INPUT_UNIVERSE['numbers']

        self.password = ''.join(
            list(map(str, random.choices(population, k=length)))
        )

    def __str__(self):
        """
        Return the generated password as a string.
        
        Returns:
            str: The generated password.
        """
        return self.password




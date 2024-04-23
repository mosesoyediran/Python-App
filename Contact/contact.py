class Contact:
    """
    Represents a contact with personal information, such as first name, last name, phone, and email.

    This class supports different display modes, including masking sensitive information,
    and allows for customized string representations, equality comparisons, and hashing.

    Attributes:
        _first_name (str): The contact's first name.
        _last_name (str): The contact's last name.
        _phone (str, optional): The contact's phone number. Defaults to None.
        _email (str, optional): The contact's email address. Defaults to None.
        _display_mode (str): Mode for displaying contact information. Can be 'masked' or 'full'. Defaults to 'masked'.

    Methods:
        __repr__():
            Returns a detailed representation of the contact, considering the display mode.

        __eq__(other):
            Checks if this contact is equal to another based on first and last name,
            phone, or email.
        
        __hash__():
            Returns a hash based on first name, last name, phone, and email.
        
        __str__():
            Returns a simplified representation of the contact using initials.
        
        __format__(__format_spec):
            Formats the contact based on the specified format.
            Supports 'masked' format to obfuscate personal information.

        _obfuscate(text):
            Static method to obfuscate half of a given text with asterisks.
        
    """
    def __init__(self, first_name, last_name, phone=None, email=None, display_mode='masked'):
        """
        Initializes a contact with the specified information.

        Args:
            first_name (str): The contact's first name.
            last_name (str): The contact's last name.
            phone (str, optional): The contact's phone number. Defaults to None.
            email (str, optional): The contact's email address. Defaults to None.
            display_mode (str): The mode for displaying contact information. Can be 'masked' or 'full'.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._email = email
        self._display_mode = display_mode

    def __repr__(self):
        """
        Provides a detailed string representation of the contact, depending on the display mode.

        Returns:
            str: The representation of the contact, with masking if 'masked' display mode is used.
        """
        if self._display_mode == 'masked':
            return f"Contact(first name='{self._obfuscate(self._first_name)}', last name='{self._obfuscate(self._last_name)}')"
        else:
            return f"Contact(first name='{self._first_name}', last name='{self._last_name}', Phone='{self._phone}', Email='{self._email}')"

    def __eq__(self, other):
        """
        Checks if this contact is equal to another contact.

        Args:
            other (Contact): The other contact to compare with.

        Returns:
            bool: True if the contacts are considered equal based on email, phone, first name, or last name, False otherwise.
        
        """
        if not isinstance(other, Contact):
            return False

        return (self._email and self._email == other._email) or \
               (self._phone and self._phone == other._phone) or \
               (self._first_name == other._first_name and self._last_name == other._last_name)

    def __hash__(self):
        """
        Returns a hash value for the contact.

        Returns:
            int: A hash based on first name, last name, phone, and email.
        """
        return hash((self._first_name, self._last_name, self._phone, self._email))

    def __str__(self):
        """
        Returns a simplified representation of the contact.

        Returns:
            str: A string using initials from first and last names.
        """
        return f'{self._last_name[0]}{self._first_name[0]}'

    def __format__(self, __format_spec):
        """
        Formats the contact based on the specified format specifier.

        Args:
            __format_spec (str): The format specifier.
        
        Returns:
            str: The formatted contact information, with 'masked' format for obfuscation.
        """
        if __format_spec == 'masked':
            return repr(self)
        else:
            return f"Contact(first name='{self._first_name}', last name='{self._last_name}', Phone='{self._phone}', Email='{self._email}')"

    @staticmethod
    def _obfuscate(text):
        """
        Obfuscates half of the given text with asterisks.
        
        Args:
            text (str): The text to obfuscate.
        
        Returns:
            str: The obfuscated text with asterisks in the second half.
        """
        half_length = len(text) // 2
        return text[:half_length] + '*' * (half_length + 1)

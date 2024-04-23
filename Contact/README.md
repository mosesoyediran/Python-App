# Contact Class

The `Contact` class is designed to represent a contact with personal information, such as first name, last name, phone number, and email address. This class supports different display modes, allowing for masking of sensitive information, and provides various methods for representation, comparison, and hashing.

## Features
- Allows flexible initialization with optional phone and email information.
- Supports 'masked' and 'full' display modes for handling sensitive data.
- Customizable string representations and formatters.
- Equality checks and hashing based on personal information.

## Attributes
- **_first_name**: The contact's first name.
- **_last_name**: The contact's last name.
- **_phone**: Optional phone number (default is `None`).
- **_email**: Optional email address (default is `None`).
- **_display_mode**: Specifies whether to display information in 'masked' or 'full' mode (default is 'masked').

## Methods
- **__repr__()**: Returns a detailed representation of the contact, with or without masking.
- **__eq__(other)**: Checks if this contact is equal to another based on first name, last name, phone, or email.
- **__hash__()**: Returns a hash value based on first name, last name, phone, and email.
- **__str__()**: Returns a simplified representation of the contact using initials.
- **__format__(__format_spec)**: Formats the contact based on the specified format specifier, supporting 'masked' and 'full' modes.
- **_obfuscate(text)**: Static method to obfuscate half of a given text with asterisks.

## Usage
Here's a simple example of how to use the `Contact` class:

```python
# Create a new contact with first and last name
contact = Contact('John', 'Doe')

# Print the contact with masking
print(repr(contact))  # Output: Contact(first name='Jo*', last name='Do*')

# Change to full display mode
contact._display_mode = 'full'

# Print the contact without masking
print(repr(contact))  # Output: Contact(first name='John', last name='Doe', Phone='None', Email='None')

# Equality checks
contact2 = Contact('John', 'Doe')
assert contact == contact2  # True because first name and last name are the same

# Using format specifiers
formatted_contact = format(contact, 'full')
print(formatted_contact)  # Output: Contact(first name='John', last name='Doe', Phone='None', Email='None')


Notes

Ensure that you provide valid input when creating or modifying contacts. Invalid or unrecognized data will raise a ValueError.
Use 'masked' mode to maintain confidentiality when displaying contact information in public settings




This README.md content describes the `Contact` class and provides an example of how to use it, covering important features and attributes. It is a useful guide for users who want to understand and work with the `Contact` class.

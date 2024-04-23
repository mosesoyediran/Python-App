# Password Generator

This project contains a class `Password` designed to generate random passwords with customizable strength and length. It is intended for developers who need to create secure passwords for user authentication or other security purposes.

## Features
- **Multiple Strength Levels**: Generate passwords with low, mid, or high strength.
- **Customizable Length**: Specify the exact length of the password or use the default length for each strength level.
- **Variety of Characters**: Passwords can include letters, numbers, and punctuation marks.

## Installation
To use the `Password` class, simply include it in your Python project. No additional packages or libraries are required.

## Usage
Here's an example of how to generate a password with the `Password` class:

```python
from password_generator import Password

# Generate a high-strength password with default length (16 characters)
high_strength_password = Password(strength='high')
print("High-strength password:", high_strength_password.password)

# Generate a mid-strength password with a custom length of 10 characters
custom_mid_password = Password(strength='mid', length=10)
print("Custom mid-strength password:", custom_mid_password.password)
```

## Class Explanation
### `Password`
The `Password` class is designed to generate random passwords based on user-defined strength and length. It has the following key components:

- **INPUT_UNIVERSE**: A dictionary containing character sets for numbers, letters, and punctuation.
- **DEFAULT_LENGTHS**: Default password lengths for low, mid, and high strength levels.

### Methods
- **`__init__`**: Initializes the password with the specified strength and length.
- **`_generate()`**: Generates a random password based on the specified strength and length.
- **`show_input_universe()`**: Returns the character sets used for password generation.

## License
This project is licensed under the MIT License. 

## Contributions
Contributions to this project are welcome. If you'd like to suggest a new feature or report a bug, please open an issue or submit a pull request.

## Author
This project was developed by Moses Oyediran.

---

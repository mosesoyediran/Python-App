# Tablet Class Overview

This module contains the `Tablet` class, which represents a tablet with a specific model, base storage, and memory capacity. It allows initialization of tablets with different models, adding storage, and retrieving key information like total storage, base storage, and memory capacity.

## Table of Contents
- [Tablet Class](#tablet-class)
  - [Attributes](#attributes)
  - [Methods](#methods)
  - [Usage Example](#usage-example)

## Tablet Class
The `Tablet` class represents a tablet device with different models, each having distinct base storage and memory specifications. It also has the ability to add storage and perform various checks to ensure that memory limits are not exceeded.

### Attributes
- `MAX_MEMORY`: The maximum memory/storage capacity for a tablet, set to 1024 MB.
- `MODELS`: A dictionary containing specifications for various tablet models. Available models are `lite`, `pro`, and `max`.

### Methods
- `__init__(self, model)`: Initializes a tablet with a specific model. If the model is not recognized, it raises a `ValueError`.
- `add_storage(self, additional_storage)`: Adds additional storage to the base storage. Raises a `ValueError` if the total storage exceeds the maximum limit.
- `storage()`: Property to get the total storage capacity (base storage + added storage). It has a setter to modify storage, raising a `ValueError` if it exceeds limits or is lower than base storage.
- `memory()`: Property to get the memory capacity of the tablet in GB.
- `base_storage()`: Property to get the base storage capacity of the tablet.
- `__repr__()`: Returns a string representation of the tablet, including its model, base storage, added storage, and memory.

### Usage Example
Here's an example of how to create a tablet, add storage, and set storage directly:

```python
from tablet_module import Tablet  # Adjust the import path to your module structure

# Create a tablet of the 'max' model
tablet = Tablet("max")

# Add 128 MB of additional storage
tablet.add_storage(128)

# Set the total storage to 512 MB
tablet.storage = 512

# Print the tablet's details
print(tablet)


Tablet(model='max', base_storage='128', added_storage='384', memory='4')


Contributing

If you'd like to contribute to the development or report a bug, please follow our contribution guidelines (link to guidelines).



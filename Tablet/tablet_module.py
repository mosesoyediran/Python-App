class Tablet:
    """
    Represents a tablet with a specific model, base storage, and memory capacity.

    This class provides a mechanism to initialize tablets with different models,
    set storage capacity, and add extra storage with validation against maximum limits.

    Attributes:
        MAX_MEMORY (int): The maximum memory/storage that any tablet can have.
        MODELS (dict): Dictionary containing specifications for different tablet models.
        model (str): The model name of the tablet.
        _base_storage (int): The base storage capacity for the tablet.
        _memory (int): The memory capacity for the tablet.
        _added_storage (int): Additional storage added to the base storage.
        
    Methods:
        add_storage(additional_storage):
            Adds additional storage to the base storage.
            Raises a ValueError if the total storage exceeds the maximum limit.
        
        storage():
            Property that returns the total storage capacity (base storage + added storage).

        storage.setter:
            Setter to modify storage.
            Raises a ValueError if the storage goes below base storage or exceeds the maximum memory.
        
        memory():
            Property that returns the memory capacity of the tablet.

        base_storage():
            Property that returns the base storage of the tablet.
        
        __repr__():
            Returns a string representation of the tablet with its model, base storage, added storage, and memory.
    """

    MAX_MEMORY = 1024  # Maximum storage capacity for a tablet in MB

    MODELS = {
        "lite": {
            "base_storage": 32,
            "memory": 2
        },
        "pro": {
            "base_storage": 64,
            "memory": 3
        },
        "max": {
            "base_storage": 128,
            "memory": 4
        }
    }

    def __init__(self, model):
        """
        Initializes a tablet with the specified model.

        Args:
            model (str): The name of the tablet model.
        
        Raises:
            ValueError: If the model name is not recognized.
        """
        model = model.lower().strip()
        if model not in list(self.MODELS.keys()):
            raise ValueError("Unrecognized model")

        specs = self.MODELS[model]

        self.model = model
        self._base_storage = specs['base_storage']
        self._memory = specs['memory']
        self._added_storage = 0

    def add_storage(self, additional_storage):
        """
        Adds additional storage to the tablet's base storage.

        Args:
            additional_storage (int): The amount of storage to add in MB.
        
        Raises:
            ValueError: If adding storage exceeds the maximum memory limit.
        """
        if self._base_storage + additional_storage > self.MAX_MEMORY:
            raise ValueError(f"Device memory cannot exceed maximum of {self.MAX_MEMORY}")

        self._added_storage = additional_storage

    @property
    def storage(self):
        """
        Returns the total storage capacity, including base storage and added storage.

        Returns:
            int: The total storage capacity in MB.
        """
        return self._base_storage + self._added_storage

    @storage.setter
    def storage(self, memory):
        """
        Sets the storage capacity, allowing adjustments.

        Args:
            memory (int): The desired storage capacity in MB.
        
        Raises:
            ValueError: If the new storage capacity is lower than the base storage or exceeds the maximum limit.
        """
        additional = memory - self._base_storage

        if additional < 0:
            raise ValueError(f"Device memory cannot be lower than base memory of {self._base_storage}")

        if memory > self.MAX_MEMORY:
            raise ValueError(f"Device memory cannot exceed maximum of {self.MAX_MEMORY}")

        self._added_storage = additional

    @property
    def memory(self):
        """
        Returns the memory capacity of the tablet.

        Returns:
            int: The memory capacity in GB.
        """
        return self._memory

    @property
    def base_storage(self):
        """
        Returns the base storage capacity of the tablet.

        Returns:
            int: The base storage in MB.
        """
        return self._base_storage

    def __repr__(self):
        """
        Provides a string representation of the tablet.

        Returns:
            str: A string describing the tablet with its model, base storage, added storage, and memory.
        """
        return f"Tablet(model='{self.model}', base_storage='{self.base_storage}', added_storage='{self._added_storage}', memory='{self.memory}')"




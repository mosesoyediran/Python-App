from enum import Flag, auto


class Permission(Flag):
    """
    A class representing various user permissions.

    It uses the `Flag` class from `enum` to allow bitwise operations for combining multiple permissions.
    """
    READ = auto()
    WRITE = auto()
    EXEC = auto()


class BaseUser:
    """
    A base class representing a user with certain permissions.

    Attributes:
        USER_ROLES (dict): Maps user roles to permission sets.
    """
    
    USER_ROLES = {
        'admin': Permission.READ | Permission.WRITE | Permission.EXEC,
        'user': Permission.READ,
        'manager': Permission.READ | Permission.WRITE,
        'support': Permission.EXEC,
    }

    def _infer_permission(self):
        """
        Infers the permissions for a user based on their role.

        Returns:
            Permission: The inferred permissions for the user.
        """
        permissions = Permission.READ  # Default to READ permission
        role = self.user_role

        if role in self.USER_ROLES:
            permissions = self.USER_ROLES.get(role)
        elif isinstance(role, int):  # Check if the role is an integer (bitwise combination)
            try:
                Permission(role)
            except ValueError:
                pass
            else:
                permissions = role

        return permissions

    def _validate_permission(self, permission):
        """
        Validates if the user has a specific permission.

        Args:
            permission (Permission): The permission to validate.

        Raises:
            PermissionError: If the user lacks the specified permission.
        """
        if permission not in self.permissions:
            raise PermissionError(f'User does not have {permission.name} permission')

    def read(self, file='script.py'):
        """
        Reads the content of a file.

        Args:
            file (str): The filename to read. Default is 'script.py'.

        Returns:
            str: The content of the file.

        Raises:
            PermissionError: If the user lacks read permission.
        """
        self._validate_permission(Permission.READ)

        with open(file) as f:
            return f.read()

    def write(self, file='script.py', content=''):
        """
        Writes content to a file.

        Args:
            file (str): The filename to write to. Default is 'script.py'.
            content (str): The content to write.

        Raises:
            PermissionError: If the user lacks write permission.
        """
        self._validate_permission(Permission.WRITE)

        with open(file, 'w') as f:
            f.write(content)
            print(f"Wrote '{content}' to {file}. ")

    def execute(self, file='script.py'):
        """
        Executes a Python script from a file.

        Args:
            file (str): The filename of the script to execute. Default is 'script.py'.

        Raises:
            PermissionError: If the user lacks execute permission.
        """
        self._validate_permission(Permission.EXEC)

        exec(open(file).read())

    def __repr__(self):
        """
        Represents the user as a string.

        Returns:
            str: A string representation of the user.
        """
        return f"{type(self).__name__}(name='{self.name}', user_role='{self.user_role}')"


class User(BaseUser):
    """
    A class representing a user with a name and role.

    Inherits from BaseUser to gain permission-based functionality.
    
    Attributes:
        name (str): The name of the user.
        user_role (str): The role of the user.
        permissions (Permission): The permissions inferred based on the role.
    """

    def __init__(self, name, user_role):
        """
        Initializes a new user with a name and a role, inferring permissions.

        Args:
            name (str): The name of the user.
            user_role (str): The role of the user, determining the permissions.
        """
        self.name = name
        self.user_role = user_role
        self.permissions = self._infer_permission()

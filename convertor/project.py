"""
    Store a project details including their path using this module.
"""


class Project:
    """
    This class represents a project node stored in the tree to fetch its information.
    """

    def __init__(self, name) -> None:
        """
        Constructor method to create Project object.

        Parameters:
                name (str): Name of the project.

        Returns:
            None
        """
        self.name = name
        self.parent_project = None
        self.path = [name]

    def get_name(self) -> str:
        """
        Returns the name of the project requried for storing it into the path.

        Returns:
                self.name (str): Name of the project.
        """
        return self.name

    def get_path(self) -> list:
        """
        Returns path of the project.

        Returns:
                self.path (list[str]):  List of project names representing
                                        a nested file structure.
        """
        return self.path

    def add_to_path(self, path_to_append) -> None:
        """
        Sets new path of the project by appending its parent's path details.

        Parameters:
                path_to_append (list[str]): list representing parent's path.

        Returns:
            None
        """
        self.path = path_to_append + self.path

    def set_parent(self, parent_project) -> None:
        """
        Stores the parent project object in current project object.
        Updates current project's path by appending its parent's path to iteself.

        Parameters:
                parent_project (Project): class object representing parent project.

        Returns:
            None
        """
        self.parent_project = parent_project
        self.add_to_path(parent_project.get_path())

    def get_path_str(self) -> dict:
        """
        need to add
        """
        return " > ".join(self.path)

    def __str__(self) -> str:
        """
        Overridden custom str method to print project details.

        Returns:
            str: string representing path of the said project.
        """
        return str({self.name: self.get_path_str()})

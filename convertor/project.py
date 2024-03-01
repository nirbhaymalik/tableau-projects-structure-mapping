class Project:
    def __init__(self, name):
        self.name = name
        self.parent_project = None
        self.path = [name]

    def get_name(self):
        '''
        Returns the name of the project requried for storing it into the path.

                Returns:
                        self.name (str): Name of the project.
        '''
        return self.name

    def get_path(self):
        '''
        Returns path of the project.
                Returns:
                        self.path (list[str]): List of project names representing a nested file structure.
        '''
        return self.path

    def set_path(self, path_to_append):
        '''Setter for path - to store path for project from its parent folder.'''
        self.path = self.path + path_to_append

    def set_parent(self, parent_project):
        '''Stores parent project details and adds the parent path to current node.'''
        self.parent_project = parent_project
        self.set_path(parent_project.get_path()) # update self path and include parent's path

    def __str__(self):
        return {self.name: self.path}.__str__()

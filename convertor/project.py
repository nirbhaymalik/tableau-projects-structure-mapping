'''
    Store a project details including their path using this module.
'''
class Project:
    '''
        This class represents a project node stored in the tree to fetch its information.
    '''
    def __init__(self, name):
        '''
            Constructor method to create Project object.
            
            Parameters:
                    name (str): Name of the project.
        '''
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
                    self.path (list[str]):  List of project names representing 
                                            a nested file structure.
        '''
        return [self.name]

    def add_to_path(self, path_to_append):
        '''
            Sets new path of the project by appending its parent's path details.
            
            Parameters:
                    path_to_append (list[str]): list representing parent's path.
        '''
        self.path = self.path + path_to_append

    def set_parent(self, parent_project):
        '''
            Stores the parent project object in current project object.
            Updates current project's path by appending its parent's path to iteself.
            
            Parameters:
                    parent_project (Project): class object representing parent project.
        '''
        self.parent_project = parent_project
        self.add_to_path(parent_project.get_path())

    def __str__(self):
        '''
            Overridden custom str method to print project details.
        '''
        return {self.name: self.path}.__str__()

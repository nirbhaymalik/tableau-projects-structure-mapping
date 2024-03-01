class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.parent_name = None
        self.project_path = [project_name]

    def get_name(self):
        return self.project_name

    def get_path(self):
        return self.project_path

    def set_path(self, add_path):
        self.project_path = self.project_path + add_path

    def set_parent(self, parent_project):
        self.parent_name = parent_project.get_name()

        # update self path and include parent's path
        self.set_path(parent_project.get_path())

    def __str__(self):
        return {self.project_name: self.project_path}.__str__()

"""
    Test file for project.py
"""

from convertor import Project


def test_get_name():
    """
    Test to confirm get_name method returns name of the Project correctly.
    """
    expected_name = "test_project_name"
    project = Project(expected_name)

    assert (project.get_name()) == expected_name


def test_get_path():
    """
    Test to confirm get_path method returns initial path of the Project correctly.
    """
    expected_path = ["test_path"]
    project = Project("test_path")

    assert (project.get_path()) == expected_path


def test_add_to_path():
    """
    Test to confirm add_to_path correctly appends value into the path.
    """
    project_name = "test_name"
    path_to_add = ["something", "extra"]
    expected_path = path_to_add + [project_name]

    project = Project(project_name)
    project.add_to_path(path_to_add)

    assert (project.get_path()) == expected_path


def test_set_parent():
    """
    Test to confirm if this method calls add_to_path method and updates the path of the Project.
    """
    parent_project = Project("test_parent_project")
    project = Project("test_project")
    project.set_parent(parent_project)

    assert (project.get_path()) == ["test_parent_project", "test_project"]


def test_str_method():
    """
    Test if str method is correctly returning project details.
    """
    project = Project("test_name")

    assert (str(project)) == str({"test_name": "test_name"})

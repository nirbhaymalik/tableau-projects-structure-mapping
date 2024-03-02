'''
    Test file for project.py
'''

from src.convertor.project import Project

def test_get_name():
    '''
        Test to confirm get_name method returns name of the Project correctly.
    '''
    expected_name = 'test_project_name'
    project = Project(expected_name)

    assert(project.get_name()) == expected_name

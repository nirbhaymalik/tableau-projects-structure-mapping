'''
    Test file for project.py
'''

import convertor

def test_get_name():
    '''
        Test to confirm get_name method returns name of the Project correctly.
    '''
    expected_name = 'test_project_name'
    project = convertor.Project(expected_name)

    assert(project.get_name()) == expected_name

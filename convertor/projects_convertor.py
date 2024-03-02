'''
    Projects Convertor Module docstring.
'''

import xml.etree.ElementTree as Xet
from .project import Project


def extract_projects_from_xml():
    xml_parse = Xet.parse('assets/projects.xml')

    ts_response = xml_parse.getroot()

    return ts_response[1]


def map_project_tags_to_dict(projects_xml_tags):
    projects_dict = {}

    for project in projects_xml_tags:
        row_data = {}

        for item in project.items():
            row_data[item[0]] = item[1]

        projects_dict[project.attrib['id']] = row_data

    return projects_dict


def check_key_in_dict(key, dictionary) -> bool:
    result = True
    try:
        dictionary[key]
    except KeyError:
        result = False
    return result


def add_project_with_parent(project_id, items, projects_dict, projects_as_structured_tree_nodes):
    parent_id = items['parentProjectId']
    parent_items = projects_dict[parent_id]

    if not check_key_in_dict('parentProjectId', parent_items):
        project = Project(items['name'])

        if projects_as_structured_tree_nodes[parent_id] is None:
            parent_project = Project(parent_items['name'])
            projects_as_structured_tree_nodes[parent_id] = parent_project
        else:
            parent_project = projects_as_structured_tree_nodes[parent_id]

        project.set_parent(parent_project)
        projects_as_structured_tree_nodes[project_id] = project

        return
    
    add_project_with_parent(
            parent_id, parent_items, projects_dict,
            projects_as_structured_tree_nodes
            )


def create_project_tree_nodes_list(projects_dict):
    projects_as_structured_tree_nodes = {}

    for project_id in projects_dict:
        if check_key_in_dict(project_id, projects_as_structured_tree_nodes):
            continue

        project_items = projects_dict[project_id]
        if not check_key_in_dict('parentProjectId', project_items):
            project_node = Project(project_items['name'])
            projects_as_structured_tree_nodes[project_id] = project_node
        else:
            add_project_with_parent(
                project_id, project_items, projects_dict,
                projects_as_structured_tree_nodes
                )
            
    return projects_as_structured_tree_nodes


# __all__ = [
#     'extract_projects_from_xml',
#     'map_project_tags_to_dict',
#     'check_key_in_dict',
#     'add_project_with_parent',
#     'create_project_tree_nodes_list'
# ]

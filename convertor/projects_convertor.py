'''
Projects Convertor Module docstring.
'''
import xml.etree.ElementTree as Xet
from project import Project

def extract_projects_from_xml():
    xml_parse = Xet.parse('assets/project.xml')
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

def add_project_with_parent(project_id, project_node, project_items, projects_as_structured_tree_nodes):
    project_parent_id = project_items['parentProjectId']
    if projects_as_structured_tree_nodes[project_parent_id] is not None:
        project_parent_node = projects_as_structured_tree_nodes[project_parent_id]
        project_node.set_parent(project_parent_node)
        projects_as_structured_tree_nodes[project_id] = project_node
    else:
        pass

def create_project_tree_nodes_list(projects_dict):
    projects_as_structured_tree_nodes = {}
    for project_id in projects_dict:
        if projects_as_structured_tree_nodes[project_id] is not None:
            continue
        project_items = projects_dict[project_id]
        project_node = Project(project_items['name'])
        
        if project_items['parentProjectId'] is None:
            projects_as_structured_tree_nodes[project_id] = project_node
        else:
            add_project_with_parent(project_id, project_node, project_items, projects_as_structured_tree_nodes)

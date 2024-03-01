# Importing the required libraries
from .assets.project import Project

import xml.etree.ElementTree as Xet
import pandas as pd

# Parsing the XML file
xml_parse = Xet.parse('assets/project.xml')
ts_response = xml_parse.getroot()
projects = ts_response[1]

projects_arr = {}
projects_tree: {str: Project} = {}

for project in projects:
    row_data = {}
    for item in project.items():
        row_data[item[0]] = item[1]
    projects_arr[project.attrib['id']] = row_data

def add_project_node(project_id, project_items):
    if projects_tree[project_id] is None:
        project_node = Project(project_items['name'])

        if project_items['parentProjectId'] is not None:
            parent_project_node =

            project_node.set_parent(projects_tree[])

        projects_tree[project_id] = project_node



for project_id in projects_arr:
    project_items = projects_arr[project_id]
    add_project_node()

    if projects_tree[project_id] is None:
        if project_items['parentProjectId'] is None:
            project_node = Project(project_items['name'])
        else:
            parent_project_id = project_items['parentProjectId']
            if projects_tree[parent_project_id] is not None:
                project_node.set_parent_project(projects_tree[parent_project_id])





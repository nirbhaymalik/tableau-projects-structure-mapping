"""
    Projects Convertor Module provides fuctions for the main file
    to process xml data into the requested output.
"""

import xml.etree.ElementTree as Xet
from convertor.project import Project


def extract_projects_from_xml(file_path) -> list:
    """
    Method to parse XML file and store return XML tags as an object.

    Returns:
        projects (list): List of XML tags.
    """
    xml_parse = Xet.parse(file_path)

    projects = xml_parse.getroot()[1]

    return projects


def map_project_tags_to_dict(projects_xml_tags) -> dict:
    """
    Method to extract Project information from XML tags and store
    it in python friendly data structures.

    Parameters:
        projects_xml_tags (list): List containing Projects XML tags.

    Returns:
        projects_dict (dict['id', dict[attribute, value]]):
                A dictionary containing all project information.
                'id' - Project Id read from its XML tag.
                'attribute' - XML attribute of the tag.
                'value' - respective attribute's value.
    """
    projects_dict = {}

    for project in projects_xml_tags:
        row_data = {"name": project.attrib["name"]}

        if "parentProjectId" in project.attrib:
            row_data["parentProjectId"] = project.attrib["parentProjectId"]

        projects_dict[project.attrib["id"]] = row_data

    return projects_dict


def check_key_in_dict(key, dictionary) -> bool:
    """
    Method to check if a key exists in given dict.

    Parameters:
        key (str): Key value to check.
        dictionary (dict): Dictionary to review for finding the asked Key.

    Returns:
        result (bool):  True - If key exists in the dict
                        False - If key does not exists in the dict.
    """
    try:
        dictionary[key]
    except KeyError:
        return False
    return True


def add_project_with_parent(
    project_id, items, projects_dict, projects_as_structured_tree_nodes
) -> None:
    """
    Recursive method to add a Project node to the tree and if a parent exists then try adding
    the parent by calling this function within itself for the parent project.

    Parameters:
        project_id (str): Project Id read from its XML tag.
        items (dict): Project's mapped attributes.
        projects_dict (dict): Dict of all projects
        projects_as_structured_tree_nodes (dict):
                        Dict representing the tree in which
                        the Project node needs to be added.

    Returns:
        None: Because it is modifying the provided tree.
    """
    parent_id = items["parentProjectId"]
    parent_items = projects_dict[parent_id]

    if not check_key_in_dict("parentProjectId", parent_items):
        project = Project(items["name"])

        if projects_as_structured_tree_nodes[parent_id] is None:
            parent_project = Project(parent_items["name"])
            projects_as_structured_tree_nodes[parent_id] = parent_project
        else:
            parent_project = projects_as_structured_tree_nodes[parent_id]

        project.set_parent(parent_project)
        projects_as_structured_tree_nodes[project_id] = project

        return
    add_project_with_parent(
        parent_id, parent_items, projects_dict, projects_as_structured_tree_nodes
    )


def create_project_tree_nodes_list(projects_dict) -> dict:
    """
    Method to create final result dictionary containing Projects
    with their nested path information.

    Parameters:
        projects_dict (dict):   Dictionary containing raw project
                                information extracted and mapped
                                using the source XML file.

    Returns:
        projects_as_structured_tree_nodes (dict['id', Project]):
                                Dictionary containing Project object.
                                'id' - Project Id read from its XML tag.
                                Project - Class object
    """
    projects_as_structured_tree_nodes = {}

    for project_id in projects_dict:
        if check_key_in_dict(project_id, projects_as_structured_tree_nodes):
            continue

        project_items = projects_dict[project_id]
        if not check_key_in_dict("parentProjectId", project_items):
            project_node = Project(project_items["name"])
            projects_as_structured_tree_nodes[project_id] = project_node
        else:
            add_project_with_parent(
                project_id,
                project_items,
                projects_dict,
                projects_as_structured_tree_nodes,
            )
    return projects_as_structured_tree_nodes

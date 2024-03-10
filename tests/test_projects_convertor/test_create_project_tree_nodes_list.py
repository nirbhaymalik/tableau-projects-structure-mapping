"""
Test file to perform tests for the methods:
- create_project_tree_nodes_list
- add_project_with_parent
"""

from collections import Counter

from convertor import projects_convertor as ps


def test_create_project_tree_nodes_list():
    """
    Test method to confirm the expected result for csv.
    """
    xml_tags = ps.extract_projects_from_xml(
        "tests/resources/sample-with-parents-xml-response.xml"
    )
    projects_dict = ps.map_project_tags_to_dict(xml_tags)
    projects_tree = ps.create_project_tree_nodes_list(projects_dict)
    actual = [str(project) for project in projects_tree.values()]

    expected = [
        "{'Chris Murphy': ['Chris Murphy', '2. Head Office User Reports']}",
        "{'Reports Seldom Used': ['Reports Seldom Used',"  # long line split into two
        + " 'Chris Murphy', '2. Head Office User Reports']}",
        "{'2. Head Office User Reports': ['2. Head Office User Reports']}",
        "{'CM New': ['CM New', 'Chris Murphy', '2. Head Office User Reports']}",
    ]

    assert Counter(actual) == Counter(expected)

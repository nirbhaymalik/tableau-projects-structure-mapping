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

    print(actual)

    expected = [
        "{'Chris Murphy': '2. Head Office User Reports > Chris Murphy'}",
        "{'Reports Seldom Used': '2. Head Office User Reports "  # long string split in two lines
        + "> Chris Murphy > Reports Seldom Used'}",
        "{'2. Head Office User Reports': '2. Head Office User Reports'}",
        "{'CM New': '2. Head Office User Reports > Chris Murphy > CM New'}",
    ]

    assert Counter(actual) == Counter(expected)

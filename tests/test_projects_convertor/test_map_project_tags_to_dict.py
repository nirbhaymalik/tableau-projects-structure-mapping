"""
    Test file to check behaviour for map_project_tags_to_dict.
"""

from convertor import projects_convertor as ps


def test_map_project_tags_to_dict():
    """
    Test to confirm that source code maps projects' xml tags correctly
    and returns projects with all its information.
    """
    xml_tags = ps.extract_projects_from_xml(
        "tests/resources/sample-with-parents-xml-response.xml"
    )
    actual = ps.map_project_tags_to_dict(xml_tags)

    expected = {
        "4b3924b2-7eee-4eaa-acff-ccfee3f2ad29": {
            "name": "Chris Murphy",
            "parentProjectId": "cb45572d-9a90-469f-b3c3-2d43a79fe3e1",
        },
        "047bae70-fd36-4921-85d2-9a902fa4c76b": {
            "name": "Reports Seldom Used",
            "parentProjectId": "4b3924b2-7eee-4eaa-acff-ccfee3f2ad29",
        },
        "cb45572d-9a90-469f-b3c3-2d43a79fe3e1": {"name": "2. Head Office User Reports"},
        "cb574fed-373c-4b55-b31d-0570f42fa77e": {
            "name": "CM New",
            "parentProjectId": "4b3924b2-7eee-4eaa-acff-ccfee3f2ad29",
        },
    }

    assert isinstance(actual, dict)
    assert (actual) == expected

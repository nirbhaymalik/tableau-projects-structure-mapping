'''
    Test file to check behaviour for extract_projects_from_xml.
'''

from convertor import projects_convertor as pc

def test_extract_projects_from_xml():
    '''
        Test to confirm that source code parses projects xml correctly
        and returns projects with all its information.
    '''
    file_path = 'tests/resources/sample-xml-response.xml'
    actual = pc.extract_projects_from_xml(file_path)

    expected = [
        {
            'tag': '{http://tableau.com/api}project',
            'attrib': {
                'id': 'dd290932-cd1a-11e8-b0b0-1f0ed16bcc61',
                'name': 'Default',
                'description': 'The default project that was automatically created by Tableau.',
                'createdAt': '2018-10-11T05:59:33Z',
                'updatedAt': '2019-05-29T03:38:54Z',
                'contentPermissions': 'ManagedByOwner'
            },
            'owner': {
                'id': '12baf4c5-4009-4d60-899e-5f1997941c40'
            }
        },
        {
            'tag': '{http://tableau.com/api}project',
            'attrib': {
                'id': '315b24e3-3f75-4f45-b6ad-903dec5062f9',
                'name': 'Tableau Samples',
                'description': 'A set of sample workbooks provided by Tableau Software.',
                'createdAt': '2018-10-11T06:16:40Z',
                'updatedAt': '2019-05-29T03:38:54Z',
                'contentPermissions': 'ManagedByOwner'
            },
            'owner': {
                'id': '12baf4c5-4009-4d60-899e-5f1997941c40'
            }
        }
    ]

    # Test root tag
    assert(actual.tag) == '{http://tableau.com/api}projects'

    # Test first child element
    assert(actual[0].tag) == expected[0]['tag']
    assert(actual[0].attrib) == expected[0]['attrib']
    assert(actual[0][0].tag) == '{http://tableau.com/api}owner'
    assert(actual[0][0].attrib['id']) == expected[0]['owner']['id']

    # Test Second child element
    assert(actual[1].tag) == expected[1]['tag']
    assert(actual[1].attrib) == expected[1]['attrib']
    assert(actual[1][0].tag) == '{http://tableau.com/api}owner'
    assert(actual[1][0].attrib['id']) == expected[1]['owner']['id']

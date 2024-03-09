'''
    Main file of the project to execute and convert all projects from the xml into csv with
    their nested project path.
'''

import convertor

def main():
    '''
        Top level main function to convert the projects.
    '''
    projects_xml_tags = convertor.extract_projects_from_xml('assets/projects.xml')
    print(len(projects_xml_tags))
    projects_dict = convertor.map_project_tags_to_dict(projects_xml_tags)
    print(len(projects_dict))
    projects_structure_tree = convertor.create_project_tree_nodes_list(projects_dict)
    print(len(projects_structure_tree))

    for project in projects_structure_tree.values():
        print(project)

if __name__ == '__main__':
    main()

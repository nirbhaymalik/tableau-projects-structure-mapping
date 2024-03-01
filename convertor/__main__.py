pc = __import__('projects-convertor')

projects_xml_tags = pc.extract_projects_from_xml()
projects_dict = pc.map_project_tags_to_dict(projects_xml_tags)
projects_structure_tree = pc.create_project_tree_nodes_list(projects_dict)

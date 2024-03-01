pc = __import__('projects_convertor')

projects_xml_tags = pc.extract_projects_from_xml()
print(len(projects_xml_tags))
projects_dict = pc.map_project_tags_to_dict(projects_xml_tags)
print(len(projects_dict))
projects_structure_tree = pc.create_project_tree_nodes_list(projects_dict)
print(len(projects_structure_tree))

for i in projects_structure_tree:
    print(projects_structure_tree[i].__str__())

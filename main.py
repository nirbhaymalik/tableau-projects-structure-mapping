"""
    Main file of the project to execute and convert all projects from the xml into csv with
    their nested project path.
"""

import pandas as pd

import convertor


def main():
    """
    Top level main function to convert the projects.
    """
    projects_xml_tags = convertor.extract_projects_from_xml("assets/projects.xml")
    projects_dict = convertor.map_project_tags_to_dict(projects_xml_tags)
    projects_structure_tree = convertor.create_project_tree_nodes_list(projects_dict)

    rows = [
        [project.get_name(), project.get_path_str()]
        for project in projects_structure_tree.values()
    ]

    cols = ["Name", "Path"]
    df = pd.DataFrame(rows, columns=cols)

    # Writing dataframe to csv
    df.to_csv("assets/output.csv", index=False)


if __name__ == "__main__":
    main()

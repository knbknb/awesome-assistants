#!/usr/bin/env python3
# Work in progress
# - does not really classify any assistants,
# - everything ends up as 'Uncategorized' yet
import yaml

def join_yaml_files(file1_path, file2_path, output_file_path):
    # Read and parse the first YAML file
    with open(file1_path, 'r', encoding='utf-8') as file:
        data1 = yaml.safe_load(file)

    # Read and parse the second YAML file
    with open(file2_path, 'r', encoding='utf-8') as file:
        data2 = yaml.unsafe_load(file)

    # Create a mapping from the second file
    role_mapping = {item['id']: item.get('role', 'Uncategorized') for item in data2}

    # Extend the objects in the first file with 'role' from the mapping
    for item in data1:
        item_id = item.get('id')
        if item_id in role_mapping:
            item['role'] = role_mapping[item_id]
    
    # Sort the list by 'role' alphabetically, then by 'id' alphabetically
    sorted_data = sorted(data1, key=lambda x: (x['role'], x['id']))

    # Save the merged data to a new YAML file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        yaml.dump(sorted_data, file)

# Example usage
file2_path = 'assistants-to-cluster.yml'
file1_path = 'updated_assistants_clusters.yml'
output_file_path = 'assistants_joined.yaml'

join_yaml_files(file1_path, file2_path, output_file_path)

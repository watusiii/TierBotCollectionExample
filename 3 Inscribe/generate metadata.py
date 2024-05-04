import json
import os

def generate_json_files(num_files, folder_name):
    # Ensure the folder exists
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for i in range(1, num_files + 1):
        data = {
            "name": f"Tutorial Sketch #{i:02}",
            "creator": "Blank",
            "description": "This is a sketch.",
            "type": "model/gltf-binary",
            "properties": {
                "license": "MIT-0",
                "collection": "Sketches"
            }
        }
        
        file_name = f"{folder_name}/{i}.json"  # Modified to include 'Ha #' in the filename
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"File created: {file_name}")

# Number of JSON files to create (up to 31) and folder name
generate_json_files(4, "metadata")

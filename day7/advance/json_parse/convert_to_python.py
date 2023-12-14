import json


def load_json_from_file(file_path):
    with open(file_path, 'r') as file:
        json_content = file.read()
        return json.loads(json_content)


if __name__ == "__main__":
    json_file_path = 'data.json'

    # Load JSON data from the file
    data = load_json_from_file(json_file_path)

    # Print the loaded data
    print("Loaded JSON Data:")
    print(data)

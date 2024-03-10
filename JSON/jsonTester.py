import json

# Assuming the JSON file is stored at /path/to/data.json
#json_file_path = '/path/to/data.json'
json_file_path = r'C:\Users\Burudani\Documents\mainPythonFolder_v1\JSON\json_keylist_exprime.json'

def load_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The JSON file was not found.")
        return None

def get_value_for_key(key, data):
    if key in data["creditcards"]:
        return data["values"]["creditcards"]
    elif key in data["shopping"]:
        return data["values"]["shopping"]
    else:
        return "NO CATEGORY"

def main():
    data = load_json_data(json_file_path)
    if data is not None:
        user_key = input("Please enter a key: ")
        message = get_value_for_key(user_key, data)
        print(message)

if __name__ == "__main__":
    main()
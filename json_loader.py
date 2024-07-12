# json_loader.py
import json
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("JSON loaded successfully.")
        return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python json_loader.py <path_to_json>")
        sys.exit(1)
    load_json(sys.argv[1])

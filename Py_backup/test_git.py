import json

def create_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def main():
    # Generate numbers (for example, repeating the number 5, 100 times)
    numbers = [5] * 100
    
    # Create a dictionary with the numbers
    data = {"numbers": numbers}

    # Specify the filename for the JSON file (inside the same code folder)
    filename = "data.json"

    # Create the JSON file
    create_json_file(data, filename)

    print(f"JSON file '{filename}' created successfully.")

if __name__ == "__main__":
    main()

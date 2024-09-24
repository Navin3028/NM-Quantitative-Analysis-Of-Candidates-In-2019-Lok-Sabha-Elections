import os
import json

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return json.loads(data)  # Potential bug: assumes file contains valid JSON
    except FileNotFoundError:
        print("File not found")  # Potential vulnerability: does not specify which file
    except json.JSONDecodeError:
        print("Error decoding JSON")  # This should be logged or handled properly

def divide_numbers(a, b):
    return a / b  # Potential bug: division by zero if b is 0

def get_env_variable(var_name):
    return os.environ[var_name]  # Potential vulnerability: could raise KeyError if variable does not exist

def main():
    # Vulnerability: using eval can execute arbitrary code
    user_input = "os.system('ls')"  # Example of dangerous input
    eval(user_input)

    file_path = "data.json"
    data = read_file(file_path)
    
    if data:
        print(data)
    
    # Bug: This might result in a division by zero error
    result = divide_numbers(10, 0)
    print(f"Result: {result}")

    # Vulnerability: accessing environment variable without checks
    api_key = get_env_variable('API_KEY')
    print(f"API Key: {api_key}")

if __name__ == "__main__":
    main()

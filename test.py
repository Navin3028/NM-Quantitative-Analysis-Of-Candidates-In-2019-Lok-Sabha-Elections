import os
import json

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return json.loads(data)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON")
    return None  # Ensure a return even on error

def divide_numbers(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None  # Avoid division by zero
    return a / b

def get_env_variable(var_name):
    value = os.environ.get(var_name)  # Safely get environment variable
    if value is None:
        print(f"Warning: Environment variable {var_name} is not set.")
    return value

def main():
    # Avoid using eval for security reasons
    user_input = "ls"  # Example of a command, but we should not execute it
    print(f"Simulated command: {user_input}")

    file_path = "data.json"
    data = read_file(file_path)
    
    if data is not None:
        print(data)
    
    result = divide_numbers(10, 2)  # Changed to avoid division by zero
    if result is not None:
        print(f"Result: {result}")

    api_key = get_env_variable('API_KEY')
    if api_key:
        print(f"API Key: {api_key}")

if __name__ == "__main__":
    main()

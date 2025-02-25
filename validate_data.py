import json
import os

# Define input folder
input_folder = "data"

# List all JSONL files in the input folder
jsonl_files = [f for f in os.listdir(input_folder) if f.endswith(".jsonl")]

# Function to validate a message structure
def is_valid_message(message):
    if not isinstance(message, dict):
        print(f"❌ Invalid message format (not a dict): {message}")
        return False
    if "role" not in message or "content" not in message:
        print(f"❌ Missing 'role' or 'content' in message: {message}")
        return False
    return True

# Function to validate each file
def validate_jsonl_file(file_path):
    valid = True
    with open(file_path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            try:
                data = json.loads(line)

                # Ensure 'messages' key exists and is a list
                if "messages" not in data or not isinstance(data["messages"], list):
                    print(f"❌ ERROR in {file_path}, Line {line_number}: Missing or invalid 'messages' list")
                    valid = False
                    continue

                # Check if 'messages' contain at least user and assistant roles
                roles = {"user": False, "assistant": False, "system": False}
                
                for msg in data["messages"]:
                    if is_valid_message(msg):
                        role = msg["role"]
                        if role in roles:
                            roles[role] = True
                    else:
                        valid = False  # Mark file as invalid

                # Ensure at least user and assistant roles exist
                if not (roles["user"] and roles["assistant"]):
                    print(f"❌ ERROR in {file_path}, Line {line_number}: Missing required roles (user and assistant)")
                    valid = False

            except json.JSONDecodeError as e:
                print(f"❌ ERROR in {file_path}, Line {line_number}: JSON Decode Error - {e}")
                valid = False
    
    if valid:
        print(f"✅ {file_path} is valid!")
    return valid

# Validate all JSONL files
for filename in jsonl_files:
    file_path = os.path.join(input_folder, filename)
    print(f"\n🔍 Validating: {file_path}")
    validate_jsonl_file(file_path)

print("\n✅ Validation completed.")

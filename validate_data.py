import json
import os
input_folder = "data"
jsonl_files = [f for f in os.listdir(input_folder) if f.endswith(".jsonl")]
def is_valid_message(message):
    return isinstance(message, dict) and "role" in message and "content" in message
def validate_jsonl_file(file_path):
    valid = True
    with open(file_path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            try:
                data = json.loads(line)
                if "messages" not in data or not isinstance(data["messages"], list):
                    print(f"❌ ERROR in {file_path}, Line {line_number}: Missing or invalid 'messages' list")
                    valid = False
                    continue
                roles = {"user": False, "assistant": False, "system": False}
                
                for msg in data["messages"]:
                    if is_valid_message(msg):
                        role = msg["role"]
                        if role in roles:
                            roles[role] = True
                    else:
                        print(f"❌ ERROR in {file_path}, Line {line_number}: Invalid message structure - {msg}")
                        valid = False

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
    validate_jsonl_file(file_path)

print("Validation completed.")

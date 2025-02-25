import json

# Define the file path
file_path = "output_data/mix.jsonl"

# Function to validate message format
def validate_messages(messages, line_number):
    if not isinstance(messages, list):
        print(f"❌ ERROR (Line {line_number}): 'messages' is not a list!")
        return False

    roles = {"user": False, "assistant": False, "system": False}

    for msg in messages:
        if not isinstance(msg, dict):
            print(f"❌ ERROR (Line {line_number}): Invalid message format (not a dict) - {msg}")
            return False
        if "role" not in msg or "content" not in msg:
            print(f"❌ ERROR (Line {line_number}): Missing 'role' or 'content' in - {msg}")
            return False
        
        if msg["role"] in roles:
            roles[msg["role"]] = True

    if not (roles["user"] and roles["assistant"]):
        print(f"❌ ERROR (Line {line_number}): Missing 'user' or 'assistant' role!")
        return False

    if not roles["system"]:
        print(f"⚠ WARNING (Line {line_number}): Missing 'system' role (optional)")

    return True

# Validate each line in mix.jsonl
with open(file_path, "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        try:
            data = json.loads(line)
            if "messages" not in data:
                print(f"❌ ERROR (Line {line_number}): Missing 'messages' key!")
                continue
            validate_messages(data["messages"], line_number)
        except json.JSONDecodeError as e:
            print(f"❌ ERROR (Line {line_number}): JSON Decode Error - {e}")

print("\n✅ Validation completed.")

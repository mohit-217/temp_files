import json
import os

# Define input and output directories
input_folder = "data"
output_folder = "cleaned_data"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# List all JSONL files in the input folder
jsonl_files = [f for f in os.listdir(input_folder) if f.endswith(".jsonl")]

# Process each file
for filename in jsonl_files:
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)  # Save with the same name

    with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            data = json.loads(line)  # Parse JSON line
            if "messages" in data:  # Keep only 'messages' column
                filtered_data = {"messages": data["messages"]}
                outfile.write(json.dumps(filtered_data) + "\n")

    print(f"Processed: {filename} → Saved to {output_path}")

print("✅ All files processed successfully!")

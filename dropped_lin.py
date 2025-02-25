def drop_line(jsonl_file, line_number, dropped_file):
    try:
        # Read all lines
        with open(jsonl_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        # Ensure the line number is valid
        if line_number < 1 or line_number > len(lines):
            print(f"Error: Line number {line_number} is out of range.")
            return
        
        # Extract the dropped line
        dropped_line = lines[line_number - 1]

        # Write the dropped line to a separate file (append mode)
        with open(dropped_file, "a", encoding="utf-8") as dropfile:
            dropfile.write(dropped_line)

        # Write back the remaining lines to the original file
        with open(jsonl_file, "w", encoding="utf-8") as outfile:
            for i, line in enumerate(lines):
                if i != line_number - 1:  # Skip the dropped line
                    outfile.write(line)

        print(f"Line {line_number} removed and saved in {dropped_file}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
jsonl_file = "dolphin-r1-flash-reasoning_90.jsonl"  # Path to your JSONL file
line_number = 1001  # Line number to remove
dropped_file = "dropped_sample.jsonl"  # File to store dropped records

drop_line(jsonl_file, line_number, dropped_file)

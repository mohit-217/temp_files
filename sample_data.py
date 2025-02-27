input_file = "data/mix.jsonl"  # Replace with your file name
output_file = "sampled_1000.jsonl"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile):
        if i >= 1000:  #: Stop after 1000 lines
            break
        outfile.write(line)

print(f"Extracted 1000 samples to {output_file}")
import os
import json
from datasets import load_dataset

# Create directory if it doesn't exist
save_dir = "./local_datasets"
os.makedirs(save_dir, exist_ok=True)

# Choose dataset and config
dataset_name = "cognitivecomputations/dolphin-r1"
config_name = "nonreasoning"  # Change to 'reasoning-deepseek' or 'reasoning-flash' if needed

# Load dataset with specific config
dataset = load_dataset(dataset_name, config_name)

# Save each split as a JSON file
for split in dataset.keys():  # Usually ['train', 'test', 'validation']
    file_path = os.path.join(save_dir, f"dolphin-r1-{config_name}-{split}.json")

    # Convert dataset to list of dictionaries
    data_list = dataset[split].to_list()

    # Write to JSON file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    print(f"✅ Saved {split} split to {file_path}")

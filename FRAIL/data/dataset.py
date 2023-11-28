from torch.utils.data import Dataset, DataLoader
import config

# Define a dummy dataset class
class CustomDataset(Dataset):
    def __init__(self, file_path):
        # Load your data from the file, assuming each line is a sample
        with open(file_path, "r") as file:
            self.data = [line.strip() for line in file.readlines()]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# File path to your training dataset
train_file_path = "train.idx"

# Create a custom dataset instance
dataset = CustomDataset(train_file_path)

# Create a DataLoader
dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)

for batch_idx, batch in enumerate(dataloader):
    # Print the batch number and its content
    print(f"Batch {batch_idx + 1}: {batch}")

    # Uncomment the following line to print individual samples in the batch
    # print(f"Batch {batch_idx + 1} samples: {batch}")

    # Stop after printing a few batches (e.g., 5)
    if batch_idx == 4:
        break
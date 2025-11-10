import kagglehub

# Download latest version
path = kagglehub.dataset_download("mlbysoham/adult-dataset")

print("Path to dataset files:", path)
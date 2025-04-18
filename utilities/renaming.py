import os
image = True
prefix = "AUG"
folder_path = "/home/jovyan/nnU-Net/nnUNet_raw/Dataset500_augmented/imagesTr"

for filename in os.listdir(folder_path):
    parts = filename.split("_")
    numeric_part = None
    for part in parts:
        if part.isnumeric(): 
            numeric_part = part

    type = ".nrrd"
    if filename.endswith(".nii.gz"):
        type = ".nii.gz"
        continue  
    new_name = f"{prefix}_{numeric_part}"

    if image:
        new_name += "_0000"+type
    else:
        new_name += type

    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)

    if os.path.exists(new_path):
        print(f"File {new_name} already exists, skipping renaming.")
    else:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

print("Renaming completed!")

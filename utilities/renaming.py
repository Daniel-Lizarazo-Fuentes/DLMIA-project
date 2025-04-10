import os
image = False
folder_path = "nnUNet_raw/Dataset200_diseased/labelsTr"

for filename in os.listdir(folder_path):
    parts = filename.split("_")
    secondary = parts[1].split(".")
    secondary[0] = "0"+secondary[0] if int(secondary[0])>9 else str("00"+secondary[0])
    new_name = f"{parts[0].upper()}_{secondary[0]}"
    new_name = f"{new_name}_0000.{secondary[1]}" if image else f"{new_name}.{secondary[1]}"

    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)

    if os.path.exists(new_path):
        print(f"File {new_name} already exists, skipping renaming.")
    else:
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

print("Renaming completed!")

import os
import SimpleITK as sitk

input_folder = "/home/jovyan/nnU-Net/nnUNet_raw/Dataset500_augmented/imagesTs"  
output_folder = "/home/jovyan/nnU-Net/nnUNet_raw/Dataset500_augmented/imagesTs"  

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".nrrd"):
        input_path = os.path.join(input_folder, filename)
        image = sitk.ReadImage(input_path)

        output_filename = os.path.splitext(filename)[0] + ".nii.gz"
        output_path = os.path.join(output_folder, output_filename)
        sitk.WriteImage(image, output_path)

        print(f"Converted: {filename} -> {output_filename}")
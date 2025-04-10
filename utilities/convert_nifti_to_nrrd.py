import os
import nibabel as nib
import nrrd
import time

def convert_nifti_to_nrrd(nifti_path, nrrd_path):
    print(f"Processing: {nifti_path}")
    start_time = time.time()

    # Load NIfTI file
    nifti_img = nib.load(nifti_path)
    nifti_data = nifti_img.get_fdata()

    # Extract affine transformation for spatial metadata
    affine = nifti_img.affine
    header = {
        'space': 'left-posterior-superior',
        'space directions': affine[:3, :3].tolist(),
        'space origin': affine[:3, 3].tolist(),
    }

    # Save as NRRD (uncompressed for speed)
    nrrd.write(nrrd_path, nifti_data, header, compression_level=0)
    print(f"✅ Saved: {nrrd_path} ({time.time() - start_time:.2f}s)")

def batch_convert_nifti_to_nrrd(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    nifti_files = [f for f in os.listdir(input_folder) if f.endswith('.nii.gz')]
    print(f"Found {len(nifti_files)} files to convert...")

    for nifti_file in nifti_files:
        nifti_path = os.path.join(input_folder, nifti_file)
        nrrd_filename = nifti_file.replace('.nii.gz', '.nrrd')
        nrrd_path = os.path.join(output_folder, nrrd_filename)

        convert_nifti_to_nrrd(nifti_path, nrrd_path)

if __name__ == "__main__":
    input_folder = "/home/jovyan/nnUNet_raw/Dataset400_supersecret/imagesTs"  
    output_folder = "/home/jovyan/nnUNet_raw/Dataset300_combined/imagesTs"  
    batch_convert_nifti_to_nrrd(input_folder, output_folder)

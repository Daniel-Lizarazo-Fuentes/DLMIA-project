# Add paths
./paths.sh

# Preprocessing
.local/bin/nnUNetv2_plan_and_preprocess -d 100 --verify_dataset_integrity -np 1 

# Training
CUDA_VISIBLE_DEVICES=0 .local/bin/nnUNetv2_train 100 2d 0 & # train on GPU 0
CUDA_VISIBLE_DEVICES=1 .local/bin/nnUNetv2_train 100 2d 1 & # train on GPU 1
CUDA_VISIBLE_DEVICES=2 .local/bin/nnUNetv2_train 100 2d 2 & # train on GPU 2
CUDA_VISIBLE_DEVICES=3 .local/bin/nnUNetv2_train 100 2d 3 & # train on GPU 3
CUDA_VISIBLE_DEVICES=4 .local/bin/nnUNetv2_train 100 2d 4 & # train on GPU 4
wait

# Needs testing
torchrun TORCH_SHARING_STRATEGY=file_system CUDA_VISIBLE_DEVICES=0 nnUNetv2_train 100 2d 0
.local/bin/nnUNetv2_find_best_configuration 100 -c [2d,3d_fullres,3d_lowres] --disable_ensembling -device cuda
# CUDA_VISIBLE_DEVICES=5 .local/bin/nnUNetv2_train 100 3d_fullres 0 [--npz] & # train on GPU 5
# CUDA_VISIBLE_DEVICES=6 .local/bin/nnUNetv2_train 100 3d_fullres 1 [--npz] & # train on GPU 6
# CUDA_VISIBLE_DEVICES=7 .local/bin/nnUNetv2_train 100 3d_fullres 2 [--npz] & # train on GPU 7


# CUDA_VISIBLE_DEVICES=0 .local/bin/nnUNetv2_train 100 3d_fullres 3 [--npz] & # train on GPU 0
# CUDA_VISIBLE_DEVICES=1 .local/bin/nnUNetv2_train 100 3d_fullres 4 [--npz] & # train on GPU 1
# CUDA_VISIBLE_DEVICES=2 .local/bin/nnUNetv2_train 100 3d_lowres 0 [--npz] & # train on GPU 2
# CUDA_VISIBLE_DEVICES=3 .local/bin/nnUNetv2_train 100 3d_lowres 1 [--npz] & # train on GPU 3
# CUDA_VISIBLE_DEVICES=4 .local/bin/nnUNetv2_train 100 3d_lowres 2 [--npz] & # train on GPU 4
# CUDA_VISIBLE_DEVICES=5 .local/bin/nnUNetv2_train 100 3d_lowres 3 [--npz] & # train on GPU 5
# CUDA_VISIBLE_DEVICES=6 .local/bin/nnUNetv2_train 100 3d_lowres 4 [--npz] & # train on GPU 6
# CUDA_VISIBLE_DEVICES=7 .local/bin/nnUNetv2_train 100  [--npz] & # train on GPU 7
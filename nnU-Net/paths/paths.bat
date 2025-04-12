@echo off
setx nnUNet_raw "%CD%\nnUNet_raw" 
setx nnUNet_preprocessed "%CD%\nnUNet_preprocessed" 
setx nnUNet_results "%CD%\nnUNet_results" 
echo Environment variables set to the current folder.
pause
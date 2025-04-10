# Introduction
# Setup Python and jupyter 
This section will help you run our project and reproduce our results.

## Local
Running locally can either be done from a global python envirnement or a virtual envirnement. The latter is recomended. 

### Command line
Select a kernel (requires Python and Jupyter to be installed): <br>
```jupyter kernelspec list```
```jupyter console --kernel <kernel_name>```
```jupyter notebook```
This will boot up a jupyter notebook webserver.
### GUI
This process can also be done through the vscode (or similar) GUI. 

### Creating venv
```python -m venv <venv_name>``` <br>
```source <venv_name>/bin/activate```

## jupyter.utwente node
For computational tasks that require a bit more than what you have locally (or you want to still be able to do other stuff) you can use the <a href="https://jupyter.utwente.nl/">Jupyter Utwente</a> nodes. Keep in mind that you need to either be on the uni network or should use the eduvpn. 

Next you need to generate a token which you can get from the hub control panel:<br>
<a href="https://jupyter.utwente.nl/hub/token">Get your token</a> 

Now you can pick to either connect the python kernel through the GUI or command line:
```URL=https://jupyter.utwente.nl/user/<your_student_email>@student.utwente.nl/?token=<your_token>```

### Command line
Then tell jupyter to connect to an existing Jupyter Server and enter the following the previously determined URL:<br>
```jupyter notebook --NotebookApp.server_url=<URL>```

### GUI
In vscode install the python/jupyter extensions. Press kernels in the top right (if a .ipynb file is opened). Then press existing Jupyter Server and then enter the url. 

<i style="color: red">If you are running an open source vscode package include ```--enable-proposed-api ms-toolsai.jupyter``` to save a lot of pain (kernels not appearing in GUI etc).</i>

## Additional setup
### nnUNet
nnUnet requires several envirnment variables and for the folders to be in a specific order and naming convention.
First create the 3 required folders (preprocess,raw,results). In the case that you do not have the files in the proper format you can use ```renaming.py``` to turn them into the proper naming convention for images or labels (the CTCA=>images, annotations=>labels: ```NORMAL_1.nrrd -> NORMAL_001_0000.nrrd or NORMAL_001.nrrd if images is false```). Structure will look like the following:

```
- nnUNet_preprocessed
- nnUNet_raw
-- Dataset100_normal
--- imagesTr
---- DISEASED_001_0000.nrrd
---- DISEASED_002_0000.nrrd
---- ...
--- labelsTr
---- DISEASED_001.nrrd
---- DISEASED_002.nrrd
---- ...

-- Dataset200_diseased
--- ...
- nnUNet_results
```

**Linux/Jupyter**
1. Activate shell file: ```chmod +x paths.sh```
2. Execute: ```./paths.sh```,<br> if an error about illegal formats appears you most likely modified the shell file in an windows envirnement (adds different charachter artifacts) which can be fixed with ```sed -i 's/\r$//' paths.sh```

**Windows (local)**
1. Run ```paths.bat``` in the terminal (powershell or cmd, as long as it's administrator)
2. Restart all shells and check if present: ```echo $env:nnUNet_raw``` for example 

#### Processing lables
As the annotations is volume data without labels we need to tell nnUNet what is background and what are the proper points. This is done though a small descripte file ```dataset.json``` which defines channels and provides information to nnUNet about the dataset. 

### Eduvpn
- Linux: [install docs](https://docs.eduvpn.org/client/linux/installation.html)
- Windows: [installation exe](https://app.eduvpn.org/windows/eduVPNClient_latest.exe)
- Mac: [mac store](https://apps.apple.com/app/eduvpn-client/id1317704208)

# Running nnUNet
<bold style="color:red">Very important! Sometimes the hub cannot find the command, use .local/bin/ before any commands to fix this.  This step should not be necessary when running locally. Additionally watch cluster usage to not eat up too many resources: ```watch -n1 nvidia-smi```</bold>

The specifc commands are included (with additional documentation) in runnable notebook file (````pipeline.ipynb```).

In short:
1. Preprocessing
2. Training (2d, 3d low/full, 3d cascade)
3. Inference (2d, 3d low/full, 3d cascade)
4. Ensemble 

# Running Auto3dseg


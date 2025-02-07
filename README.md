# Introduction
# Setup
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

<i>If you are running an open source vscode package include ```--enable-proposed-api ms-toolsai.jupyter``` to save a lot of pain (kernels not appearing in GUI etc).</i>

### Eduvpn
- Linux: [install docs](https://docs.eduvpn.org/client/linux/installation.html)
- Windows: [installation exe](https://app.eduvpn.org/windows/eduVPNClient_latest.exe)
- Mac: [mac store](https://apps.apple.com/app/eduvpn-client/id1317704208)

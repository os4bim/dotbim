# dotbim

🗣️ EN

Trying some scripts to show some selected data from Revit in a 3D web-viewer with dotbim files.

You can follow this steps :
Ces fichiers sont utilisé via pyrevit. Pour les utiliser via RevitPythonShell supprimer ces lignes :
```
__doc__ =
__title__ =
__author__ =
```

### 1/ Extract_data_from_revit.py

Execute this code with RevitPythonShell, you will have three tuple of pipes, ducts and equipment with the desired datas.

### 2/ Import_revit_data_to_dotbim.py

Execute this code in your IDE by copy paste the previous tuples at the beginning of the script.

### 3/ Revit_MEP_data.bim

You obtain a dotbim file ! You can try this sample with

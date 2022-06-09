# dotbim

🗣️ EN

Trying some scripts to show some selected data from Revit in a 3D web-viewer with dotbim files.

You can follow this steps :

### 1/ Extract_data_from_revit.py

Execute this code with RevitPythonShell, you will have three tuple of pipes, ducts and equipment with the desired datas.

### 2/ Import_revit_data_to_dotbim.py

Execute this code in your IDE by copy paste the previous tuples at the beginning of the script.

### 3/ Revit_MEP_data.bim

You obtain a dotbim file ! You can try this sample : just drop it in https://3dviewer.net/
You have a schematic 3D model of your installation that you can easily share to your colleagues !
The green line are the ducts, the blues ones the pipes ans the red pyramids the equipment.
You can click on all this element to check the desired data you extracted from revit !
Enjoy !

![alt text](https://github.com/os4bim/dotbim/blob/main/revit_dotbim.png)

Visit dotbim website : https://dotbim.net/
Visit this topic to see how we could improve some viewers to display data : https://github.com/kovacsv/Online3DViewer/issues/258

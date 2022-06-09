#Extract equipment coordinates v1.0
#Edited by Yoann OBRY


import clr
import System

clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from Autodesk.Revit.DB import * 
from System import Guid
from System.Drawing import Point
from Autodesk.Revit import UI
from System.Collections.Generic import List
from Autodesk.Revit.DB import ElementId


#### Collecte les équipements ####

#Shared parameter code GMAO court
code_gmao_c = Guid(r'4570ee53-6118-4f4e-a65f-94f1d6d728e6')

#Conversion feet -> meters
feet = 3.28084


### Collecte les Air terminals ###
ATs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctTerminal).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_GMAO_ID_AT = ()

for AT in ATs:

	# Code GMAO court - Instance Parameter (Shared Parameter)
	code_gmao_court = AT.get_Parameter(code_gmao_c)
	#print code_gmao_court.AsString()
	
	# Coordonnées
	location = AT.Location.Point
	
	# Element ID - Instance Parameter
	#print PA.Id
	
	tup_GMAO_ID_AT += ((AT.Id.IntegerValue,code_gmao_court.AsString(),"{:01.2f}".format(location.X / feet),"{:01.2f}".format(location.Y / feet),"{:01.2f}".format(location.Z / feet)),)


### Collecte les Duct Accessories ###
DAs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctAccessory).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_GMAO_ID_DA = ()

for DA in DAs:

	# Code GMAO court - Instance Parameter (Shared Parameter)
	code_gmao_court = DA.get_Parameter(code_gmao_c)
	#print code_gmao_court.AsString()
	
	# Coordonnées
	location = DA.Location.Point
	
	# Element ID - Instance Parameter
	#print PA.Id
	
	tup_GMAO_ID_DA += ((DA.Id.IntegerValue,code_gmao_court.AsString(),"{:01.2f}".format(location.X / feet),"{:01.2f}".format(location.Y / feet),"{:01.2f}".format(location.Z / feet)),)


### Collecte les Mechanical Equipment ###
MEs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MechanicalEquipment).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_GMAO_ID_ME = ()

for ME in MEs:

	# Code GMAO court - Instance Parameter (Shared Parameter)
	code_gmao_court = ME.get_Parameter(code_gmao_c)
	#print code_gmao_court.AsString()

	# Coordonnées
	location = ME.Location.Point
	
	# Element ID - Instance Parameter
	#print PA.Id
	
	tup_GMAO_ID_ME += ((ME.Id.IntegerValue,code_gmao_court.AsString(),"{:01.2f}".format(location.X / feet),"{:01.2f}".format(location.Y / feet),"{:01.2f}".format(location.Z / feet)),)


### Collecte les Pipe Accessories ###
PAs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeAccessory).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_GMAO_ID_PA = ()

for PA in PAs:

	# Code GMAO court - Instance Parameter (Shared Parameter)
	code_gmao_court = PA.get_Parameter(code_gmao_c)
	#print code_gmao_court.AsString()
	
	# Coordonnées
	location = PA.Location.Point
	
	# Element ID - Instance Parameter
	#print PA.Id
	
	tup_GMAO_ID_PA += ((PA.Id.IntegerValue,code_gmao_court.AsString(),"{:01.2f}".format(location.X / feet),"{:01.2f}".format(location.Y / feet),"{:01.2f}".format(location.Z / feet)),)
	
	
### Collecte les Plumbing fixtures ###
PFs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PlumbingFixtures).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_GMAO_ID_PF = ()

for PF in PFs:

	# Code GMAO court - Instance Parameter (Shared Parameter)
	code_gmao_court = PF.get_Parameter(code_gmao_c)
	#print code_gmao_court.AsString()

	# Coordonnées
	location = PF.Location.Point
	
	# Element ID - Instance Parameter
	#print PA.Id
	
	tup_GMAO_ID_PF += ((PF.Id.IntegerValue,code_gmao_court.AsString(),"{:01.2f}".format(location.X / feet),"{:01.2f}".format(location.Y / feet),"{:01.2f}".format(location.Z / feet)),)
	
	
### Collecte les Electrical Equipment ###
EEs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_ElectricalEquipment).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_GMAO_ID_EE = ()

for EE in EEs:

	# Code GMAO court - Instance Parameter (Shared Parameter)
	code_gmao_court = EE.get_Parameter(code_gmao_c)
	#print code_gmao_court.AsString()

	# Coordonnées
	location = EE.Location.Point
	
	# Element ID - Instance Parameter
	#print PA.Id
	
	tup_GMAO_ID_EE += ((EE.Id.IntegerValue,code_gmao_court.AsString(),"{:01.2f}".format(location.X / feet),"{:01.2f}".format(location.Y / feet),"{:01.2f}".format(location.Z / feet)),)
	

tup_GMAO_ID = tup_GMAO_ID_AT + tup_GMAO_ID_DA + tup_GMAO_ID_ME + tup_GMAO_ID_PA + tup_GMAO_ID_PF + tup_GMAO_ID_EE


print('tup_equip = ' + str(tup_GMAO_ID))


#### Collecte les ducts segment ####
			
#Collecte les Duct
DTs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_DuctCurves).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_duct = ()

for DT in DTs:
	
	# Coordonnées du segment de duct
	pt1 = DT.Location.Curve.GetEndPoint(0)
	pt2 = DT.Location.Curve.GetEndPoint(1)

	tup_duct += ((DT.Id.IntegerValue,"{:01.2f}".format(pt1.X / feet),"{:01.2f}".format(pt1.Y / feet),"{:01.2f}".format(pt1.Z / feet),"{:01.2f}".format(pt2.X / feet),"{:01.2f}".format(pt2.Y / feet),"{:01.2f}".format(pt2.Z / feet)),)

print('tup_duct = ' + str(tup_duct))



#### Collecte les pipes segment ####
			
#Collecte les Pipes
PIs = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_PipeCurves).WhereElementIsNotElementType().ToElements()

#Créer un tuple vide
tup_pipe = ()

for PI in PIs:
	
	# Coordonnées du segment de pipe
	pt1 = PI.Location.Curve.GetEndPoint(0)
	pt2 = PI.Location.Curve.GetEndPoint(1)

	tup_pipe += ((PI.Id.IntegerValue,"{:01.2f}".format(pt1.X / feet),"{:01.2f}".format(pt1.Y / feet),"{:01.2f}".format(pt1.Z / feet),"{:01.2f}".format(pt2.X / feet),"{:01.2f}".format(pt2.Y / feet),"{:01.2f}".format(pt2.Z / feet)),)


print('tup_pipe = ' + str(tup_pipe))

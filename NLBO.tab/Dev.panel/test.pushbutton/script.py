__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

import re
import pyrevit
from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, \
    ElementParameterFilter, BuiltInCategory, BuiltInParameter
import clr
from pyrevit import forms, revit, DB, script, UI
project_client_id = 1
object_code = "23.17.11.00"
clr.AddReference('RevitAPI')
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
collector = FilteredElementCollector(doc)
elements = collector.WhereElementIsNotElementType().ToElementIds()
selection = [doc.GetElement(x) for x in elements]
table = [[]]
for element in selection:
    t = str(element.GetType())
    if re.match("^Autodesk.Revit.DB.FamilyInstance$", t):
        p = element.Symbol
        if object_code == p.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString():
            omniclass_number = p.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString()
            # ProductURL = p.LookupParameter('ProductURL').AsString()
            # Material = p.LookupParameter('Material')
            Thickness1 = p.GetParameters('Material')[0].AsDouble()
            Thickness2 = p.get_Parameter(BuiltInParameter.FAMILY_THICKNESS_PARAM).AsDouble()
            Thickness3 = p.LookupParameter('Material').AsDouble()
            print(Thickness1,Thickness2,Thickness3)










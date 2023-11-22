__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

import re

import pyrevit
from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, ElementParameterFilter,BuiltInCategory, BuiltInParameter
import clr
from pyrevit import forms,revit,DB
from omniclass import *
omniclass.filter_by_level(2)
items = omniclass.name_level
name_code = omniclass.code_level
# with open("omniclass.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     if re.match("([\d]{2}\.[\d]{2}\.[\d]{2}\.00)\t",line):
#         for ifc_product_name in re.findall("\t(.*?)\t", line):
#             items.append(ifc_product_name)
select_item = forms.SelectFromList.show(items, button_name='Select object', title='Please select object')
index_selected = items.index(select_item)
object_code = name_code[index_selected]

# Create a message box
message_box = forms.alert(
    object_code,
    title="ifc_code",
    warn_icon = False
)
clr.AddReference('RevitAPI')
doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
collector = FilteredElementCollector(doc)
elements = collector.WhereElementIsNotElementType().ToElementIds()
selection = [doc.GetElement(x) for x in elements]
x = 0
table = [[0,0,0]]
for element in selection:
   t = str(element.GetType())
   if re.match("^Autodesk.Revit.DB.FamilyInstance$",t):
      p = element.Symbol
      if object_code == p.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString():
        c = p.LookupParameter('ProductURL').AsString()
        m = p.LookupParameter('ModelLabel').AsString()
        for d in table:
            if d[0] == m :
                d[1] = d[1]+1
            else:
                table.append([m, 0, c])

output = pyrevit.output.get_output()
output.add_style('body { color: blue; }')
output.print_table(
table_data=table,
title="Object_Data",
columns=["Model_Label", "Count", "PoductUrl"],
formats=['', '', ''],
last_line_style='color:red;'
)
























# # Show the message box
# message_box.open()


# import clr
# clr.AddReference('System.windows.Forms')
# clr.AddReference('IronPython.Wpf')
#
# #find the path of ui.xaml
# from pyrevit import script
# xamlfile = script.get_bundle_file('ui.xaml')
#
# #import wpf creator and base window
# import wpf
# from System import Windows
#
# class MyWindow(Windows.Window):
#     def __init__(self):
#         wpf.LoadComponent(self, xamlfile)
#
# # let's show the windows
# MyWindow().ShowDialog()


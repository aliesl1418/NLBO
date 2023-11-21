__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

import re
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
for element in selection:
   t = str(element.GetType())
   if re.match("^Autodesk.Revit.DB.FamilyInstance$",t):
      p = element.Symbol
      if object_code == p.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString():
        c = p.LookupParameter('ProductURL').AsString()
        print(c)
        x = x + 1
print(x)




      # if element.Symbol:
      #  T = element.Symbol
      #  if object_code == T.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString():
      #     p = T.LookupParameter('ProductURL').AsString()
      #     print(p)






















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


__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

# import pyrevit
# from pyrevit import *
# from pyrevit import output

# #first_try
# from pyrevit import revit,DB
# from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, ElementParameterFilter,BuiltInCategory, BuiltInParameter
# import clr
# clr.AddReference('RevitAPI')
# doc = __revit__.ActiveUIDocument.Document
# uidoc = __revit__.ActiveUIDocument
# collector = FilteredElementCollector(doc)
# elements = collector.OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElementIds()
#
# selection = [doc.GetElement(x) for x in elements]
# for element in selection:
#    T = element.GetType()
#    print(T)
#

   # T = element.Symbol
   # print(T)
   # P = T.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString()
   # print(P)




#  # param = element.LookupParameter('Unconnected Height')
#  # print(param)
#  print(list(element.Parameters))
# for p in element.Parameters:
#  print(p.Definition.Name)






# #second try
# from pyrevit import revit,DB
# from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, ElementParameterFilter,BuiltInCategory,BuiltInParameter
# import clr
# clr.AddReference('RevitAPI')
# doc = __revit__.ActiveUIDocument.Document
# collector = FilteredElementCollector(doc)
# elements = collector.OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElementIds()
#
# selection = [doc.GetElement(x) for x in elements]
# for element in selection:
#  param = element.get_Parameter(BuiltInParameter.WALL_BASE_CONSTRAINT).AsValueString()
#  print(param)

# #third try
# import System
# from pyrevit import revit,DB
# from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, ElementParameterFilter,BuiltInCategory,BuiltInParameter
# import clr
# clr.AddReference('RevitAPI')
# doc = __revit__.ActiveUIDocument.Document
# collector = FilteredElementCollector(doc)
# elements = collector.OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElementIds()
#
# selection = [doc.GetElement(x) for x in elements]
# guid_str = 'afec3538-445f-49e7-b8cd-2e852da79350'
# guid = System.Guid(guid_str)
# for element in selection:
#  param = element.get_Parameter(guid).AsValueString()
#  print(param)


# data = [
# ['row1', 'data', 'data', 80 ],
# ['row2', 'data', 'data', 45 ],
# ]
# output = pyrevit.output.get_output()
# output.add_style('body { color: blue; }')
# output.print_table(
# table_data=data,
# title="Object_Data",
# columns=["Object Name", "Count", "PoductUrl"],
# formats=['', '', ''],
# last_line_style='color:red;'
# )
mlist = [1,2,3]
m = 2
if not m in mlist:
 mlist.append(2)
print(mlist)
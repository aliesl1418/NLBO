__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""


# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, UnitUtils, DisplayUnitType
# doc = __revit__.ActiveUIDocument.Document
# # Define the omniclass code
# omniclass_code = "23-25 39 11"
#
# # Get all elements with the specified omniclass code
# collector = FilteredElementCollector(doc).WhereElementIsNotElementType()
# elements = [elem for elem in collector if elem.GetEntitySchemaGuids().Contains(omniclass_code)]
#
# # Print the elements with the specified omniclass code
# for elem in elements:
#     print(elem.Name)
#     # Get all parameters of the element
#     parameters = elem.Parameters
#     for param in parameters:
#         # Get parameter name and value
#         param_name = param.Definition.Name
#         param_value = param.AsValueString()
#         print(param_name, param_value)


from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ViewSchedule
#
# doc = __revit__.ActiveUIDocument.Document
#
# def all_elements_of_category(category):
# 	return FilteredElementCollector(doc).OfCategory(category).WhereElementIsNotElementType().ToElements()
#
# #All Elements Of Walls Category.
# walls = all_elements_of_category(BuiltInCategory.OST_Walls)
#
# #All Elements Of Doors Category.
# doors = all_elements_of_category(BuiltInCategory.OST_Doors)

# import clr
#
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, UnitType, DisplayUnitType, UnitUtils
# doc = __revit__.ActiveUIDocument.Document
# # Assume doc is the Revit document object
# # Assume omniClassCode is the OmniClass code you want to search for
#
# # Get all elements in the model
# collector = FilteredElementCollector(doc)
# elements = collector.WhereElementIsNotElementType().ToElements()
#
# # Loop through each element and check if it has the OmniClass code
# for element in elements:
#     # Assume omniClassParam is the parameter storing the OmniClass code in the Revit model
#     omniClassParam = element.get_Parameter(BuiltInParameter.OMNICLASS_CODE)
#     print(omniClassParam)
    # if omniClassParam and omniClassParam.AsString() == omniClassCode:
    #     # Extract information about the object
    #     name = element.Name
    #     category = element.Category.Name
    #     # Add more properties as needed
    #
    #     # Print or store the information as needed
#     #     print(f"Object Name: {name}, Category: {category}")


# import clr
#
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, UnitType, DisplayUnitType, UnitUtils, Parameter, Element,ParameterElement
# doc = __revit__.ActiveUIDocument.Document
#
#
# collector = FilteredElementCollector(doc)
# elements = collector.OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()
# #print(elements)
# for element in elements:
#     omniClassParam = element.get_Parameter(BuiltInParameter.DOOR_HEIGHT).AsValueString()
#     print(omniClassParam)

# import clr
#
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, ParameterType, Element,ParameterElement
# doc = __revit__.ActiveUIDocument.Document
#
# # Define the OmniClass number
# omniClassNumber = "23.30.10.00"
#
# # Collect all elements in the model
# collector = FilteredElementCollector(doc).WhereElementIsNotElementType().ToElements()
#
# # Iterate over the elements
# for element in collector:
#     # Get the OmniClass number parameter
#     omniClassParam = element.LookupParameter('OmniClass Number')
#
#     if omniClassParam:
#         # Check if the OmniClass number matches
#         if omniClassParam.AsString() == omniClassNumber:
#             # Print the element ID and all its parameters
#             print("Element ID: ", element.Id)
#             params = element.Parameters
#             for param in params:
#                 # Check if the parameter has a value
#                 if param.HasValue:
#                     # Print the parameter name and value
#                     print(param.Definition.Name)
#                     print(param.AsValueString())




# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import *
# revit_doc = __revit__.ActiveUIDocument.Document
# omniclass_code = "23.30.10.00"
# # Collect all elements in the Revit document
# elements = FilteredElementCollector(revit_doc).OfClass(FamilyInstance).WhereElementIsNotElementType().ToElements()
#
# # Filter elements by OmniClass code
# elements_with_omniclass = [elem for elem in elements if elem.get_Parameter(BuiltInParameter.OMNICLASS_CODE) == omniclass_code]
#
# print(list(elements_with_omniclass))

# import clr
# clr.AddReference('RevitAPI')
# from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, ElementParameterFilter
# revit_doc = __revit__.ActiveUIDocument.Document
#
# # Get the shared parameter
# shared_param = [param.Definition for param in revit_doc.ParameterBindings if param.Definition.Name == 'OmniClass Number'][0]
# # Create a filter for the OmniClass code
# value_provider = ParameterValueProvider(shared_param.Id)
# filter_rule = FilterStringEquals(value_provider, '23.30.10.00')
# param_filter = ElementParameterFilter(filter_rule)
#
# # Collect all elements in the Revit document that match the filter
# elements = FilteredElementCollector(revit_doc).WherePasses(param_filter).ToElements()
#
# print(elements)





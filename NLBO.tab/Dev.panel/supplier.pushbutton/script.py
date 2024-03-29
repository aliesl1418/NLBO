__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

# -*- coding: utf-8 -*-
import os
import webbrowser
import csv
import re
import pyrevit
from Autodesk.Revit.DB import FilteredElementCollector, ParameterValueProvider, FilterStringEquals, \
    ElementParameterFilter, BuiltInCategory, BuiltInParameter
import clr
from pyrevit import forms, revit, DB, script, UI
from omniclass import *
from view import *

x = MyWindow()
x.ShowDialog()
project_client_id = x.project_client_id

if project_client_id:
    omniclass.filter_by_level(2)
    items = omniclass.name_level
    name_code = omniclass.code_level

    select_item = forms.SelectFromList.show(items, button_name='Select object', title='Please select object')
    if select_item:
        index_selected = items.index(select_item)
        object_code = name_code[index_selected]

        # Create a message box
        # message_box = forms.alert(
        #     object_code,
        #     title="omniclass_code",
        #     warn_icon=False
        # )
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
                    pp = element
                    omniclass_number = p.get_Parameter(BuiltInParameter.OMNICLASS_CODE).AsString()
                    if p.LookupParameter('Color'):
                        Color = p.LookupParameter('Color').AsString()
                    else:
                        Color = "N/A"
                    if p.LookupParameter('Height'):
                        Height = p.LookupParameter('Height').AsValueString()
                    else:
                        Height = "0"
                    if p.LookupParameter('Length'):
                        Length = p.LookupParameter('Length').AsValueString()
                    else:
                        Length = "0"
                    if p.LookupParameter('Width'):
                        Width = p.LookupParameter('Width').AsValueString()
                    else:
                        Width = "0"
                    if p.LookupParameter('Depth'):
                        Depth = p.LookupParameter('Depth').AsValueString()
                    else:
                        Depth = "0"
                    if p.LookupParameter('Thickness'):
                        Thickness = p.LookupParameter('Thickness').AsValueString()
                    else:
                        Thickness = "0"
                    if p.LookupParameter('Material'):
                        Material = p.LookupParameter('Material').AsValueString()
                    else:
                        Material = "N/A"
                    if p.LookupParameter('Weight'):
                        Weight = p.LookupParameter('Weight').AsValueString()
                    else:
                        Weight = "0"
                    if p.LookupParameter('ManufacturerFa'):
                        ManufacturerFa = p.LookupParameter('ManufacturerFa').AsString()
                    else:
                        ManufacturerFa = "N/A"
                    if p.LookupParameter('Manufacturer'):
                        Manufacturer = p.LookupParameter('Manufacturer').AsString()
                    else:
                        Manufacturer = "N/A"
                    if p.LookupParameter('ModelLabel'):
                        ModelLabel = p.LookupParameter('ModelLabel').AsString()
                    else:
                        ModelLabel = "N/A"
                    if pp.LookupParameter('AcquisitionDatePlanned'):
                        AcquisitionDatePlanned = pp.LookupParameter('AcquisitionDatePlanned').AsString()
                    else:
                        AcquisitionDatePlanned = "2000-01-01"

                    for d in table:
                        if d == []:
                            table.remove([])
                            table.append([project_client_id, omniclass_number, 1, Color, Height, Length,
                                          Width, Depth, Thickness, Material, Weight, ManufacturerFa, Manufacturer,
                                          ModelLabel, AcquisitionDatePlanned])
                        elif d[13] == ModelLabel and d[3] == Color and d[4] == Height and d[5] == Length and d[
                            6] == Width \
                                and d[7] == Depth and d[8] == Thickness and d[9] == Material and d[
                            14] == AcquisitionDatePlanned:
                            d[2] = d[2] + 1
                    ModelLabellist = [d[13] for d in table]
                    Colorlist = [d[3] for d in table]
                    Heightlist = [d[4] for d in table]
                    Lengthlist = [d[5] for d in table]
                    Widthlist = [d[6] for d in table]
                    Depthlist = [d[7] for d in table]
                    Thicknessllist = [d[8] for d in table]
                    Materiallist = [d[9] for d in table]
                    AcquisitionDatePlannedlist = [d[14] for d in table]
                    if ModelLabel not in ModelLabellist or Color not in Colorlist or Height not in Heightlist \
                            or Length not in Lengthlist or Width not in Widthlist or Depth not in Depthlist or Thickness not in Thicknessllist \
                            or Material not in Materiallist or AcquisitionDatePlanned not in AcquisitionDatePlannedlist:
                        table.append([project_client_id, omniclass_number, 1, Color, Height, Length,
                                      Width, Depth, Thickness, Material, Weight, ManufacturerFa, Manufacturer,
                                      ModelLabel, AcquisitionDatePlanned])

        output = pyrevit.output.get_output()
        output.add_style('body { color: blue; }')
        output.print_table(
            table_data=table,
            title="Object_Data",
            columns=["project_client_id", "omniclass_number", "count", "Color", "Height", "Length",
                     "Width", "Depth", "Thickness", "Material", "Weight", "ManufacturerFa", "Manufacturer",
                     "ModelLabel", "AcquisitionDatePlannedlist"],
            formats=['', '', '', '', '', '', '', '', '', '', '', '', '', ''],
            last_line_style='color:red;'
        )
        table.insert(0, ["projectclient_id", "omniclass_code", "count", "Color", "Height", "Length",
                         "Width", "Depth", "Thickness", "Material", "Weight", "ManufacturerFa", "Manufacturer",
                         "ModelLabel", "AcquisitionDatePlanned"])
# for num in table:
#     num[2] = "{}".format(num[2])

if not os.path.exists("c:/NLBO"):
    os.mkdir("c:/NLBO")
if os.path.exists("c:/NLBO/table.csv"):
    os.remove("c:/NLBO/table.csv")

with open("c:/NLBO/table.csv", 'wt') as file:
    # Create a writer object
    writer = csv.writer(file)
    # Write the data to the CSV file
    for row in table:
        if row:
            writer.writerow([str(s).encode('utf-8') for s in row])
os.system("python C:/Users/ali/Documents/GitHub/procurement/app.py")
webbrowser.open("http://127.0.0.1:5000")

__title__ = "NLBO suppliar"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

# from pyrevit import forms
# items = ['item1', 'item2', 'item3']
# forms.SelectFromList.show(items, button_name='Select Item')


import clr
clr.AddReference('System.windows.Forms')
clr.AddReference('IronPython.Wpf')

#find the path of ui.xaml
from pyrevit import script
xamlfile = script.get_bundle_file('ui.xaml')

#import wpf creator and base window
import wpf
from System import Windows

class MyWindow(Windows.Window):
    def __init__(self):
        wpf.LoadComponent(self, xamlfile)

# let's show the windows
MyWindow().ShowDialog()
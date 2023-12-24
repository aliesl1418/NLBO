__title__ = "NLBO supplier"
__author__ = "Ali Eslamifar"
__doc__ = """ This is NLBO supllier application"""

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
#
# # let's show the windows
# MyWindow().ShowDialog()
from pyrevit import forms,script
w = forms.WPFWindow('ui.xaml', literal_string=False)
w.set_icon('icon.bmp')
w.show()

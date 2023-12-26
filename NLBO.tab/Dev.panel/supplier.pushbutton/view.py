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
    def Name = self.name


# let's show the windows
MyWindow().ShowDialog()
from System import Windows
from pyrevit import script, UI
import wpf
import clr
clr.AddReference('System.windows.Forms')
clr.AddReference('IronPython.Wpf')


class MyWindow(Windows.Window):
     def __init__(self):
           xamlfile = script.get_bundle_file('ui.xaml1')
           wpf.LoadComponent(self, xamlfile)
     def save(self, sender, args):
           self.project_client_id = self.txt_id.Text
           self.Close()
           UI.TaskDialog.Show("hello", "hello{}".format(self.project_client_id))





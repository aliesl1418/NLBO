# import re
# items = []
# with open("omniclass.txt", "r") as f:
#     lines = f.readlines()
# for line in lines:
#     if re.match("([\d]{2}\.[\d]{2}\.[\d]{2}\.00)\t",line):
#         for ifc_product_name in re.findall("\t(.*?)\t", line):
#             items.append(ifc_product_name)
# print(items)


# from omniclass import *
# x = omniclass()
# items = list(x.ifc.keys()
#
# print(items)

import forms

class MyForm(forms.Form):
    def __init__(self):
        super().__init__()

        self.list = ["Item 1", "Item 2", "Item 3"]

        self.selected_item = forms.SelectFromList(
            label="Select an item:",
            options=self.list,
            default=None,
        )

    def open(self):
        # Open the list form and get the selected item
        selected_item = self.selected_item.open()

        # If an item was selected, open another form
        if selected_item:
            another_form = AnotherForm(selected_item)
            another_form.open()

class AnotherForm(forms.Form):
    def __init__(self, selected_item):
        super().__init__()

        self.selected_item = selected_item

        self.label = forms.Label(label="Selected item:", text=self.selected_item)

    def open(self):
        # Open the label form
        self.label.open()

if __name__ == "__main__":
    # Create and open the main form
    form = MyForm()
    form.open()

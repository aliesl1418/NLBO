import re

class omniclass:
  @classmethod
  def ifc_dict(self):
    with open("omniclass.txt", "r") as f:
        ifc_info = {}
        for line in f:
            ifc_numbers = []
            ifc_level = []
            ifc_name = []
            for ifc_product_number in re.findall("([\d\.]{6,})\t", line):
                ifc_numbers.append(ifc_product_number)

            for ifc_product_level in re.findall("\t(\d)\n", line):
                ifc_level.append(ifc_product_level)

            for ifc_product_name in re.findall("\t(.*?)\t", line):
                ifc_name.append(ifc_product_name)

            ifc_info[ifc_numbers[0]] = [ifc_name[0], ifc_level[0]]
    self.ifc = ifc_info
  @classmethod
  def filter_by_level(self, level):
      with open("omniclass.txt", "r") as f:
          self.name_level = []
          self.code_level = []
          for line in f:
              for ifc_product_level in re.findall("\t(\d)\n", line):
                  if int(ifc_product_level) == int(level):
                     for ifc_product_name in re.findall("\t(.*?)\t", line):
                         self.name_level.append(ifc_product_name)
                     for ifc_product_number in re.findall("([\d\.]{6,})\t", line):
                         self.code_level.append(ifc_product_number)


# omniclass.filter_by_level(2)
# items = omniclass.name_level
# name_code = omniclass.code_level
# select_item = ['Doors']
# index_selected = items.index(select_item[0])
# object_code = name_code[index_selected]
# print(object_code)

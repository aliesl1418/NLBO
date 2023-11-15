import re
# with open("omniclass.txt", "r") as f:
#         lines = f.readlines()
#         print(len(lines))
# ifc_number = []
# for line in lines:
#   key = re.findall("\d[\d\.]*\d", line)
#   ifc_number = key[0]
# print(ifc_number)

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



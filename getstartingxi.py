
# import csv
# def get_startingxi_from_matches():
#     startingxi = [{
#     "Defenders": set(),
#     "Midfielders": set(),
#     "Forwards": set(),
# }] * 38
#     with open("passingevents.csv") as f:
#         lis = [line.split() for line in f]        # create a list of list
#         team = "Huskies"
#         for i, x in enumerate(lis):              #print the list items 
#             # x[1] = x[1].split(',')
#             if len(x) > 1:
#                 x[0] = x[0].split(',')
#                 x[1] = x[1].split(',')
#             if x[0][2][:9] == "Huskies_D" and len(startingxi[int(x[0][0]) - 1]["Defenders"]) < 4:
#                 startingxi[int(x[0][0]) - 1]["Defenders"].add(x[0][2])
#             elif x[0][2][:9] == "Huskies_M" and len(startingxi[int(x[0][0]) - 1]["Midfielders"]) < 4:
#                 startingxi[int(x[0][0]) - 1]["Midfielders"].add(x[0][2])
#             elif x[0][2][:9] == "Huskies_F" and len(startingxi[int(x[0][0]) - 1]["Forwards"]) < 2:
#                 startingxi[int(x[0][0]) - 1]["Forwards"].add(x[0][2])
#     with open("startingxis.csv", mode = 'w') as xis:
#         header_writer = csv.writer(xis, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         header_writer.writerow(['','Defenders', 'Midfielders', 'Forwards'])
#         stat_writer = csv.writer(xis, delimiter= ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         for i in startingxi:
#             stat_writer.writerow(['Match{}'.format(startingxi.index(i) + 1), i["Defenders"], i["Midfielders"], i["Forwards"]])

# get_startingxi_from_matches()

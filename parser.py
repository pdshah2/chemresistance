import csv

# dutyTrack = open("chemical-resistance-guide-min.csv", "r")
dutyTrack = open("Sangir-Chemical-resistance-Chart.csv", "r")


# Set up CSV reader and process the header
csvReader = csv.reader(dutyTrack)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)
header = next(csvReader)

materials = header

# print(materials)
mat = "".join(materials)

mat = mat.split()

# for i in range(0,len(mat)-1,1):
#     if mat[i] == " " and mat[i+1]==" ":
#         mat.replace(" ","")

    # print(mat[i])

print(len(mat))
print(type(mat))

print(mat)

# nameIndex = header.index("SUMMARY")
# dateIndex = header.index("DTSTART")
#
# # Make an empty list
# csvList = []
#
# # Loop through the lines in the file and get each coordinate
# for row in csvReader:
#     name = row[nameIndex]
#     name = name.replace("(P) ", "")
#     name = name.replace("(S) ", "")
#     date = row[dateIndex].rstrip(' 0:0')
#     date = date.replace("/",'.')
#     csvList.append([name,date])
#
# # Print the coordinate list
# file=open("output.txt","w")
# file.writelines(["%s," % item  for item in csvList])
# file.close()

# arr = []
# for row in csvReader:
#     arr.append(row)

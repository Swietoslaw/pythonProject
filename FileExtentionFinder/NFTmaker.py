path = r"C:\Users\malin\OneDrive\Desktop\image.jpg"
path2 = r"C:\Users\malin\OneDrive\Desktop\image2.jpg"
fp = open(path, 'rb')

finalData = b''

data = fp.read()
data2 = data

for c in range(len(data2)):
  #  finalData += bytes("a","utf-8")

    if c > (len(data2)-30):
        finalData += bytes(data2[c])
    elif c > 29:
        if (data2[c] == "\\"):
            finalData += bytes(data2[c])

        elif (data2[c] == "x"):
            finalData += bytes(data2[c])

        else:
            finalData += bytes(0)
    else:
        finalData += bytes(data2[c])

print(finalData)
finalData2 = str(finalData)
x = 0

fp = open(path2,'wb')
fp.write(finalData)

print(data)
print(data2)
fp.close()
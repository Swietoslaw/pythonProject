path = r"C:\Users\malin\OneDrive\Desktop\image.jpg"  # change to argv or stdin
fp = open(path, 'rb')

data = fp.read(3)
data2 = fp.read()
lastdata = data2[-2:]
if (data == b'\xff\xd8\xff') & (lastdata == b'\xff\xd9'):
    print("JPEG")

fp.close()


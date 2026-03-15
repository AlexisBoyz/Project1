fileFrom = open("path", "r")
fileTo = open("Черновик", "w")

line = fileFrom.readline()
countLines = 1
while line != "":
    fileTo.write(str(countLines) + " - " + line)
    line = fileFrom.readline()
    countLines += 1

fileFrom.close()
fileTo.close()
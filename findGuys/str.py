def loadDataFromTxt(fileName, fileWrite):
    fr = open(fileName, 'r', encoding='utf-8')
    name = open(fileWrite, 'w', encoding='utf-8')
    for line in fr.readlines():
        line = line.split()
        name.write(line[0]+'\n')
    fr.close()
    name.close()

loadDataFromTxt('xinanxinan.txt', 'name.txt')

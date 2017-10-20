dianYuan = open('dianyuan.txt', 'r', encoding='utf-8')
dianYuanName = []
xinAn = open('xinan.txt', 'r', encoding='utf-8')
xinAnName = []
jiJi = open('jiji.txt', 'w', encoding='utf-8')

for line in xinAn.readlines():
    line = line.split()
    xinAnName.append(line[0])

for line in dianYuan.readlines():
    lineArray = line.split()
    if lineArray[0] in xinAnName:
        jiJi.write(line+'\n')

dianYuan.close()
xinAn.close()
jiJi.close()

with open('NITs_list.txt','r') as file:
    info = file.readlines()
    list = []
    for i in range(len(info)):
        if i%7 == 0:
            list.append(info[i][0:-2])

for i in list:
    name = 'NITs/'+str(i.split()[0])+'_'+str(i.split()[1])+'.txt'
    with open(name,'w') as file:
        pass

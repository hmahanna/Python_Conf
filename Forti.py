import os


filepath = os.path.join('C:/Users/Noha/Desktop', 'Results.txt')
if not os.path.exists('C:/Users/Noha/Desktop'):
    os.makedirs('C:/Users/Noha/Desktop')
f = open(filepath)
#time.sleep(2)
#f.write(x)

print(f)

l = []

for line in f:

    line = line.rstrip()
    #print(line)
    l.append(line)


filesave = filepath = os.path.join('C:/Users/Noha/Desktop', 'save.txt')
with open (filesave , 'w') as p:

    for ip in l:
        print ("edit  Office_" + ip , file=p)
        print ("set subnet " + ip , file=p)
        print("next" + '\n', file=p)



    #p.write(print1)
    #p.write(print2)

#print(l)



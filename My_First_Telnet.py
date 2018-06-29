import getpass
import telnetlib
import time
import os


def ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    print(start)
    end = list(map(int, end_ip.split('.')))
    print(end)
    iprange = []
    while start != list(map(int, end_ip.split('.'))):
        for i in range(len(start) - 1, -1, -1):
            if start[i] < 255:
                start[i] += 1
                break
            else:
                start[i] = 0
        iprange.append('.'.join(map(str, start)))
    iprange = [start_ip] + iprange
    return iprange



while True:



    #HOST = input("Enter your HOST IP ADD : ")
    s = input("Enter your first IP ADD : ")
    e = input("Enter your second IP ADD : ")
    user = input("Enter your remote account: ")

    #password = getpass.getpass(prompt="Input:")
    password = input("Enter your password: ")
    en = input("Enter your enable pass : ")

    iprange = ip_range(s,e)
    for HOST in iprange:
        try:

            tn = telnetlib.Telnet(HOST)
            print (HOST , 'ok')

        except:
            print(HOST , 'HOST Not Found')
            continue

        tn.read_until(b"Username:")
        tn.write(user.encode('ascii') + b"\n")
        print (user + 'accessed sucsessfuly ........ ')
        if password:
            tn.read_until(b"Password:")
            tn.write(password.encode('ascii') + b"\n")

        if en:
            tn.read_until(b"R1>")
            tn.write(b"enable\n")
            if password:
                tn.read_until(b"Password:")
                tn.write(password.encode('ascii') + b"\n")


        time.sleep(2)
        print(user + 'accessed sucsessfuly ........ ')

        time.sleep(2)
        tn.write(b"terminal length 0\n")
        tn.write(b"config t\n")
        print('Config t entered ...........')
        time.sleep(2)
        tn.write(b"int GigabitEthernet3/0\n")
        print('Interface mode entered ........')
        time.sleep(2)
        tn.write(b"ip add 10.10.1.2 255.255.255.0\n")
        print('IP configured ........')
        #tn.write(b"do show ip int br \n")
        time.sleep(2)
        tn.write(b"do show run \n")
        print('Show run sent ........')
        time.sleep(3)
        x = tn.read_very_eager().decode('UTF-8')
        #x = tn.read_eager().decode('ascii')
        time.sleep(2)
        fname = 'show run ' + HOST + '.txt'
        filepath = os.path.join('C:/Users/Noha/Desktop', fname )
        if not os.path.exists('C:/Users/Noha/Desktop'):
            os.makedirs('C:/Users/Noha/Desktop')
        f = open(filepath, "a")
        time.sleep(2)
        f.write(x)
        f.close()
        print(x)


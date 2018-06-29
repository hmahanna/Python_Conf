
#def R(HOST)

OCT_RANGE = []
IP_CUT = []
IP_RANGE = []
IP_RANGE.append(input(" please Enter the first IP Add in the range > "))
IP_RANGE.append(input(" please Enter the second IP Add in the range > "))
# IP_RANGE[0] = input(" please Enter the first IP Add in the range > ")
# IP_RANGE[1] = input(" please Enter the second IP Add in the range > ")
print(IP_RANGE)

for ip in IP_RANGE:
    _IP_ = ip.split()
    print(_IP_)
   # i = _IP_[0]
    IP_CUT = _IP_[0].split('.')
    print(IP_CUT)
    #OCT_RANGE.append(IP_CUT[3])
    

#print(OCT_RANGE)

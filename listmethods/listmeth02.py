#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)



#try to demonstrate list.count(x)
#this following line is going to count how many times element "dns" showed up
print(proto.count("dns"))

#try to demonstrate list.insert(i, x)
#this following line is going to insert element x into i position
proto.insert(len(proto), "IPV4")
print(proto)

#try to play with something I didn't use before, which is list.index(x[,start[,end]])
print(proto.index("dns"))


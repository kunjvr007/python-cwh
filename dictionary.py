# dictionary is nothing but a key value pairs
d1 = {}
# print(type(d1))
d2 = {"justin":"baby", "weekend":"pray for me","travis":"angel baby","arjit":{"a":"khamosiya","b":"beh chala","c":"phir kabhi"}}
print(d2["arjit"]["a"])
d2["kunj"] = "besabriya" #this will add if not in the list
d2[420]= "bantai"
del d2[420]
print (d2)
print(d2.keys())
print(d2.items())
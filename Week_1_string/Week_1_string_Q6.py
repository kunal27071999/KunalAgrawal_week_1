"""6. str = "abrakadabra"
What will be the output of below
	str[1:6:20]
	str[::1]
	str[::-1]
	str[3:7:-1]
	str[7:4:-1]
	str[0:10000:1]
	str[-4:1:-1]
	str[-4:1:-2]
	str[5:0:1]
	str[9:0:0]
	str[0:-10:-1]
	str[0:0:1]
	str[0:-9:-2]
	str[-5:-9--2]
	str[10:-1:-1]
	str[1000:2:1]"""


s = "abrakadabra"
print(s[1:6:20])

print(s[::1])
print(s[::-1])
#print(s[3:7:-1]) cannot print this
print(s[7:4:-1])
print(s[0:1000:1])
print(s[-4:1:-1])
print(s[-4:1:-2])
#print(s[5:0:1])
#print(s[9:0:0])
#print(s[0:-10:-1])
#print(s[10:-1:-1])

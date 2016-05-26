import sys

stop = int(input())
onbus = 0
onbusmax = 0
for i in range(0,stop):
	getoff, geton = input().split()
	onbus += (int(geton) - int(getoff))
	if(onbus > onbusmax):
		onbusmax = onbus
print(onbusmax)
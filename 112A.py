import sys

string1 = input().lower()
string2 = input().lower()

def strcompare(string1, string2):
	for i in range(0,len(string1)):
		if(string1[i]>string2[i]):
			print(1)
			return 1
		elif(string1[i] < string2[i]):
			print(-1)
			return -1
	print(0)
	return 0

strcompare(string1, string2)
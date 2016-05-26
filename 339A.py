import sys

string = input()
string = string.split('+')
string = sorted(string)

ans = ""

for x in range(0,len(string)-1):
	ans += string[x]
	ans += "+"
ans += string[len(string)-1]

print(ans)
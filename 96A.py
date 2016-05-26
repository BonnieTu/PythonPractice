import sys

def main():
	string = input()
	count = 0
	for i in range(1,len(string)):
		if string[i-1] != string[i]:
			count = 0
		else:
			count+=1
			if count>=6:
				print("YES")
				return "YES"
	print("NO")
	return "NO"

if __name__=="__main__":
	main()
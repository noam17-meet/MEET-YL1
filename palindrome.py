n=input()
size_of_string= len(n)
x=len(n)-1
c=""
while x>=0:
	c=c+n[x]
	x=x-1
if c==n:
	print("TRUE")
else:
	print("FALSE")
	
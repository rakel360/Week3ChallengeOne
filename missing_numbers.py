
a = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
b=[]

for x in range(min(a),max(a)):
	if x not in a:
		b.append(x)

a.sort()
print("List of numbers:", a)
print("list of missing numbers:",b)



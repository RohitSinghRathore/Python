def work(num):
	sum=0
	for x in range(num):
		name=int(input("Hours"))
		sum=sum+name
	print("Total Hours"+str(sum) + " and average "+ str((sum)/num))
	return sum;
max= int(input("Input how many employees"))
wholeget=0;
for x in range(max):
	get=work(int(input("Employee "+ str(x+1) +":How many days")))
	print("Total Working hours of both employee" + str(get+wholeget));
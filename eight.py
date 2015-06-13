class Avengers:
	avengersCount=0;        #Class Variable
	def __init__(self,name,power):
		Avengers.avengersCount+=1;   # 4,5 and  6  lines are instance variables.
		self.name=name;
		self.power=power;
	def howMany():			
		print("Total Avengers %d" % Avengers.avengersCount);
		return Avengers.avengersCount;
	def getName(self):
		print("Avenger Name:"+self.name+" have power "+self.power);
hulk=Avengers("hulk","Angryness");
print("how Many:", Avengers.howMany()); 
hulk.getName();
hulk.size="Very big";
print(hulk.size);
##del hulk.name; -----------------------> delete the name of hulk
##print(hulk.name); --------------------> will show an error
print(getattr(hulk,"name"));
print(setattr(hulk,"name","Stupid hulk")); ## returns none
print(getattr(hulk,"name"));
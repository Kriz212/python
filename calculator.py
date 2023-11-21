def add(x,y):
	return x + y
def subtract(x,y):
	return x - y
def multiply(x,y):
	return x * y
def devide(x,y):	
	return x / y

selection = ('1', '2', '3', '4')
print("1 Add\n2 Subtract\n3 Multiply\n4 Devide\nType quit to exit")



while True:
	choice = input("Please enter 1 2 3 or 4: ")
	if choice == "quit":
			break			
	num1 = int(input("Please enter the first number: "))
	num2 = int(input("Please enter the second number: "))

	if choice in selection:
	
		if choice == "1":
			print(num1, "+", num2, "=", add(num1,num2))
		elif choice == "2":
			print(num1, "-", num2, "=", subtract(num1,num2))	
		elif choice == "3":
			print(num1, "*", num2, "=", multiply(num1,num2))
		elif choice == "4":
			print(num1, "/", num2, "=", devide(num1,num2))					
				



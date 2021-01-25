value = 100
while value > 0:
 	n = int(input("Enter value: "))
 	if n > value:
 		print("NOT CORRECT")
 		continue
 	else:
 		value -= n
print("You have", value)


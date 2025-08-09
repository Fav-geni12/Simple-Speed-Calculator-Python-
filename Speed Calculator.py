# Speed Calculator with a repeat feature

while True:
	try:
			# Ask the user to enter the distance covered.
			distance = float(input("Enter the distance (in meters):"))
		
				# Ask the user to enter the time taken.
			time = float(input("Enter the time (in seconds): "))

			if time != 0:
				speed = distance / time
			else:
				print("Error: Time cannot be zero")
			print("Speed is:", speed, "m/s")

	except ValueError:
			print("Please enter a valid number.")

	repeat = input("Do you want to calculate again (yes / no): ")
	if repeat != "yes":
			print("Thank you, Goodbye!!")
			break 
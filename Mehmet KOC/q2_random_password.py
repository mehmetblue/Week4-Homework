import string
import random
import tkinter as tk

def generate_random_password():
	""" This function generates a desired password length with number of characters. 
	Then displays the result to the user on the windows"""


	## length of password from the user
	desired_password_length = 10


	## character of types of desired minimum number
	uppercases_count = 2
	digits_count = 2
	specials_count = 2
	lowercases_count = 2


	## to check if the lenght of the password reach the lent
	characters_count = lowercases_count + uppercases_count + digits_count + specials_count


	## different types of characters to generate password from
	uppercases = list(string.ascii_uppercase)
	digits = list(string.digits)
	specials = list(string.punctuation)
	lowercases = list(string.ascii_lowercase)


	## list of all character types that will be used to 
	# achieve the desired character length 
	characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)


	## check the total length with characters sum count
	## print not valid if the sum is greater than desired password length
	if characters_count > desired_password_length:
		print("Characters total count is greater than the password length")
		return


	## initializing the password
	password = []
	

	## picking random lowercases
	for i in range(lowercases_count):
		password.append(random.choice(lowercases))


	## picking random uppercases
	for i in range(uppercases_count):
		password.append(random.choice(uppercases))


	## picking random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## picking random special characters
	for i in range(specials_count):
		password.append(random.choice(specials))


	## if the total characters count is less than the password length
	## add random characters to make it equal to the desired password length
	if characters_count < desired_password_length:
		random.shuffle(characters)
		for i in range(desired_password_length - characters_count):
			password.append(random.choice(characters))


	## shuffling the resultant password
	random.shuffle(password)


	## converting the list to string
	## printing the list
	x = "".join(password)
	
	print(x)

	## sending the password to show on the window
	label.config(text=x)



## tkinter part
window = tk.Tk()


window.title("Random Password Generator")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to generate the next password ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" GENERATE ", width=50, height=5, command=generate_random_password)
button1.grid(padx=110, pady=40)


window.mainloop()
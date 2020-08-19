import time, sys

#colors 
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

#typewriter effect function
def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.9)

message = input(yellow + "You find yourself in a burger shop, to try and satisfy your hunger. But, you dont know what to eat. would you like to have an A- Cheeseburger, B- Pasta, or C- Salad. " + green + "[A,B,C]\n")

typewriter(message)
import time, sys

green = "\033[0;32m"
red = "\033[0;31m"

def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.9)


message = (red + 'We meet again, world. My name is Mihir. I live in an undisclosed location.')

typewriter(message)

message2 = (green + 'waddup world')

typewriter(message2)
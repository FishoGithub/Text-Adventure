#colors 
green = "\033[0;32m"
red = "\033[0;31m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_cyan = "\033[0;96m"
bright_blue = "\033[0;94m"


def game_over():
  print(white + "       G A M E   O V E R.")

def game_win():
  print(bright_blue + "        Y O U   W I N! ")
  

answer = input(bright_blue + "you find yourself lost in a cave. you have no idea how you got there, but, you know you want to get out. you see 2 tunnels before you. left, and right. which do you choose?" + green +" [left,right]")


def left_path():

  print(red + "\nyou decide to go left. you find a tv blasting the veggie tales theme song. your head begins to implode but then your realize that in front of you is the off switch.\n")

  answer = input(green + "do you push the button? [Y,N] ").lower().strip()

  if answer == "y":
    print(red + "\nyou push the button. the song doesn't stop. you hear a noise from above, and your realize that you've played yourself. suddenly, a lima beeeeean drops on top of you. your life force slowly fades as you hear the song play...\n")

    game_over()

  elif answer == "n":
    print(bright_cyan + "\nyou calmly walk past the anomaly, trying not to lose your sanity, and walk through the next tunnel. you come up on a room with a sword sitting on a stone. the sword appears to be hovering.\n")

    answer = input(green + "do you take the sword? [Y,N] ").lower().strip()

    if answer == "y":
      print(red + "\nyou take the sword, but, while taking it, you get cut. you slowly bleed out because you didn't have a band-aid.\n")

      game_over()

    elif answer == "n":
      print(bright_cyan + "\nyou let the sword be. some things are not meant to be taken.\n")

      print(red + "as you walk into the next room, you feel a rumble in your stomach. you're hungry. After a bit of searching, you find 2 possible food sources, some chicken that you cooked, or mushrooms that you found growing on the wall.\n")

      answer = input(green + "which do you choose? [1,2] ")

      if answer == '2':
        print(red + "you eat the mushrooms that you found growing from the wall. honestly, what did you think would happen, you feel a strange sensation in your stomach. you realize that you've made a stupid mistake.\n")

        game_over()

      elif answer == "1":
        print(bright_cyan + "you eat the chicken. sometimes the simpler choice is the best one.")

        print(bright_blue + "\nwhile eating the chicken, you feel a surge of power breezign through you. you suddenly can see through the walls, and you see the way out. using the power of chicken you go through the walls to get to the exit. but, if you leave, you will lose your power of the chicken.\n")

        answer = input(green + "Do you leave? [Y,N] ").lower().strip()

        if answer == "n":
          print(red + "\nyou don't leave. but then, you recall something about your adventure. every time you tried to make the logical chioce, you've been tricked. you realize this just as a boulder falls on your head.\n")

          game_over()

        elif answer == "y":
          print(bright_cyan + "\nyou exit the cave. you made the right choice. good job! now, to start your long walk home...\n")

          game_win()



if answer == 'left':
  left_path()
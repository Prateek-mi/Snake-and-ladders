#snakesandladder
import random
import time
import sys

max_val = 100

snakes = { 15:4,             #the snakes if key hits it returns values
           34:28,
           44:25,
           67:31,
           77:45,
           96:9
                }

ladder = {11:51,         #the ladder same if key hits it returns values
          24:43,
          46:87,
          48:69,
          57:98,
          58:62,
               }

snake_bite = ["hissssss","ohh nooo","kaat liya re maiiyaa"]
ladder_hit = ["yooohooo","shortcut","sidi mil gya baba"]

def welcome_msg(): # just a welcome function
  print("welcome to the snake and ladder game")
  print("you can get hisss or ladder short cut")
  print("ARE YOU READY ????")
  time.sleep(1)
  print("lets play.........!")

def get_player_name(): #taking player name function
  player1_name = input("enter player 1 name please: ")
  print(player1_name)
  player2_name = input("enter player 1 name please: ")
  print(player2_name)
  return player1_name,player2_name

def get_dice_value(): # getting dice value randomly generated
    time.sleep(1)
    dice_value = random.randint(1,6)
    print("Its a " , dice_value)
    return dice_value


def got_snake_bite(old_value, current_value, player_name):  # if snake bites
  print(random.choice(snake_bite).upper() + " hisss~~~~~~~~>")
  print(player_name + " go down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name): # if player got a ladder
  print(random.choice(ladder_hit).upper() + " ########")
  print(player_name + "go up from" + str(old_value) + " to " + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(1)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > max_val:
      print("You need " + str(max_val - old_value) + " to win this game. Keep trying.")
      return old_value

    print(player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
      final_value = snakes.get(current_value)
      got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladder:
      final_value = ladder.get(current_value)
      got_ladder_jump(current_value, final_value, player_name)

    else:
      final_value = current_value

    return final_value


def check_win(player_name, position):
  time.sleep(1)
  if max_val == position:
    print("\n\n\nThats it.\n\n" + player_name + " won the game.")
    print("Congratulations " + player_name)
    print("\nThank you for playing the game. great spirit shown\n")
    sys.exit(1)

def start():
  welcome_msg()
  time.sleep(1)
  player1_name, player2_name = get_player_name()
  time.sleep(1)

  player1_current_position = 0
  player2_current_position = 0

  while True:
    time.sleep(1)
    input_1 = input("\n" + player1_name + ": " + "its your turn go ahead" + " Hit the enter to roll dice: ")
    print("\nRolling dice...")
    dice_value = get_dice_value()
    time.sleep(1)
    print(player1_name + " moving....")
    player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

    check_win(player1_name, player1_current_position)

    input_2 = input("\n" + player2_name + ": " + "its your turn go ahead Hit the enter to roll dice: ")
    print("\nRolling dice...")
    dice_value = get_dice_value()
    time.sleep(1)
    print(player2_name + " moving....")
    player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

    check_win(player2_name, player2_current_position)

if __name__ == "__main__":
    start()
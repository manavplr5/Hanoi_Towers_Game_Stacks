from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
Left = Stack("left_stack")
Middle = Stack("middle_stack")
Right = Stack("right_stack")
stacks.append(Left)
stacks.append(Middle)
stacks.append(Right)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
  Left.push(i)
num_optical_moves = (2**(num_disks)) - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optical_moves))
  

#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    user_input = input(">>")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
        
#Play the Game
num_user_moves = 0
while Right.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items() 
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack  = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.get_size() == 0:
      print("\n\nInvalid Move. Try Again")
    elif to_stack.get_size()==0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
print("\n\nYou completed the games in {0} moves, and the optimal number of movies is {1}".format(num_user_moves, num_optical_moves))      
      





























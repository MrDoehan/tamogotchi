from tamagotchi import Tamagotchi
import alg
name = input("What would you like to name your Tamagotchi pet? ")
pet = Tamagotchi(name)
print(pet)
action = input("What would you like to do? feed/wait/play: ")
view = action.split()
while action != "":
  if action == "wait":
    pet.increment_time()
    print(pet)

    alg.counter +=1
  if action == "play":
    pet.play()
    print(pet)

    alg.counter+=1
  if action == "feed":
    pet.feed()
    print(pet)
    alg.counter+=1
  print(Tamagotchi.thing)
  action = input("What would you like to do? feed/wait/play: ")
  
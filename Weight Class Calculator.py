WEIGHT_CLASSES = [
  (115, 124, "Strawweight"),
  (125, 134, "Flyweight"),
  (135, 144, "Bantamweight"),
  (145, 154, "Featherweight"),
  (155, 169, "Lightweight"),
  (170, 184, "Welterweight"),
  (185, 204, "Middleweight"),
  (205, 264, "Light Heavyweight"),
  (265, None, "Heavyweight")
]

def get_weight_class(weight):
  for min_weight, max_weight, class_name in WEIGHT_CLASSES:
    if max_weight is None:
      if weight >= min_weight:
        return class_name
    elif min_weight <= weight <= max_weight:
        return class_name
  return None

def get_weight():
  while True:
    try:
      weight = int(input('How much do you weigh in lbs?: '))
      return weight
    except ValueError:
      print("Please enter a valid number.")

def get_fighter_name():
  name = input("What is the fighter's name?: ")
  return name

def save_fighter_profile(fighter):
  with open("fighters.txt", "a") as file:
    file.write("Fighter Profile\n")
    file.write(f"Name: {fighter['name']}\n")
    file.write(f"Weight: {fighter['weight']} lbs\n")
    file.write(f"Class: {fighter['weight_class']}\n")
    file.write("--------------------\n")

def view_saved_fighters():
    try:
      with open("fighters.txt", "r") as file:
        saved_fighters = file.read()
        print("\nSaved Fighters")
        print(saved_fighters)
    except FileNotFoundError:
      print("No saved fighters found yet.")

def main():
  fighter_name = get_fighter_name()
  weight_input = get_weight()

  weight_class = get_weight_class(weight_input)

  fighter = {
    "name": fighter_name,
    "weight": weight_input,
    "weight_class": weight_class
  }

  if weight_class:
    print("\nFighter Profile")
    print(f"Name: {fighter['name']}")
    print(f"Weight: {fighter['weight']} lbs")
    print(f"Class: {fighter['weight_class']}")

    save_fighter_profile(fighter)
    print("Fighter profile saved to fighters.txt")
  else:
    print("Sorry! You are not heavy enough for a listed weight class yet.")

  view_saved_fighters()

  print("Thank you! This program has concluded...")

main()
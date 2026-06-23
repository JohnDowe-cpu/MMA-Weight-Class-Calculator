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

def show_menu():
  print("\nMMA Fighter Tracker")
  print("1. Add fighter profile")
  print("2. View saved fighters")
  print("3. Search fighter by name")
  print("4. Quit")

def get_menu_choice():
  choice = input("Choose an option: ")
  return choice

def create_fighter_profile():
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

def search_fighter_by_name():
  search_name = input("Enter fighter name to search: ")

  try:
    with open("fighters.txt", "r") as file:
      saved_fighters = file.read()

      if search_name in saved_fighters:
        print(f"{search_name} found in saved fighters.")
      else:
        print(f"{search_name} not found.")
  except FileNotFoundError:
    print("No saved fighters found yet.")

def main():
  while True:
    show_menu()
    choice = get_menu_choice()
    
    if choice == "1":
      create_fighter_profile()
    elif choice == "2":
      view_saved_fighters()
    elif choice == "3":
      search_fighter_by_name()
    elif choice == "4":
      print("Thank you! This program has concluded...")
      break
    else:
      print("Invalid choice. Please choose 1, 2, 3, or 4.")

main()
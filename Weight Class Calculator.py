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
    
    
def main():
  weight_input = get_weight()

  weight_class = get_weight_class(weight_input)

  if weight_class:
    print (f"You are a {weight_class}!")
  else:
    print("Sorry! You are not heavy enough for a listed weight class yet.")

  print("Thank you! This program has concluded...")

main()
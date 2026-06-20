def get_weight_class(weight):
  if 115 <= weight <= 124:
    return "Strawweight"
  elif 125 <= weight <= 134:
    return "Flyweight"
  elif 135 <= weight <= 144:
    return "Bantamweight"
  elif 145 <= weight <= 154:
    return "Featherweight"
  elif 155 <= weight <= 169:
    return "Lightweight"
  elif 170 <= weight <= 184:
    return "Welterweight"
  elif 185 <= weight <= 204:
    return "Middleweight"
  elif 205 <= weight <= 264:
    return "Light_Heavy weight"
  elif weight >= 265:
    return "Heavyweight"
  else:
    return None

def get_weight():
  weight = int(input('How much do you weigh in lbs?: '))
  return weight
weight_input = get_weight()

weight_class = get_weight_class(weight_input)

if weight_class:
  print (f"You are a {weight_class}!")
else:
  print("Sorry! You are not heavy enough for a listed weight class yet.")
print("Thank you! This program has concluded...")
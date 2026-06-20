weight_input = int(input("How much do you weigh in lbs?: "))

if 115 <= weight_input <= 124:
    print("You are a Strawweight!")
elif 125 <= weight_input <= 134:
    print("You are a Flyweight!")
elif 135 <= weight_input <= 144:
    print("You are a Bantamweight!")
elif 145 <= weight_input <= 154:
    print("You are a Featherweight!")
elif 155 <= weight_input <= 169:
    print("You are a Lightweight!")
elif 170 <= weight_input <= 184:
    print("You are a Welterweight!")
elif 185 <= weight_input <= 204:
    print("You are a Middleweight!")
elif 205 <= weight_input <= 264:
    print("You are a Light_Heavy weight!")
elif weight_input >= 265:
    print("You are a Heavyweight!")
else:
    print("Sorry! Not you are not heavy enough yet.")
print("Thank you! This program has concluded...")
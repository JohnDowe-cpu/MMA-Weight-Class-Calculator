weight_input = int(input("How much do you weigh in lbs?: "))
strawweight = weight_input >= 115 and weight_input <= 124
flyweight = weight_input >= 125 and weight_input <= 134
bantamweight = weight_input >= 135 and weight_input <= 144
featherweight = weight_input >= 145 and weight_input <= 154
lightweight = weight_input >= 155 and weight_input <= 169
welterweight = weight_input >= 170 and weight_input <= 184
middleweight = weight_input >= 185 and weight_input <= 204
light_heavyweight = weight_input >= 205 and weight_input <= 264
heavyweight = weight_input >= 265

if strawweight:
    print("You are a Strawweight!")
elif flyweight:
    print("You are a Flyweight!")
elif bantamweight:
    print("You are a Bantamweight!")
elif featherweight:
    print("You are a Featherweight!")
elif lightweight:
    print("You are a Lightweight!")
elif welterweight:
    print("You are a Welterweight!")
elif middleweight:
    print("You are a Middleweight!")
elif light_heavyweight:
    print("You are a Light_Heavy weight!")
elif heavyweight:
    print("You are a Heavyweight!")
print("Thank you! This program has concluded...")
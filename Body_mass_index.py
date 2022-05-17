print("*********"
      " Body Mass Index "
      "*********")

weight = float(input("Your weight:"))
length = float(input("Your length(decimal number) :"))
body_mass_index = weight / (length * length)
print("Your length : {}, Your weight : {}, Your body mass index : {}".format(length, weight, body_mass_index))

if body_mass_index < 18.5 :
    print("Weak")
elif body_mass_index > 18.5 and body_mass_index < 25:
    print("Normal")
elif body_mass_index > 25 and body_mass_index < 30:
    print("Fat")
else:
    print("Obese")


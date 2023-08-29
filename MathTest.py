acceleration_due_to_gravity = float(input("Enter your value of acceleration in m/s2: "))
mass_of_object = float(input("Enter mass of object in Kg: "))
formulae_of_weight = acceleration_due_to_gravity * mass_of_object
final_answer = str(round(formulae_of_weight, 2))
final_form = "Your total weight rounded to 2 decimal places is " + str(final_answer)
print(final_form)
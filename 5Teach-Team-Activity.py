print()
GradePre = float (input ("What is your grade precentage? %"))
if GradePre >= 90:
    print("You have an A")
elif GradePre >= 80:
    print("You have a B")
if GradePre >= 70:
    print("You have a C")
# Below is the text related to whether or not the person passed the class.
if GradePre >= 70:
    print("You passed the class! Your parents must be proud!")
elif GradePre <= 70:
    print("You have failed the class and will need to retake.")
print()
print()
# R1Age stands for Rider one age, and R1Hieght stands for Rider 1 Height
R1Age = int (input("What is the age of the first rider in year? "))
R1Hieght = int (input("What is the height of the first rider in inches? "))
R2Age = int (input('What is the age of the second rider? '))
R2Hieght = int (input('What is the height of the second rider in Inches? '))

if R1Hieght <= 36: 
    False
    print('Sorry rider one, you are not allowed on this ride.')
elif R1Hieght >= 36:
    True
if R2Hieght <= 36:
    False
    print('Sorry rider two, you are not allowed on this ride.')
elif R2Hieght >= 36:
    True
print()
# Here we first need to set up our varables
child_meal = float(input('What is the price of a childs meal? '))
child_number = int(input('How many children? '))
adult_meal = float(input('What is the price of an adults meal? '))
adult_number = int(input('How many adults? '))
senior_meal = float(input('What is the price for persons over age 65? '))
senior_number = int(input('How many persons over age 65? '))
sales_tax_per = float(input('What is the state sales tax? %'))
print()
# Here is where we start to do the math after the user has inputed all their data
meal_subtotal = (child_number * child_meal) + (adult_meal * adult_number) + (senior_meal * senior_number)
sales_tax_del = sales_tax_per / 100
tax = sales_tax_del * meal_subtotal
meal_total = tax + meal_subtotal
# After the first round of calculations now we need to figure out the payment.
print(f'Your subtotal is ${meal_subtotal}')
print(f'The sales tax is ${tax}')
print(f'Your final total is ${meal_total}')
print()
payment = float(input('How much would you like to pay? $'))
#Next set of functions is to figure out payment and display the total after that.
meal_total = meal_total - payment
print(f'Your new total is ${meal_total}')

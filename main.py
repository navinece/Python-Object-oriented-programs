from Customer import Customer 

customer1  = Customer('meenakshi', 1000.0)
customer2  = Customer('Anandhi',500.0)
x=customer1.deposit(100)

print( customer1.name +" you deposited $" + str(x[1]) + " and your remaining balance is $" + str(x[0]))



y=customer1.withdraw(500)

print (customer1.name + "you withdrawed $"+ str(y[1]) + " your remaining balance is " + str( y[0]) ) 

print (customer2.name + "You withdrawed $"+ str(y[1]) + " your remaining balance is " + str (y[0]))



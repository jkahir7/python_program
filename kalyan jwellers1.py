name=input("enter your name: ")
gender=input("enter a gender m or f: ")
age=int(input("enter a age: "))

print("name is: ",name)
print("gender is: ",gender)

print("age is: ",age)
print()
print()

t_rate=0
total_amount=0
status= True
net=0

while status: 
    product=input(" enter a product name: ")
    product_gram=int(input(" enter a product gram: "))
    price_g=5752



    print("product is: ",product)
    print("product gram is: ",product_gram)
    print("price of 1 grm is 5752")


    t_rate=product_gram*price_g
    print("--------------------------------------")
    print("total  rate is :",t_rate)

    print()

    print("making charge of 1 grm is 845")
    m_charge=0
    m_charge=product_gram*845
    print("--------------------------------------")

    print(" total making charge  is",m_charge)
    print("--------------------------------------")

    total_amount=m_charge+t_rate
    print("total amount :",total_amount)


    if gender=="m" and age>65:    # calculate discount rate by gender and age
        
        if total_amount>=200000 and total_amount<=300000:
            dis=20
            print("20%_ dic")    
        
        elif total_amount>=300000 and total_amount<=500000:
            dis=30
            print("30%_ dic") 

        elif total_amount>500000:
            dis=35
            print("35%_ dic") 

    if gender=="m" and age<65:
        if total_amount>=200000 and total_amount<=300000:
            dis=10
            print("10%_ dic")    
        
        elif total_amount>=300000 and total_amount<=500000:
            dis=20
            print("20%_ dic") 

        elif total_amount>500000:
            dis=25
            print("25%_ dic") 


    if gender=="f" and age>65:
        if total_amount<=200000 and total_amount>=300000:
            dis=25
            print("25%_ dic")    
        
        elif total_amount<=300000 and total_amount>=500000:
            dis=35
            print("35%_ dic") 

        elif total_amount>500000:
            dis=40
            print("40%_ dic") 


    if gender=="f" and age>65:
        if total_amount>=200000 and total_amount<=300000:
            dis=15
            print("15%_ dic")    
        
        elif total_amount>=300000 and total_amount<=500000:
            dis=25
            print("25%_ dic") 

        elif total_amount>500000:
            dis=30
            print("30%_ dic")        

    dis_amt=0      # calculate a amount of discount
    dis_amt=(t_rate*dis)/100
    print("dis_amount is :",dis_amt)

    print("--------------------------------------")

    total_net_amount=0
    total_net_amount=total_amount-dis_amt
    print("your total amt is :",total_net_amount)         

    choice=input("do you want to add more product : press 'y' for yes and 'n' for no")
    if choice =='y' or choice == 'Y' or choice == 'yes':
        status = True
    else:
        status = False
        
        
    net+=total_net_amount   # total net amount

print("net amt:",net)
     
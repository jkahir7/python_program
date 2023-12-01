class menu:
    def display(self):
        print("------------welcome to amazing pizza and pasta pizzeria ----------------")   # menu
        print("press 1 : order menu")
        print("press 2 : exit")
        print(" ")

        choice = int(input("enter a choice : "))
        if choice == 1:
            print("""
    
            1) large pizza = 10.99 
            2) large pizza = 20.99 
            3) large pizza = 29.99 
                    
                *** Buy 4 or more pizza and get 1.5lt of soft drink free***
                    
            1) large pasta = 9.5 
            2) large pasta = 17.00 
            3) large pasta = 27.50 
                    
             *** buy 4 or more pastas and get 2 bruschetta.***
             ***Buy 4 or more pizzas and pastas and get 2 choco brownies ice cream free.
            
            """)        
            print("-------------------------------------")



            net = 0
            net_pizza = 0
            net_pasta = 0
            net_qty = 0
            soft_drink = 0
            bruschetta = 0
            ice = 0

            status = True
            while status:

                # calculation of food order and offer
                
                name1 = input("Enter your name : ")
                print("welcome,",name1)
                qty = int(input("Enter number or pizza order you want : "))
                print(" ")


                if qty == 1:
                    ans = 10.99
                    print("your pizza order amount is : ",ans)

                elif qty == 2:
                    ans = 20.99
                    print("your pizza order amount is : ",ans)

                elif qty == 3:
                    ans = 9.5
                    print("your pizza order amount is : ",ans)

                elif qty > 3:
                    ans = qty * 10.99
                    print("your pizza order amount is : ",ans)
                    print("***congratulation !! 1.5lt softdrink free***")
                    soft_drink += 1
                elif qty == 0:
                    ans = 0
                    print("your pizza amount is : ",ans)
                net_pizza+=ans   
                print(" ")

                print("  ------------------------------------------    ")


                qty1 = int(input("Enter number or pastas order you want : "))
                print(" ")

                if qty1 == 1:
                    ans1 = 9.5
                    print("your pastas order amount is : ",ans)

                elif qty1 == 2:
                    ans1 = 17.50
                    print("your pastas order amount is : ",ans1)

                elif qty1 == 3:
                    ans1 = 27.50
                    print("your pastas order amount is : ",ans1)

                elif qty1 > 3:
                    ans1 = qty1 * 9.5
                    print("your pastas order amount is : ",ans1)
                    print(" ")
                    print("***congratulation !! get 2 bruschetta free ")
                    bruschetta += 2
                elif qty1 == 0:
                    ans1 = 0
                    print("your pastas amount is : ",ans1)
                net_pasta += ans1 

                if  qty > 3 and qty1>3:
                    print("*** congratulation !!get 2 choco brownies ice cream free ***")
                    print(" ")
                    ice += 2

                a = qty + qty1  
                net_qty += a

                total_order = ans + ans1
                print("your total order is : ",total_order)
                net =net +  total_order
                print(" ")
                print(" -----------------------------------------")
                print("---> your net order amount of the day is : ",net)
                print(" ")
                que=input("want to enter order from another customer(y/n): ")
                if que == 'n':
                    status = False


            
            print(" ")
            print("     --------------- pizza and pasta bill --------------")
            print(" ")
            print(" ")
            print("payment received from pizza : ",net_pizza)
            print(" ")
            print("payment received from pastas : ",net_pasta)
            print(" ")
            print("payment received today : ",net)
            print(" ")
            print("number of pizza and pastas sold in one shift : ",net_qty)
            print(" ")
            print("number of 1.5lt soft drink bottle given : ",soft_drink)
            print(" ")
            print("number of bruschetta given : ",bruschetta)
            print(" ")
            print(" number of chocco brownies ice cream given to customer : ",ice)

            print("Bye Bye !!!")

        else:
            print("exit")
            status = False




menu = menu()

menu.display()








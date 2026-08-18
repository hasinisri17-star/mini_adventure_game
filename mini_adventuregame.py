print("=====================MINI ADVENTURE GAME=============================")
name=input("enter your nick name:")
print("Welcome",name,"!")
print("you are lost in the mysterious forest")
print("you see two path")
choice=input("right or left:").lower()
if choice=="right":
        print("you will see the river")
        choice=input("cross or follow ?")
        if choice=="cross":
            print("u will cross the river and then reach beauty island ")
            choice=input("search or leave:").lower()
            if choice=="search":
                print("you found a 🔑key")
            elif choice=="leave":
                print("u return to the river")
            else:
               print("Please choose search or leave.")
        elif choice=="follow":
            print("you will follow the river and then reach the bridge")
            print("the bridge is been danger!")
            choice=input("cross or go back? ")
            if choice=="cross":
                print("you reach the other side safe------->You Win🎉 ")
            elif choice=="go back":
                print("return to river")
            else:
              print("Please choose cross or go back.")
        else:
          print("Please choose cross or follow.")



        
elif choice=="left":
        print("you will see the broken house")
        choice=input(" red door and blue door:")
        if choice=="red door":
            print("u see the mysterious box")
            choice = input("open or leave? ").lower()
            if choice == "open":
              print("You found a magical object! ✨ You Win!")
            elif choice == "leave":
              print("You escaped safely. GAME OVER!")
        elif choice=="blue door":
              print("you find the three box")
              choice=input("box1,box2,box3:").lower()
              if choice=="box1":
                print("coins---->💎 you win")
              elif choice=="box2":
                print("boom------>you blast")
              elif choice=="box3":
                print("a key🔑------>you won")
              else:
                 print("pls choose crt.")
        else:
          print("Please choose red door or blue door.")


else:
       print("please choose right or left")
    



    
#-------------------------------------------------------------------------------
# Name: Ena Kohli
# Date: 05/31/2017
# Name of Program: Plane Crash
# Program Description: A text-based adventure game based on a plane crash
#-------------------------------------------------------------------------------

#The program welcomes the user and makes sure that the name input by the user is not a number. If it is a number, it asks the user for their name again
print("Welcome").center(100,"*")
Name =  raw_input("What is your name?")
while True:
    if Name.isnumeric():
        print("That's not a name!")
        Name =  raw_input("What is your name?")

    else:
        break

def wait_minute():
        import time
        time.sleep(1.5)

#The program greets the user with their name and introduces them to the program
wait_minute()
print("Hello " + str(Name) + ". Welcome to Plane Crash! An adventure game for you to enjoy!")
wait_minute()
print(str(Name) + ", make sure you make your decisions very wisely")
wait_minute()
print("The objective of the game is to try to get rescued and not die")
wait_minute()
print("REMEMBER! MAKE SURE TO MAKE YOUR DECISIONS VERY WISELY")
wait_minute()
print(" ")
print("Begin").center(100,"*")
print(" ")

while True:

    #A time delay has been added to make the output more neat
    def wait_minute():
        import time
        time.sleep(1.5)

    #Points and Health are being kept track of
    Points = 0
    Health = 100

    #The story starts off with you visiting Bora Bora on a private jet
    print(" ")
    print(str(Name) + ", you are on your way to beautiful Bora Bora in a private jet.")
    wait_minute()
    print("You are enjoying a nice cold drink when you hear something from the cockpit and you are not too sure what it is.")
    wait_minute()
    print("What would you like to do?")
    wait_minute()
    print(" ")
    print("1. Go check out what the noise is")
    print("2. Stay in your seat")
    print("3. Hide")
    Noise = raw_input("What would you like to do (select a number from options listed)?")

    num = False
    while num == False:
            try:
                Noise = int(Noise)
                if Noise >3 or Noise <1:
                    print ("That's an incorrect option! Try again.")
                    Noise = raw_input("What would you like to do (select a number from options listed)?")
                else:
                    num = True
            except:
                print("Invalid Input")
                Noise = raw_input("What would you like to do (select a number from options listed)?")

    #This decision leads to the user finding the pilot to be unconscious
    if Noise == 1:
        Points = Points + 3
        Health = Health - 2
        print(" ")
        wait_minute()
        print(str(Name) + ", you decided to go check what the noise was. You step into the cockpit and you realize that the pilot is no longer conscious.")
        wait_minute()
        print("You check his pulse and realize he is dead. The plane is crashing.")
        wait_minute()
        print("What do you want to do?")
        wait_minute()
        print(" ")
        print("1. Pilot the plane by yourself")
        print("2. Contact Air Control")
        print("3. Go back to your seat")
        PlaneCockpit = raw_input("What is your next step (select a number from the options available)?")

        num = False
        while num == False:
                try:
                    PlaneCockpit = int(PlaneCockpit)
                    if PlaneCockpit >3 or PlaneCockpit <1:
                        print ("That's an incorrect option! Try again.")
                        PlaneCockpit = raw_input("What is your next step (select a number from the options available)?")
                    else:
                        num = True
                except:
                    print("Invalid Input")
                    PlaneCockpit = raw_input("What is your next step (select a number from the options available)?")

        #The user decides to pilot the plane by themselves which leads to the plane crashing
        if PlaneCockpit == 1:
            Points = Points - 1
            Health = Health - 3
            print(" ")
            wait_minute()
            print(str(Name) + "! You decide to pilot the plane by yourself??? BAD OPTION!!!")
            wait_minute()
            print("You do not know how to and you click a bright red button. The plane suddenly starts to lose altitude and you crash.")
            wait_minute()
            print("On the way down, you lose consciousness. When you wake up, you look around and realize that the plane has crashed and you are at a deserted island.")
            wait_minute()
            print("What would you like to do?")
            wait_minute()
            print(" ")
            print("1. Look around the island")
            print("2. Stay and try to call for help using the plane system")
            print("3. Stay and make a fire to keep you warm")
            CrashRed = raw_input("What is your next step (select a number from the options available)?")

            num = False
            while num == False:
                    try:
                        CrashRed = int(CrashRed)
                        if CrashRed >3 or CrashRed <1:
                            print ("That's an incorrect option! Try again.")
                            CrashRed = raw_input("What would you like to do (select a number from options listed)?")
                        else:
                            num = True
                    except:
                        print("Invalid Input")
                        CrashRed = raw_input("What would you like to do (select a number from options listed)?")

            #The user decides to look around the island and comes face to face with a black bear
            if CrashRed == 1:
                Points = Points + 2
                Health = Health - 3
                print(" ")
                wait_minute()
                print(str(Name) + "! You decide to look around the island. After 1 hour of walking, you hear something in the woods.")
                wait_minute()
                print("You turn around and see that it is a huge BLACK BEAR! You scream and catch the attention of the bear.")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Run away from the bear")
                print("2. Stay where you are")
                print("3. Climb up a tree")
                Bear = raw_input("What is your next step (select a number from the options available)?")

                num = False
                while num == False:
                        try:
                            Bear = int(Bear)
                            if Bear >3 or Bear <1:
                                print ("That's an incorrect option! Try again.")
                                Bear = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Bear = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to run away from the bear which results in their death
                if Bear == 1:
                    Points = Points - 1
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + "! You decide to run away from the bear!!! Bad decision!")
                    wait_minute()
                    print("You start running away and trip over a rock. The bear is very angry and comes right toward you.")
                    wait_minute()
                    print(str(Name) + " , you are unable to get up and the bear is running fast towards you...YOU DIE!!! GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + " , you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to stay where they are which leads to the bear leaving
                elif Bear == 2:
                    Points = Points + 3
                    Health = Health - 1
                    print(" ")
                    wait_minute()
                    print("You decide to stay right where you are and not move. The bear smells your scent but does not move.")
                    wait_minute()
                    print("The bear goes back into the woods and you are left alone. You breathe a sigh of relief. You decide to go back to where the plane is.")
                    wait_minute()
                    print("You turn around but realize that you don't remember which way you came from.")
                    wait_minute()
                    print("Which way do you want to go?")
                    wait_minute()
                    print(" ")
                    print("1. Straight")
                    print("2. Right")
                    print("3. Left")
                    Direction = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Direction = int(Direction)
                                if Direction >3 or Direction <1:
                                    print ("That's an incorrect option! Try again.")
                                    Direction = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Direction = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to go straight which leads to them hearing a noise
                    if Direction == 1:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to go straight. You walk for 2 hours and realize that this was not the correct way back.")
                        wait_minute()
                        print("You seem to be lost even more now. Suddenly, you hear a crunching noise behind you.")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Turn around to see what was making the sound")
                        print("2. Run away from the sound")
                        print("3. Keep walking in the direction you were walking in")
                        Sound = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Sound = int(Sound)
                                    if Sound >3 or Sound <1:
                                        print ("That's an incorrect option! Try again.")
                                        Sound = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Sound = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to see what the noise was behind them. They see an old man
                        if Sound == 1:
                            Points = Points - 1
                            Health = Health - 1
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to see what the noise behind you was. You turn around and see that it is a short, old man.")
                            wait_minute()
                            print("He says he will take you to his house.")
                            wait_minute()
                            print("What would you like to do?")
                            wait_minute()
                            print(" ")
                            print("1. Ignore the man and try to go back to the plane")
                            print("2. Go with the man")
                            print("3. Run away in the other direction")
                            Man = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Man = int(Man)
                                        if Man >3 or Man <1:
                                            print ("That's an incorrect option! Try again.")
                                            Man = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Man = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to walk away from the old man which results in them being kidnapped by the man
                            if Man == 1:
                                Points = Points - 1
                                Health = Health - 3
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to ignore the man and continue to walk. As you continue walking, you realize that someone is following you.")
                                wait_minute()
                                print("You turn around and you are hit with a baseball bat! You lose consciousness.")
                                wait_minute()
                                print("When you wake up, you are tied to a chair. You are kidnapped! The old man comes into the room and tells you that he wants a friend.")
                                wait_minute()
                                print("What do you do?")
                                wait_minute()
                                print(" ")
                                print("1. Start talking to him")
                                print("2. Attempt to fight")
                                print("3. Run away")
                                Kidnap = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            Kidnap = int(Kidnap)
                                            if Kidnap >3 or Kidnap <1:
                                                print ("That's an incorrect option! Try again.")
                                                Kidnap = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            Kidnap = raw_input("What would you like to do (select a number from options listed)?")

                                #The user starts to talk to the man which causes them to become friends with the man
                                if Kidnap == 1:
                                    Points = Points - 1
                                    Health = Health - 3
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to start talking to the man. His ideals and thoughts start sinking in with you.")
                                    wait_minute()
                                    print("YOU BECOME FRIENDS WITH A PSYCHOPATH!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you have become friends with a psychopath in the forest. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to fight the man which eventually leads to their death
                                elif Kidnap == 2:
                                    Points = Points - 1
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to fight the man. As you start to punch the man, he pulls out a knife and stabs you once in the neck.")
                                    wait_minute()
                                    print("As you bleed to death, you look in the corner of the room. The man is crying and saying that all he wanted was a friend. GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you bleed to death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to run away which eventually leads to their death in different ways using the randon integer function
                                else:
                                    Points = Points - 1
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    from random import randint
                                    Run = randint(1,3)
                                    if Run == 1:
                                        print("You decide to run away. As you run away, you feel a piercing pain to the back of your head.")
                                        wait_minute()
                                        print("You touch the back of your head and see dark red. You turn around and see the old man threw a knife at the back of your head.")
                                        wait_minute()
                                        print("YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you bleed to death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                    elif Run == 2:
                                        print("You decide to run away. As you run away, you see an opening, you run threw that opening and you see yourself falling")
                                        wait_minute()
                                        print(str(Name) + ", you fall off a cliff. YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you fall to your death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                    else:
                                        print("You decide to run away. As you run away, you look up and see a snake hanging from the tree.")
                                        wait_minute()
                                        print("You can't slow down so you keep running. The snake bites you. You run away and you are back at your plane but as soon as you stop running, you die.")
                                        wait_minute()
                                        print("The snake was poisonous! YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you die due to poison. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to go with the old man which leads to them being stuck in the house
                            elif Man == 2:
                                Points = Points - 1
                                Health = Health - 2
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to go with the man. The old man feeds you, gives you a bed to sleep in and always watches you.")
                                wait_minute()
                                print("After 1 day with the man, you want to leave. As you go towards the door, you try to open the door but see that it is locked.")
                                wait_minute()
                                print("You ask the man and he leads you back to your bed. You know something is wrong. The next day this happens again.")
                                wait_minute()
                                print("For a week, the man always leads you away from the door and you follow. One night, you wake up and see that the door is unlocked.")
                                wait_minute()
                                print("What do you do?")
                                wait_minute()
                                print(" ")
                                print("1. Go see what the man is doing")
                                print("2. Try to sneak out")
                                print("3. Go back to sleep")
                                CreepyMan = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            CreepyMan = int(CreepyMan)
                                            if CreepyMan >3 or CreepyMan <1:
                                                print ("That's an incorrect option! Try again.")
                                                CreepyMan = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            CreepyMan = raw_input("What would you like to do (select a number from options listed)?")

                                #The user decides to go see what the man is doing which eventually leads to the user being rescued
                                if CreepyMan == 1:
                                    Points = Points + 5
                                    Health = Health - 3
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to go see what the man is doing. As you approach his room, you constantly keep hearing this sound from outside.")
                                    wait_minute()
                                    print("You step into his room and see that he is not in there.")
                                    wait_minute()
                                    print("You walk out and hear the sound again.")
                                    wait_minute()
                                    print("You walk outside and see the old man making weird symbols on a tree. He looks at you and says that he wished you never came out.")
                                    wait_minute()
                                    print("As soon as you hear this, you start to run as fast as you can.")
                                    wait_minute()
                                    print("You run for several hours and realize that you have made it back to the plane crash site!")
                                    wait_minute()
                                    print("There is a helicopter waiting for you! You meet the pilot and he flies you home safely! GAME OVER!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Fortunately " + str(Name) + " , you survived the plane crash! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to try to sneak out from the house which eventually leads to their death
                                elif CreepyMan == 2:
                                    Points = Points - 1
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to try to sneak out of the house. As you sneak out, you notice strange markings on the trees surrounding the house.")
                                    wait_minute()
                                    print("You walk away quietly but hear a sound behind you.")
                                    wait_minute()
                                    print("The old man is standing behind the tree staring directly at you, He says that he wished you never came out. You don't know what to do so you stand still.")
                                    wait_minute()
                                    print("The man stabs you 3 times and you bleed to death!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you bled to death! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to go back to sleep which leads to them living with the old man
                                else:
                                    Points = Points + 5
                                    Health = Health - 1
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to go back to sleep meaning that you will stay with the old man for all of eternity. Over time, your ideals and thoughts sink in with the old man.")
                                    wait_minute()
                                    print("You become his therapist and teach him the true meaning of life. You and the old man stay together in the forest. GAME OVER!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Fortunately " + str(Name) + " , you changed the old man! Well done! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to run away in the other direction which leads to their death
                            else:
                                Points = Points - 1
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to run away in the other direction. You are running fast and there is a large rock in front of you!")
                                wait_minute()
                                print("You see it and are unable to avoid it. You trip and hit your head against the rock. YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to run away from the sound which leads to their death
                        elif Sound == 2:
                            Points = Points - 1
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to run away from the sound. You run away and you trip over a branch. You fall and realize that you tripped over a cliff! YOU DIE!!! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + " , you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to keep walking in the direction that they were walking in which leads to them finding a cave
                        else:
                            Points = Points - 1
                            Health = Health - 3
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to keep walking in the direction you were walking in. You continue to walk and you see an opening in the forest! You walk through the opening and see a cave.")
                            wait_minute()
                            print("What would you like to do?")
                            wait_minute()
                            print(" ")
                            print("1. Go into the cave")
                            print("2. Turn around")
                            print("3. Keep walking in the same direction")
                            Cave = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Cave = int(Cave)
                                        if Cave >3 or Cave <1:
                                            print ("That's an incorrect option! Try again.")
                                            Cave = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Cave = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to go into the cave which leads to them finding lots of lost treasure
                            if Cave == 1:
                                Points = Points + 4
                                Health = Health - 1
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to go into the cave. You have found lots of missing treasure that was buried by pirates 100 years ago! AWESOME!!!")
                                wait_minute()
                                print("You see a lot of treasure but are unsure how to carry all of it.")
                                wait_minute()
                                print("What would you like to do?")
                                wait_minute()
                                print(" ")
                                print("1. Bring all of the treasure with you ")
                                print("2. Bring some of the treasure with you")
                                print("3. Leave all of the treasure")
                                Treasure = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            Treasure = int(Treasure)
                                            if Treasure >3 or Treasure <1:
                                                print ("That's an incorrect option! Try again.")
                                                Treasure = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            Treasure = raw_input("What would you like to do (select a number from options listed)?")

                                #The user decides to bring all of the treasure with them which leads to a large chest almost falling on them
                                if Treasure == 1:
                                    Points = Points - 1
                                    Health = Health - 3
                                    print(" ")
                                    wait_minute()
                                    print("You decide to try to bring all of the treasure with you. As you try to carry as much as you can in your hands, you hear a shaking noise coming from above your head.")
                                    wait_minute()
                                    print("You look up and it looks like a gigantic treasure chest is going to fall on top of you!")
                                    wait_minute()
                                    print("What would you like to do?")
                                    wait_minute()
                                    print(" ")
                                    print("1. Leave the treasure and run away ")
                                    print("2. Continue to carry the treasure with you")
                                    print("3. Stay where you are")
                                    TreasureChest = raw_input("What is your next step (select a number from the options available)?")

                                    num = False
                                    while num == False:
                                            try:
                                                TreasureChest = int(TreasureChest)
                                                if TreasureChest >3 or TreasureChest <1:
                                                    print ("That's an incorrect option! Try again.")
                                                    TreasureChest = raw_input("What would you like to do (select a number from options listed)?")
                                                else:
                                                    num = True
                                            except:
                                                print("Invalid Input")
                                                TreasureChest = raw_input("What would you like to do (select a number from options listed)?")

                                    #The user decides to leave the treasure and get out of the cave which leads to their rescue
                                    if TreasureChest == 1:
                                        Points = Points + 4
                                        Health = Health - 3
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you decide to leave the treasure and get out of the cave. You make it out of the cave but unfortunately you are still lost.")
                                        wait_minute()
                                        print("You walk for more than 2 hours until you see the water! You see the plane and a lifeguard is there waitng for you! You are saved! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Fortunately " + str(Name) + " , you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to pick up the treasure which eventually leads to their death
                                    elif TreasureChest == 2:
                                        Points = Points - 1
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you continue to pick up the treasure. As you do so, the treasure chest seems to be falling.")
                                        wait_minute()
                                        print("You think that you can carry one more gem but unfortunately, the treasure chest falls. YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you get crushed by the treasure chest. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user is in shock and is not moving which leads to their death
                                    else:
                                        Points = Points - 1
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you are in shock and are unable to move! The treasure chest keeps slipping and slipping!")
                                        wait_minute()
                                        print("Unfortunately you are too scared to move so the treasure chest falls on top of you! YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you get crushed by the treasure chest. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to try to bring some of the treasure with them which leads to them being trapped in the cave
                                elif Treasure == 2:
                                    Points = Points + 2
                                    Health = Health - 2
                                    print(" ")
                                    wait_minute()
                                    print("You decide to try to bring some of the treasure with you. Once you have gotten as much treasure as you can hold, you decide to leave the cave with whatever you have left.")
                                    wait_minute()
                                    print("As you are about to leave, you notice a beautiful, shining, green emerald. You decide to go back for it.")
                                    wait_minute()
                                    print("You pick up the diamond and suddenly a huge door closes the cave and you are trapped inside! You try to get out when you see a long wire-like object hanging from above.")
                                    wait_minute()
                                    print("What would you like to do?")
                                    wait_minute()
                                    print(" ")
                                    print("1. Grab it ")
                                    print("2. Don't touch it")
                                    print("3. Try to look for another way")
                                    Wire = raw_input("What is your next step (select a number from the options available)?")

                                    num = False
                                    while num == False:
                                            try:
                                                Wire = int(Wire)
                                                if Wire >3 or Wire <1:
                                                    print ("That's an incorrect option! Try again.")
                                                    Wire = raw_input("What would you like to do (select a number from options listed)?")
                                                else:
                                                    num = True
                                            except:
                                                print("Invalid Input")
                                                Wire = raw_input("What would you like to do (select a number from options listed)?")

                                    #The user decides to grab the object which leads to their death
                                    if Wire == 1:
                                        Points = Points - 3
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you decide to grab the wire-like object to try to get out of the cave. You touch the object and realize that it is a poisonous snake!")
                                        wait_minute()
                                        print("The snake, feeling threatened, bites you and you are killed instantly. GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you get bitten by a snake. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to grab the object which leads to their death
                                    elif Wire == 2:
                                        Points = Points - 3
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you decide to not grab the wire-like object. As you are looking to find something else that can help you escape, you seem to be losing consciousness!")
                                        wait_minute()
                                        print("You are suffocating to death! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you suffocate to death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to try to look for another way out which leads to their death in various ways using the random integer function
                                    else:
                                        Points = Points - 3
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        from random import randint
                                        Run = randint(1,3)
                                        if Run == 1:
                                            print("You decide to try to look for another way to get out. As you are doing so, you start to feel tired and you are having trouble breathing!")
                                            wait_minute()
                                            print("You are suffocating in the cave! YOU DIE!!! GAME OVER!!!")
                                            wait_minute()
                                            print(" ")
                                            print("Good game! Unfortunately " + str(Name) + " , you suffocate to death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                        elif Run == 2:
                                            print("You decide to look for something that can get you out. You see the green emerald again. You think that if you touch it, the cave may open.")
                                            wait_minute()
                                            print("Unfortunately, nothing happens and you suffocate. GAME OVER!!!")
                                            wait_minute()
                                            print(" ")
                                            print("Good game! Unfortunately " + str(Name) + " , you suffocate to your death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                        else:
                                            print("You decide to look for something that may help you get out. You see a switch and you think it is a switch that can open the door!")
                                            wait_minute()
                                            print("You click the switch and nothing happens. You click it again and still nothing happens.")
                                            wait_minute()
                                            print("Suddenly, you hear a loud noise. You look up and see large rocks falling! The switch was a trap made for intruders by the pirates!")
                                            wait_minute()
                                            print("The rocks fall on you. YOU DIE!!! GAME OVER!!!")
                                            wait_minute()
                                            print(" ")
                                            print("Good game! Unfortunately " + str(Name) + " ,falling rocks killed you. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to leave the treasure which leads to their death
                                else:
                                    Points = Points - 1
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to leave the treasure. As you are leaving the cave, you notice a really pretty jeweled crown.")
                                    wait_minute()
                                    print("You decide to take the beautiful crown. Suddenly, you hear a shaking noise and you look up to see a large treasure chest that looks like it is about to fall!")
                                    wait_minute()
                                    print("You try to run but a necklace has caught your leg.")
                                    wait_minute()
                                    print("The treasure chest falls on you and crushes you. YOU DIE!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you got crushed by a treasure chest. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to turn around and this leads to their death
                            elif Cave == 2:
                                Points = Points - 1
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to turn around. Right behind you, you see a ferocious lion! He looks hungry. The lion slowly starts to approach you.")
                                wait_minute()
                                print("You stay where you are and the lion comes and kills you. YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to keep walking which leads to the user being saved
                            else:
                                Points = Points + 2
                                Health = Health - 2
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to keep walking. As you continue to walk in the same direction, you notice another opening through some bushes. You look through the opening and see the plane!")
                                wait_minute()
                                print("You run back and notice a speed boat coming your way! You get on the speed boat and make it back to your home! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Fortunately " + str(Name) + " , you survived the plane crash and made it back home! Yay! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to turn right which leads to the user seeing a helicopter
                    elif Direction == 2:
                        Points = Points + 2
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to go turn right. Good job! You walk for another hour and make it to a clear spot in the forest.")
                        wait_minute()
                        print("You look up and realize that a helicopter is coming in your direction!")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Hide")
                        print("2. Scream and shout from inside the forest")
                        print("3. Try to make a fire as a signal")
                        Helicopter = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Helicopter = int(Helicopter)
                                    if Helicopter >3 or Helicopter <1:
                                        print ("That's an incorrect option! Try again.")
                                        Helicopter = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Helicopter = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to hide from the helicopter which leads to the user discovering the island is a large prison
                        if Helicopter == 1:
                            Points = Points + 2
                            Health = Health - 1
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to hide from the helicopter. As you run behind a bush in the forest, you see a man step off from the helicopter. He is in no condition to move as he looks very ill.")
                            wait_minute()
                            print("He is also in handcuffs. Another man steps down from the helicopter and has a police uniform on. You overhear someone telling the man in the uniform that the criminal needs to be taken to the prison.")
                            wait_minute()
                            print("You realize that this island holds prisoners and criminals from all over the world! You move your foot and you step on a branch. The man hears you and starts walking towards you.")
                            wait_minute()
                            print("What would you do?")
                            wait_minute()
                            print(" ")
                            print("1. Try to sneak away")
                            print("2. Go talk to the police officer")
                            print("3. Stay where you are")
                            Police = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Police = int(Police)
                                        if Police >3 or Police <1:
                                            print ("That's an incorrect option! Try again.")
                                            Police = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Police = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to sneak away which leads to people chasing after them
                            if Police == 1:
                                Points = Points + 2
                                Health = Health - 1
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to sneak away. As you do so, the man starts to walk slowly towards you. You run away but the man is behind you.")
                                wait_minute()
                                print("You keep walking fast and have lost the man but you are unsure where you are. Suddenly, you hear more helicopters in the air and shouting voices. The voices are getting closer.")
                                wait_minute()
                                print("What would you do?")
                                wait_minute()
                                print(" ")
                                print("1. Stay where you are")
                                print("2. Run away")
                                print("3. Go hide")
                                Shouting = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            Shouting = int(Shouting)
                                            if Shouting >3 or Shouting <1:
                                                print ("That's an incorrect option! Try again.")
                                                Shouting = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            Shouting = raw_input("What would you like to do (select a number from options listed)?")

                                #The user decides to stay right where they are which leads to their death
                                if Shouting == 1:
                                    Points = Points - 1
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to stay right where you are. The shouting gets closer and closer. 10 people with guns come towards you and you are shot right then and there.")
                                    wait_minute()
                                    print("The guards thought you were an escapee! You shouldn't have stayed! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to run away which leads to you finding out the island is a prison
                                elif Shouting == 2:
                                    Points = Points + 2
                                    Health = Health - 1
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + " , you decide to run away. As you do so, you hear the shouting get quieter and quieter! Good choice! You continue to walk.")
                                    wait_minute()
                                    print("You know that this is an island where the world's most dangerous criminals are held as prisoners. You continue to walk when you see your plane!")
                                    wait_minute()
                                    print("You look through an opening through a bush and see the guards inspecting the plane.")
                                    wait_minute()
                                    print("What would you do?")
                                    wait_minute()
                                    print(" ")
                                    print("1. Stay where you are")
                                    print("2. Go to them")
                                    print("3. Run away")
                                    Guards = raw_input("What is your next step (select a number from the options available)?")

                                    num = False
                                    while num == False:
                                            try:
                                                Guards = int(Guards)
                                                if Guards >3 or Guards <1:
                                                    print ("That's an incorrect option! Try again.")
                                                    Guards = raw_input("What would you like to do (select a number from options listed)?")
                                                else:
                                                    num = True
                                            except:
                                                print("Invalid Input")
                                                Guards = raw_input("What would you like to do (select a number from options listed)?")

                                    #The user decides to stay where there which leads to their death
                                    if Guards == 1:
                                        Points = Points - 1
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you decide to stay where you are and look to see what the guards do. You walk and you make eye contact with one of the guards!")
                                        wait_minute()
                                        print("They see you and shoot at you! YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to go to the guards which leads to them being saved
                                    elif Guards == 2:
                                        Points = Points + 2
                                        Health = Health - 2
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you decide to go to the guards. They see you but do not shoot. They realize that you are the plane crash survivor and decide to help you.")
                                        wait_minute()
                                        print("One of the guards takes you on the helicopter and you are back at home!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Fortunately " + str(Name) + " , you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to run away in the other direction
                                    else:
                                        Points = Points - 1
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + ", you decide to run away in the other direction. As you are running away, you hear a noise behind you. You turn around and it's a bear!")
                                        wait_minute()
                                        print("The bear roars and comes after you. You are eaten by the bear! YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you get eaten by a bear! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to hide which leads to their death
                                else:
                                    Points = Points - 1
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to go hide. As you are finding a good spot, you notice a spot behind a bush. You hide behind a bush when suddenly you fall! It was a trap!")
                                    wait_minute()
                                    print("You break your neck. YOU DIE!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you fall and break your neck! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to go to the police man which leads to you being saved
                            elif Police == 2:
                                Points = Points + 5
                                Health = Health - 2
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to go talk to the police man. You tell him that you are not a prisoner and were in a plane crash.")
                                wait_minute()
                                print("He doesn't believe you at first but you tell him that you will take him to the plane crash site. You, the prisoner and the police officer walk for an hour and make it back to the plane crash site!")
                                wait_minute()
                                print("The police officer believes you and decides to help you and take you back! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Fortunately " + str(Name) + " , you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to stay right where they were which leads to their death
                            else:
                                Points = Points - 1
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to stay right where you are. The man comes to you and points a gun to you. You tell him your story but he doesn't believe you.")
                                wait_minute()
                                print("He thinks you are a prisoner!!! He shoots you! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to scream and shout which leads to the user being stuck in jail
                        elif Helicopter == 2:
                            Points = Points - 1
                            Health = Health - 4
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to scream and shout. The helicopter starts to land and a man in a uniform gets out. Suddenly, he knocks you out!")
                            wait_minute()
                            print("You wake up and realize you are in handcuffs! You ask the man in the uniform why you are in handcuffs and he says that he knows that you were trying to escape from prison!")
                            wait_minute()
                            print("You realize that this island holds the most dangerous criminals from all over the world! You keep telling the man that you were stranded on the island but he doesn't believe you.")
                            wait_minute()
                            print("You reach the prison with the man and he locks you up in a cell.")
                            wait_minute()
                            print("What would you do?")
                            wait_minute()
                            print(" ")
                            print("1. Try to escape")
                            print("2. Stay where you are")
                            print("3. Ask for help from another prisoner")
                            Prison = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Prison = int(Prison)
                                        if Prison >3 or Prison <1:
                                            print ("That's an incorrect option! Try again.")
                                            Prison = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Prison = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to try to escape from the cell which leads them to a door
                            if Prison == 1:
                                Points = Points + 2
                                Health = Health - 4
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to try to escape from the cell. You hear a voice and notice the guard with the keys to your cell. He is slowly falling asleep.")
                                wait_minute()
                                print("He is right in front of you and you decide to try to steal the keys. You reach out and grab the keys slowly and carfeully. You unlock the cell door but as you do so, a siren wails!")
                                wait_minute()
                                print("You start to run! You run and make it to a door.")
                                wait_minute()
                                print("What would you do?")
                                wait_minute()
                                print(" ")
                                print("1. Open the door")
                                print("2. Try to find another way out")
                                print("3. Turn back around and surrender")
                                Escape = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            Escape = int(Escape)
                                            if Escape >3 or Escape <1:
                                                print ("That's an incorrect option! Try again.")
                                                Escape = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            Escape = raw_input("What would you like to do (select a number from options listed)?")

                                #The user decides to open the door which leads to them being stuck in prison
                                if Escape == 1:
                                    Points = Points - 1
                                    Health = Health - 2
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to open the door. You open the door and on the other side is a group of guards waiting for you! They catch you and you are taken back to your cell!")
                                    wait_minute()
                                    print("You stay there for your entire life counting the days. GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you are stuck in prison! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to try to find another way out which leads to their death
                                elif Escape == 2:
                                    Points = Points - 2
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to try to find another way out. You turn right and you start to run. Suddenly, you hear a group of guards approaching you.")
                                    wait_minute()
                                    print("You start to run in the other direction but you hear guards coming from there too!")
                                    wait_minute()
                                    print("You hear one of the guards say to another that they have been given an order to shoot you on sight! You are stuck.")
                                    wait_minute()
                                    print("One of the guards sees you and you are shot multiple times. YOU DIE!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you are shot trying to escape! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to turn around and surrender and they are stuck in jail
                                else:
                                    Points = Points + 1
                                    Health = Health - 2
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + ", you decide to turn around and surrender. You walk back to your cell and a guard is screaming.")
                                    wait_minute()
                                    print("The guards shuts you in your cell and you remain there for all of eternity. GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you are surrender and are stuck in jail! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to stay right where they are which leads to them being stuck in prison
                            elif Prison == 2:
                                Points = Points - 2
                                Health = Health - 2
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to stay right where you are. Every day, you keep thinking to yourself that you wished you tried to escape.")
                                wait_minute()
                                print("You are stuck in this prison with high security for all your life! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " ,you are stuck in prison! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user deecides to take help from a few other prisoners to try to escape which eventually leads to them being stuck in jail
                            else:
                                Points = Points + 2
                                Health = Health - 2
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you as another few prisoners if they would help you escape. You plan for days on how to escape from prison.")
                                wait_minute()
                                print("You decide to try to dig your way out. Day by day, you and the prisoners slowly and carefully try to dig.")
                                wait_minute()
                                print("After a few months, you make a hole large enough to escape! One of the other prisoners decides to go first.")
                                wait_minute()
                                print("The other prisoner leaves and as soon as he leaves, one of the guards catches you!")
                                wait_minute()
                                print("You and the other prisoners with you, are sent back to your cells for all of you life. GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " ,you are stuck in prison! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to start a fire which leads to their death
                        else:
                            Points = Points - 1
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to start a fire. As you get the things needed from the woods, you notice the helicopter slowly landing.")
                            wait_minute()
                            print("A man with a uniform steps off the helicopter and tells you to go back to prison with him. You are confused and he tells you to go back to prison.")
                            wait_minute()
                            print("You realize that you are stuck on an island with prisoners! You say no to the man. He points a gun at you and you hear a gunshot. You are shot! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to turn left which leads to them finding a berry bush
                    else:
                        Points = Points + 1
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to go turn left. You continue to walk for 3 hours and realize that you are far away from your camp.")
                        wait_minute()
                        print("You walk for another few kilometers and find a berry bush.")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Eat the berries")
                        print("2. Don't eat the berries")
                        print("3. Take the berries with you")
                        Berries = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Berries = int(Berries)
                                    if Berries >3 or Berries <1:
                                        print ("That's an incorrect option! Try again.")
                                        Berries = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Berries = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to eat the berries which leads to their death
                        if Berries == 1:
                            Points = Points - 3
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to eat the berries! Bad choice! You eat one and you start to slowly lose consciousness! You realize that the berries are poisonous!")
                            wait_minute()
                            print("You lose consciousness and die! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + " , you eat poisonous berries! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to not eat the berries which leads them to a hunter
                        elif Berries == 2:
                            Points = Points + 3
                            Health = Health - 1
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to not eat the berries. Smart move! You see a squirrel come and eat a berry and die.")
                            wait_minute()
                            print("You realize that the berries were poisonous. You didn't eat the berries and are safe, but are very hungry. You start to walk.")
                            wait_minute()
                            print("After an hour of walking, you see someone behind a bush. You walk up to them and it is a hunter! You think you are saved.")
                            wait_minute()
                            print("The hunter is shocked to see you but you tell him your story, and ask him for food. He gives you food and offers to take you to his house.")
                            wait_minute()
                            print("What would you do?")
                            wait_minute()
                            print(" ")
                            print("1. Go with him")
                            print("2. Eat the food and leave")
                            print("3. Run away")
                            Hunter = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Hunter = int(Hunter)
                                        if Hunter >3 or Hunter <1:
                                            print ("That's an incorrect option! Try again.")
                                            Hunter = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Hunter = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to go with the hunter which leads to them smelling something weird
                            if Hunter == 1:
                                Points = Points + 2
                                Health = Health - 1
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to go with the hunter to his house. You walk in and you smell something weird.")
                                wait_minute()
                                print("You ask him what the smell is and he changes the topic.")
                                wait_minute()
                                print("He takes you to your room and tells you to not go into the room next door. You are suspicious.")
                                wait_minute()
                                print("When the hunter goes out to get some food, you decide to go into the room.")
                                wait_minute()
                                print("You open the door and the smell is unbearable. You close the door.")
                                wait_minute()
                                print("What would you like to do?")
                                wait_minute()
                                print(" ")
                                print("1. Go back to your room")
                                print("2. Step into the room")
                                print("3. Try to escape")
                                Smell = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            Smell = int(Smell)
                                            if Smell >3 or Smell <1:
                                                print ("That's an incorrect option! Try again.")
                                                Smell = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            Smell = raw_input("What would you like to do (select a number from options listed)?")

                                #The user decides to go to the room which leads to death
                                if Smell == 1:
                                    Points = Points - 3
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + " , you decide to go back to your room. As you are backing out of the room, you bump into something.")
                                    wait_minute()
                                    print("You turn around and see the hunter! He shoots you! As you fall to the ground, he tells you to die in suspense! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you die and you don't know why! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to step back into the room which leads to them finding out the truth about the hunter
                                elif Smell == 2:
                                    Points = Points + 2
                                    Health = Health - 1
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + " , you decide to step back into the room. The smell hits you again and you cover your nose.")
                                    wait_minute()
                                    print("You look around and you see that the walls are red and there are fake skeletons hanging from the ceiling.")
                                    wait_minute()
                                    print("Except, the wall colour isn't just red, it's blood, and the skeletons aren't fake, they are human skulls.")
                                    wait_minute()
                                    print("You realize that this hunter is a killer! You walk up to one of the walls and you see a piece of paper.")
                                    wait_minute()
                                    print("You read the paper and it says that this man is on the most wanted list.")
                                    wait_minute()
                                    print("He kidnaps his victims, makes them like him and then kills them in the most brutal way.")
                                    wait_minute()
                                    print("What would you like to do?")
                                    wait_minute()
                                    print(" ")
                                    print("1. Get out of the room")
                                    print("2. Stay in the room and try to find out more")
                                    print("3. Try to escape")
                                    Killer = raw_input("What is your next step (select a number from the options available)?")

                                    num = False
                                    while num == False:
                                            try:
                                                Killer = int(Killer)
                                                if Killer >3 or Killer <1:
                                                    print ("That's an incorrect option! Try again.")
                                                    Killer = raw_input("What would you like to do (select a number from options listed)?")
                                                else:
                                                    num = True
                                            except:
                                                print("Invalid Input")
                                                Killer = raw_input("What would you like to do (select a number from options listed)?")

                                    #The user decides to get out of the room which leads the user's death
                                    if Killer == 1:
                                        Points = Points - 3
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + " , you decide to get out of the room! You try to open the door but it's stuck! You try to open it but are unable to.")
                                        wait_minute()
                                        print("You wait for the hunter to return and he sees you are stuck in there. He opens the door and shoots you in the forehead. GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to stay in the room which leads to death
                                    elif Killer == 2:
                                        Points = Points - 3
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        print(str(Name) + " , you decide to stay in the room! You find more articles on this man but nothing that can help you. Suddenly, you hear the door open and it's the hunter!")
                                        wait_minute()
                                        print("He pulls out his gun and shoots you! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                    #The user decides to escape which leads to death in different ways using the random integer function
                                    else:
                                        Points = Points - 3
                                        Health = Health * 0
                                        print(" ")
                                        wait_minute()
                                        from random import randint
                                        Dice = randint(1,3)
                                        if Dice == 1:
                                                print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                                wait_minute()
                                                print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                                wait_minute()
                                                print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                                wait_minute()
                                                print("You don't see a way to escape and so you have to roll. You roll a 3! You are burned alive! YOU DIE!!! GAME OVER!!!")
                                                wait_minute()
                                                print(" ")
                                                print("Good game! Unfortunately " + str(Name) + " , you are burned alive. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                        elif Dice == 2:
                                                print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                                wait_minute()
                                                print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                                wait_minute()
                                                print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                                wait_minute()
                                                print("You roll a 6. You are thrown off a cliff! GAME OVER!!!")
                                                wait_minute()
                                                print(" ")
                                                print("Good game! Unfortunately " + str(Name) + " , you are thrown off a cliff. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                        else:
                                                print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                                wait_minute()
                                                print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                                wait_minute()
                                                print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                                wait_minute()
                                                print("You roll a 1. You are shot in the head! YOU DIE!!! GAME OVER!!!")
                                                wait_minute()
                                                print(" ")
                                                print("Good game! Unfortunately " + str(Name) + " , you are shot in the head. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to escape which leads to death in different ways using the random integer function
                                else:
                                    Points = Points - 3
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    from random import randint
                                    Kill = randint(1,3)
                                    if Kill == 1:
                                            print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                            wait_minute()
                                            print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                            wait_minute()
                                            print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                            wait_minute()
                                            print("You don't see a way to escape and so you have to roll. You roll a 3! You are burned alive! YOU DIE!!! GAME OVER!!!")
                                            wait_minute()
                                            print(" ")
                                            print("Good game! Unfortunately " + str(Name) + " , you are burned alive. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                    elif Kill == 2:
                                            print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                            wait_minute()
                                            print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                            wait_minute()
                                            print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff. You roll a 6. You are thrown off a cliff! GAME OVER!!!")
                                            wait_minute()
                                            print(" ")
                                            print("Good game! Unfortunately " + str(Name) + " , you are thrown off a cliff. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                    else:
                                            print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                            wait_minute()
                                            print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                            wait_minute()
                                            print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff. You roll a 1. You are shot in the head! YOU DIE!!! GAME OVER!!!")
                                            wait_minute()
                                            print(" ")
                                            print("Good game! Unfortunately " + str(Name) + " , you are shot in the head. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to eat the food and leave which eventually leads to death
                            elif Hunter == 2:
                                Points = Points - 3
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to eat the food and politely tell the man that you want to leave.")
                                wait_minute()
                                print("He gives you a sly smile and tells you that you cannot leave. You are confused when suddenly the hunter shoots you!")
                                wait_minute()
                                print("As you are dying, you hear the man say that this could have gone much more easily. GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to run away which eventually leads to death
                            else:
                                Points = Points - 3
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to run away. As you are running away, you turn around and see the hunter gives you a sly smile and tells you that you cannot run away.")
                                wait_minute()
                                print("You stop and turn around.")
                                wait_minute()
                                print("You are confused when suddenly the hunter shoots you! As you are dying, you hear the man say that this could have gone much more easily. GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to take the berries with them which leads to them being saved
                        else:
                            Points = Points - 2
                            Health = Health - 2
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to take the berries with you. You see a squirrel come and eat a berry and die.")
                            wait_minute()
                            print("You realize that the berries were poisonous. You leave the berries there.")
                            wait_minute()
                            print("You didn't eat the berries and are safe, but are very hungry. You start to walk. After an hour of walking, you see someone behind a bush.")
                            wait_minute()
                            print("You walk up to them and it is a hunter! You think you are saved.")
                            wait_minute()
                            print("The hunter is shocked to see you but you tell him your story, and ask him for food.")
                            wait_minute()
                            print("He gives you food and asks you if you want him to call someone for help. You agree and a day later, you are being taken home! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Fortunately " + str(Name) + " , you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to climb the tree which leads to the bear lying under the tree
                else:
                    Points = Points + 2
                    Health = Health - 3
                    print(" ")
                    wait_minute()
                    print("You decide to climb up a tree. " + str(Name) + " , you see that the bear is coming after you. You go as fast as you can but the bear is faster.")
                    wait_minute()
                    print("You get to the top when suddenly, you hear the scream of the bear. You look down and see that the bear fell! The bear lay right below the tree unconscious.")
                    wait_minute()
                    print("What do you want to do next?")
                    wait_minute()
                    print(" ")
                    print("1. Climb down")
                    print("2. Stay up")
                    print("3. Try to jump to the next tree")
                    Tree = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Tree = int(Tree)
                                if Tree >3 or Tree <1:
                                    print ("That's an incorrect option! Try again.")
                                    Tree = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Tree = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to climb down the tree which leads to them being attacked by the bear
                    if Tree == 1:
                        Points = Points - 2
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to climb down. Suddenly, the bear wakes up! You are stuck! The bear smells your scent and comes after you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + " , you are attacked by the bear! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to stay up on the tree which eventually leads to death
                    elif Tree == 2:
                        Points = Points - 2
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to stay up on the tree. After a few hours, you decide to look down and see that the bear is awake and starts to climb up.")
                        wait_minute()
                        print("You try to jump, but your hand is stuck on the branch! You try to get it free but are unable to!")
                        wait_minute()
                        print("The bear is coming up and sees you! It looks hungry! You try to break free but can't!")
                        wait_minute()
                        print("The bear grabs you and takes you away! You are dead! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + " , you are attacked by the bear! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to jump to the next tree which leads to death
                    else:
                        Points = Points - 2
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to try to jump to the next tree! Bad choice. You see a tree close to your tree and try to jump. You jump but are still too far from the tree!")
                        wait_minute()
                        print("You fall and hit the ground breaking your neck. GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + " , you fall and are bear food! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to stay where they are and call for help using the radio system which leads to them being stuck on the island for a few hours longer
            elif CrashRed == 2:
                Points = Points + 2
                Health = Health - 1
                print(" ")
                wait_minute()
                print("You decide to stay where you are and call for help using the plane's radio device.")
                wait_minute()
                print("You get in contact with someone at Air Control and they say that they need a few hours to find your location.")
                wait_minute()
                print("You are unsure how you can survive for a few more hours.")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Save as much as you can from the plane crash")
                print("2. Try to wait")
                print("3. Go looking for food and water in the forest")
                Hours = raw_input("What is your next step (select a number from the options available)?")

                num = False
                while num == False:
                        try:
                            Hours = int(Hours)
                            if Hours >3 or Hours <1:
                                print ("That's an incorrect option! Try again.")
                                Hours = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Hours = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to save as much as they can from the crash which leads them to find a berry bush
                if Hours == 1:
                    Points = Points + 2
                    Health = Health - 1
                    print(" ")
                    wait_minute()
                    print("You decide to save as much as you can from the plane crash. After hours of trying to save the things, you are hungry.")
                    wait_minute()
                    print("You decide to go into the forest to get something to eat. You step in and see a berry bush.")
                    wait_minute()
                    print("What would you like to do?")
                    wait_minute()
                    print(" ")
                    print("1. Eat the berries")
                    print("2. Don't eat the berries")
                    print("3. Take the berries with you")
                    Bush = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Bush = int(Bush)
                                if Bush >3 or Bush <1:
                                    print ("That's an incorrect option! Try again.")
                                    Bush = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Bush = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to eat the berries which leads to death
                    if Bush == 1:
                        Points = Points - 3
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to eat the berries! Bad choice! You eat one and you start to slowly lose consciousness! You realize that the berries are poisonous!")
                        wait_minute()
                        print("You lose consciousness and die! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + " , you eat poisonous berries! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to not eat the berries which leads them to find a hunter
                    elif Bush == 2:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to not eat the berries. Smart move! You see a squirrel come and eat a berry and die. You realize that the berries were poisonous.")
                        wait_minute()
                        print("You didn't eat the berries and are safe, but are very hungry. You start to walk. After an hour of walking, you see someone behind a bush.")
                        wait_minute()
                        print("You walk up to them and it is a hunter!")
                        wait_minute()
                        print("You think you are saved. The hunter is shocked to see you but you tell him your story, and ask him for food. He gives you food and offers to take you to his house.")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Go with him")
                        print("2. Eat the food and leave")
                        print("3. Run away")
                        Shoot = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Shoot = int(Shoot)
                                    if Shoot >3 or Shoot <1:
                                        print ("That's an incorrect option! Try again.")
                                        Shoot = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Shoot = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to go with the hunter which leads to a suspicious scent
                        if Shoot == 1:
                            Points = Points + 3
                            Health = Health - 1
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to go with the hunter to his house. You walk in and you smell something weird.")
                            wait_minute()
                            print("You ask him what the smell is and changes the topic. He takes you to your room and tells you to not go into the room next door.")
                            wait_minute()
                            print("You are suspicious. When the hunter goes out to get some food, you decide to go into the room. You open the door and the smell is unbearable. You close the door.")
                            wait_minute()
                            print("What would you like to do?")
                            wait_minute()
                            print(" ")
                            print("1. Go back to your room")
                            print("2. Step into the room")
                            print("3. Try to escape")
                            Scent = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Scent = int(Scent)
                                        if Scent >3 or Scent <1:
                                            print ("That's an incorrect option! Try again.")
                                            Scent = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Scent = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to go back to their room which leads to death
                            if Scent == 1:
                                Points = Points - 3
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to go back to your room. As you are backing out of the room, you bump into something. You turn around and see the hunter! He shoots you!")
                                wait_minute()
                                print("As you fall to the ground, he tells you to die in suspense! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you die and you don't know why! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to step back into the room which leads to them finding out the truth about the hunter
                            elif Scent == 2:
                                Points = Points + 2
                                Health = Health - 1
                                print(" ")
                                wait_minute()
                                print(str(Name) + " , you decide to step back into the room. The smell hits you again and you cover your nose.")
                                wait_minute()
                                print("You look around and you see that the walls are red and there are fake skeletons hanging from the ceiling.")
                                wait_minute()
                                print("Except, the wall colour isn't just red, it's blood, and the skeletons aren't fake, they are human skulls.")
                                wait_minute()
                                print("You realize that this hunter is a killer! You walk up to one of the walls and you see a piece of paper.")
                                wait_minute()
                                print("You read the paper and it says that this man is on the most wanted list.")
                                wait_minute()
                                print("He kidnaps his victims, makes them like him and then kills them in the most brutal way.")
                                wait_minute()
                                print("What would you like to do? ")
                                wait_minute()
                                print(" ")
                                print("1. Get out of the room")
                                print("2. Stay in the room and try to find out more")
                                print("3. Try to escape")
                                Murder = raw_input("What is your next step (select a number from the options available)?")

                                num = False
                                while num == False:
                                        try:
                                            Murder = int(Murder)
                                            if Murder >3 or Murder <1:
                                                print ("That's an incorrect option! Try again.")
                                                Murder = raw_input("What would you like to do (select a number from options listed)?")
                                            else:
                                                num = True
                                        except:
                                            print("Invalid Input")
                                            Murder = raw_input("What would you like to do (select a number from options listed)?")

                                #The user decides to get out of the room which leads to death
                                if Murder == 1:
                                    Points = Points - 3
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + " , you decide to get out of the room! You try to open the door but it's stuck! You try to open it but are unable to.")
                                    wait_minute()
                                    print("You wait for the hunter to return and he sees you are stuck in there.")
                                    wait_minute()
                                    print("He opens the door and shoots you in the forehead. GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to stay in their room which leads to death
                                elif Murder == 2:
                                    Points = Points - 3
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    print(str(Name) + " , you decide to stay in the room! You find more articles on this man but nothing that can help you.")
                                    wait_minute()
                                    print("Suddenly, you hear the door open and it's the hunter!")
                                    wait_minute()
                                    print("He pulls out his gun and shoots you! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                                #The user decides to escape which leads to death in many different ways using the random integer function
                                else:
                                    Points = Points - 3
                                    Health = Health * 0
                                    print(" ")
                                    wait_minute()
                                    from random import randint
                                    Option = randint(1,3)
                                    if Option == 1:
                                        print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                        wait_minute()
                                        print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                        wait_minute()
                                        print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                        wait_minute()
                                        print("You don't see a way to escape and so you have to roll. You roll a 3! You are burned alive! YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you are burned alive. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                    elif Option == 2:
                                        print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                        wait_minute()
                                        print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                        wait_minute()
                                        print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                        wait_minute()
                                        print("You roll a 6. You are thrown off a cliff! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you are thrown off a cliff. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                    else:
                                        print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                        wait_minute()
                                        print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                        wait_minute()
                                        print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                        wait_minute()
                                        print("You roll a 1. You are shot in the head! YOU DIE!!! GAME OVER!!!")
                                        wait_minute()
                                        print(" ")
                                        print("Good game! Unfortunately " + str(Name) + " , you are shot in the head. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to escape which leads to death in many different ways using the random integer number
                            else:
                                Points = Points - 3
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                from random import randint
                                Away = randint(1,3)
                                if Away == 1:
                                    print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                    wait_minute()
                                    print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                    wait_minute()
                                    print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                    wait_minute()
                                    print("You don't see a way to escape and so you have to roll. You roll a 3! You are burned alive! YOU DIE!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + ", you are burned alive. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                elif Away == 2:
                                    print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                    wait_minute()
                                    print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                    wait_minute()
                                    print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                    wait_minute()
                                    print("You roll a 6. You are thrown off a cliff! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + ", you are thrown off a cliff. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                                else:
                                    print("You feel something is wrong so you decide to escape. As you are leaving, you hear the door open.")
                                    wait_minute()
                                    print("You see the hunter and it looks like he knows what you were doing. He makes you sit down and tells you he is a serial killer!")
                                    wait_minute()
                                    print("He pulls out a dice and tells you to roll. If you roll a 1 or 2, you will be shot. If you roll a 3 or 4, you will be burned alive. If you roll a 5 or 6, you will be thrown off a cliff.")
                                    wait_minute()
                                    print("You roll a 1. You are shot in the head! YOU DIE!!! GAME OVER!!!")
                                    wait_minute()
                                    print(" ")
                                    print("Good game! Unfortunately " + str(Name) + ", you are shot in the head. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to eat the food which leads to death
                        elif Shoot == 2:
                            Points = Points - 3
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to eat the food and politely tell the man that you want to leave. He gives you a sly smile and tells you that you cannot leave.")
                            wait_minute()
                            print("You are confused when suddenly the hunter shoots you! As you are dying, you hear the man say that this could have gone much more easily. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to run away which leads to death
                        else:
                            Points = Points - 3
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to run away. As you are running away, you turn around and see the hunter gives you a sly smile and tells you that you cannot run away.")
                            wait_minute()
                            print("You stop and turn around.")
                            wait_minute()
                            print("You are confused when suddenly the hunter shoots you! As you are dying, you hear the man say that this could have gone much more easily. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to take the berries with them which leads to them being saved
                    else:
                        Points = Points + 5
                        Health = Health - 2
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to take the berries with you. You see a squirrel come and eat a berry and die.")
                        wait_minute()
                        print("You realize that the berries were poisonous. You leave the berries there.")
                        wait_minute()
                        print("You didn't eat the berries and are safe, but are very hungry. You start to walk. After an hour of walking, you see someone behind a bush.")
                        wait_minute()
                        print("You walk up to them and it is a hunter!")
                        wait_minute()
                        print("You think you are saved. The hunter is shocked to see you but you tell him your story, and ask him for food.")
                        wait_minute()
                        print("He gives you food and asks you if you want him to call someone for help.")
                        wait_minute()
                        print("You agree and a day later, you are being taken home! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Fortunately " + str(Name) + ", you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to wait which leads to death
                elif Hours == 2:
                    Points = Points - 3
                    Health = Health - 2
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to try to wait. You are starving, dehydrated and hypothermic.")
                    wait_minute()
                    print("You die due to starvation. GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to go look for food and water which leads to death
                else:
                    Points = Points - 3
                    Health = Health - 2
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to go looking for food and water. You walk for hours and hours.")
                    wait_minute()
                    print("You are unable to find water or food. You find a berry bush and eat the berries. The berries were poisonous! GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to stay where they are which leads to them seeing a house
            else:
                Points = Points + 2
                Health = Health - 1
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to stay where you are and build a fire to keep yourself warm and not get hypothermic.")
                wait_minute()
                print("You build a fire and are warm, but as no food was saved from the crash, you are hungry. You decide to go look for food.")
                wait_minute()
                print("After walking in the forest for several hours, you see a house with a few lights on inside.")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Turn around and go back where you came from")
                print("2. Continue looking for food")
                print("3. Knock on the door")
                House = raw_input("What is your next step (select a number from the options available)?")

                num = False
                while num == False:
                        try:
                            House = int(House)
                            if House >3 or House <1:
                                print ("That's an incorrect option! Try again.")
                                House = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            House = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to turn around which leads to death
                if House == 1:
                    Points = Points + 2
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to turn around and go back. You turn around and see that the fire that you built is gone!")
                    wait_minute()
                    print("You are stranded, cold and have no food.")
                    wait_minute()
                    print("You know that you will either die due to hypothermia or starvation.")
                    wait_minute()
                    print("You don't want to go through all the pain so you decide to commit suicide. GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + " , you commit suicide! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to look for food which results in them hearing a helicopter
                elif House == 2:
                    Points = Points + 2
                    Health = Health - 2
                    print(" ")
                    wait_minute()
                    print(str(Name) + "! You decide to continue to look for food. You see a tree with fruit growing out of it but you are unsure of what the fruit is.")
                    wait_minute()
                    print("You can't survive any longer without food so you decide to go and eat the fruit. Luckily, the fruit turns out to be mango!")
                    wait_minute()
                    print("You take some with you and are happy that you survived that!")
                    wait_minute()
                    print("Suddenly, you hear a noise from above! It's a helicopter!")
                    wait_minute()
                    print("What would you like to do?")
                    wait_minute()
                    print(" ")
                    print("1. Run away")
                    print("2. Scream and shout")
                    print("3. Build a fire as a signal")
                    Signal = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Signal = int(Signal)
                                if Signal >3 or Signal <1:
                                    print ("That's an incorrect option! Try again.")
                                    Signal = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Signal = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to run away which leads to them being stuck on the island forever
                    if Signal == 1:
                        Points = Points - 2
                        Health = Health - 3
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to run away from the helicopter! BAD CHOICE! You run away and the helicopter passes from above you!")
                        wait_minute()
                        print("You realize that the helicopter was the one helicopter which was going to save your life!")
                        wait_minute()
                        print("Now you are stuck on this island for as long as you live! GAME OVER!!! ")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you stay on the island forever! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to scream and shout which results in them being stuck on the island forever
                    elif Signal == 2:
                        Points = Points - 2
                        Health = Health - 3
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to scream and shout to try to get the attention of the helicopter! You scream and shout but the helicopter does not hear you!")
                        wait_minute()
                        print("You continue to do so, but the pilot doesn't hear you! That helicopter is your last chance and it could not hear you!")
                        wait_minute()
                        print("The helicopter leaves and you are stranded on the island for as long as you live! GAME OVER!!! ")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you stay on the island forever! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to build a fire which leads to them being saved
                    else:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to build a fire to signal the helicopter. The helicopter sees the fire and lands! You are rescued! GAME OVER!!! ")
                        wait_minute()
                        print(" ")
                        print("Good game! Fortunately " + str(Name) + ", you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to knock on the door which results in meeting an old man
                else:
                    Points = Points + 2
                    Health = Health - 2
                    print(" ")
                    wait_minute()
                    print(str(Name) + "! You decide to knock on the door. An old man opens the door. He looks kind and asks you if you would like to come in.")
                    wait_minute()
                    print("What would you like to do?")
                    wait_minute()
                    print(" ")
                    print("1. Ignore the man and leave")
                    print("2. Go into the house with the man")
                    print("3. Run away")
                    Invite = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Invite = int(Invite)
                                if Invite >3 or Invite <1:
                                    print ("That's an incorrect option! Try again.")
                                    Invite = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Invite = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to ignore the man which leads to them being kidnapped
                    if Invite == 1:
                        Points = Points - 1
                        Health = Health - 3
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to ignore the man and leave. As you continue walking, you realize that someone is following you.")
                        wait_minute()
                        print("You turn around and you are hit with a baseball bat!")
                        wait_minute()
                        print("You lose consciousness. When you wake up, you are tied to a chair. You are kidnapped! The old man comes into the room and tells you that he wants a friend.")
                        wait_minute()
                        print("What do you do?")
                        wait_minute()
                        print(" ")
                        print("1. Start talking to him")
                        print("2. Attempt to fight")
                        print("3. Run away")
                        Taken = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Taken = int(Taken)
                                    if Taken >3 or Taken <1:
                                        print ("That's an incorrect option! Try again.")
                                        Taken = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Taken = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to talk to the man which leads to the user becoming friends with the user
                        if Taken == 1:
                            Points = Points - 1
                            Health = Health - 1
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to start talking to the man. His ideals and thoughts start sinking in with you. YOU BECOME FRIENDS WITH A PSYCHOPATH!!! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you have become friends with a psychopath in the forest. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to fight the man which leads to death
                        elif Taken ==2:
                            Points = Points - 1
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to fight the man. As you start to punch the man, he pulls out a knife and stabs you once in the neck.")
                            wait_minute()
                            print("As you bleed to death, you look in the corner of the room.")
                            wait_minute()
                            print("The man is crying and saying that all he wanted was a friend. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + " , you bleed to death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to run away which leads to death in various ways using the random integer function
                        else:
                            Points = Points - 1
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            from random import randint
                            Leave = randint(1,3)
                            if Leave == 1:
                                print("You decide to run away. As you run away, you feel a piercing pain to the back of your head. You touch the back of your head and see dark red.")
                                wait_minute()
                                print("You turn around and see the old man threw a knife at the back of your head. YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you bleed to death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                            elif Leave == 2:
                                print("You decide to run away. As you run away, you see an opening, you run threw that opening and you see yourself falling" + str(Name) + ", you fall off a cliff.")
                                wait_minute()
                                print("YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you fall to your death. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")
                            else:
                                print("You decide to run away. As you run away, you look up and see a snake hanging from the tree. You can't slow down so you keep running. The snake bites you.")
                                wait_minute()
                                print("You run away and you are back at your plane but as soon as you stop running, you die. The snake was poisonous. YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + " , you die due to poison. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to go with the man which results in the man holding the user captive
                    elif Invite == 2:
                        Points = Points - 1
                        Health = Health - 2
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to go with the man into his home. The old man feeds you, gives you a bed to sleep in and always watches you.")
                        wait_minute()
                        print("After 1 day with the man, you want to leave.")
                        wait_minute()
                        print("As you go towards the door, you try to open the door but see that it is locked. You ask the man and he leads you back to your bed.")
                        wait_minute()
                        print("You know something is wrong. The next day this happens again.")
                        wait_minute()
                        print("For a week, the man always leads you away from the door and you follow. One night, you wake up and see that the door is unlocked.")
                        wait_minute()
                        print("What do you do?")
                        wait_minute()
                        print(" ")
                        print("1. Go see what the man is doing")
                        print("2. Try to sneak out")
                        print("3. Go back to sleep")
                        StrangeMan = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    StrangeMan = int(StrangeMan)
                                    if StrangeMan >3 or StrangeMan <1:
                                        print ("That's an incorrect option! Try again.")
                                        StrangeMan = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    StrangeMan = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to see what the man is doing which leads them to be saved
                        if StrangeMan == 1:
                            Points = Points + 5
                            Health = Health - 2
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to go see what the man is doing. As you approach his room, you constantly keep hearing this sound from outside.")
                            wait_minute()
                            print("You step into his room and see that he is not in there. You walk out and hear the sound again. You walk outside and see the old man making weird symbols on a tree.")
                            wait_minute()
                            print("He looks at you and says that he wished you never came out. As soon as you hear this, you start to run as fast as you can.")
                            wait_minute()
                            print("You run for several hours and realize that you have made it back to the plane crash site!")
                            wait_minute()
                            print("There is a helicopter waiting for you! You meet the pilot and he flies you home safely! GAME OVER!")
                            wait_minute()
                            print(" ")
                            print("Good game! Fortunately " + str(Name) + ", you survived the plane crash! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to try to sneak out of the house which results in death
                        elif StrangeMan == 2:
                            Points = Points - 1
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to try to sneak out of the house. As you sneak out, you notice strange markings on the trees surrounding the house.")
                            wait_minute()
                            print("You walk away quietly but hear a sound behind you.")
                            wait_minute()
                            print("The old man is standing behind the tree staring directly at you, He says that he wished you never came out. You don't know what to do so you stand still.")
                            wait_minute()
                            print("The man stabs you 3 times and you bleed to death!!! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you bled to death! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to go back to sleep which results in the user staying with the man
                        else:
                            Points = Points + 5
                            Health = Health - 2
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to go back to sleep meaning that you will stay with the old man for all of eternity.")
                            wait_minute()
                            print("Over time, your ideals and thoughts sink in with the old man.")
                            wait_minute()
                            print("You become his therapist and teach him the true meaning of life. You and the old man stay together in the forest. GAME OVER!")
                            wait_minute()
                            print(" ")
                            print("Good game! Fortunately " + str(Name) + ", you changed the old man! Well done! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to run away in the other direction which results in death
                    else:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to run away in the other direction. You are running fast and there is a large rock in front of you! You see it and are unable to avoid it.")
                        wait_minute()
                        print("You trip and hit your head against the rock. YOU DIE!!! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

        #The user decides to contact Air Control which results in the plane crash
        elif PlaneCockpit == 2:
            Points = Points + 2
            Health = Health - 2
            print(" ")
            wait_minute()
            print(str(Name) + "! You decide to contact Air Control. Good choice. Unfortunately, you are flying where Air Control is unable to speak with you!")
            wait_minute()
            print("You start to look for other ways to stay safe.")
            wait_minute()
            print("Suddenly, the plane starts to lose altitude! You lose consciousness. When you wake up, you see that the plane is burning and you are stranded on an island.")
            wait_minute()
            print("What would you like to do?")
            wait_minute()
            print(" ")
            print("1. Look around the island for food")
            print("2. Try to save all belongings from the burning plane")
            print("3. Stay and make a fire to keep you warm")
            Stranded = raw_input("What would you like to do now (select a number from options)?")

            num = False
            while num == False:
                    try:
                        Stranded = int(Stranded)
                        if Stranded >3 or Stranded <1:
                            print ("That's an incorrect option! Try again.")
                            Stranded = raw_input("What would you like to do (select a number from options listed)?")
                        else:
                            num = True
                    except:
                        print("Invalid Input")
                        Stranded = raw_input("What would you like to do (select a number from options listed)?")

            #The user decides to look around the island and sees a berry bush
            if Stranded == 1:
                Points = Points + 2
                Health = Health - 2
                print(" ")
                wait_minute()
                print(str(Name) + "! You decide to look around the island. You are starving and spend over an hour looking for food. Finally, you look around and see a berry bush.")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Eat the berries")
                print("2. Don't eat the berries")
                print("3. Take the berries with you")
                Food = raw_input("What is your next step (select a number from the options available)?")

                num = False
                while num == False:
                        try:
                            Food = int(Food)
                            if Food >3 or Food <1:
                                print ("That's an incorrect option! Try again.")
                                Food = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Food = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to eat the berries which results in death
                if Food == 1:
                        Points = Points - 3
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to eat the berries! Bad choice! You eat one and you start to slowly lose consciousness! You realize that the berries are poisonous!")
                        wait_minute()
                        print("You lose consciousness and die! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you eat poisonous berries! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to not eat the berries which results in meeting the hunter
                elif Food == 2:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to not eat the berries. Smart move! You see a squirrel come and eat a berry and die. You realize that the berries were poisonous.")
                        wait_minute()
                        print("You didn't eat the berries and are safe, but are very hungry. You start to walk.")
                        wait_minute()
                        print("After an hour of walking, you see someone behind a bush. You walk up to them and it is a hunter!")
                        wait_minute()
                        print("You think you are saved. The hunter is shocked to see you but you tell him your story, and ask him for food. He gives you food and offers to take you to his house.")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Go with him")
                        print("2. Eat the food and leave")
                        print("3. Run away")
                        Hunt = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Hunt = int(Hunt)
                                    if Hunt >3 or Hunt <1:
                                        print ("That's an incorrect option! Try again.")
                                        Hunt = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Hunt = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to go with the man which leads to death
                        if Hunt == 1:
                            Points = Points - 3
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to go with the man. As you both are approaching the house.")
                            wait_minute()
                            print("You both fall into the pit! The hunter breaks his neck and dies so you are stuck there all by yourself.")
                            wait_minute()
                            print("You try to climb out but are unable to. You have no food or water. You die due to dehydration. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you die due to dehydration. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to eat the food which results in death
                        elif Hunt == 2:
                            Points = Points - 3
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to eat the food and politely tell the man that you want to leave. He gives you a sly smile and tells you that you cannot leave.")
                            wait_minute()
                            print("You are confused when suddenly the hunter shoots you! As you are dying, you hear the man say that this could have gone much more easily. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to run away which leads to death
                        else:
                            Points = Points - 3
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to run away. As you are running away, you turn around and see the hunter gives you a sly smile and tells you that you cannot run away.")
                            wait_minute()
                            print("You stop and turn around. You are confused when suddenly the hunter shoots you! As you are dying, you hear the man say that this could have gone much more easily. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to take the berries with them which leads to them being saved
                else:
                    Points = Points - 3
                    Health = Health - 1
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to take the berries with you. You see a squirrel come and eat a berry and die.")
                    wait_minute()
                    print("You realize that the berries were poisonous. You leave the berries there.")
                    wait_minute()
                    print("You didn't eat the berries and are safe, but are very hungry. You start to walk. After an hour of walking, you see someone behind a bush.")
                    wait_minute()
                    print("You walk up to them and it is a hunter! You think you are saved.")
                    wait_minute()
                    print("The hunter is shocked to see you but you tell him your story, and ask him for food. He gives you food and asks you if you want him to call someone for help.")
                    wait_minute()
                    print("You agree and a day later, you are being taken home! GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Fortunately " + str(Name) + ", you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to try to save all their belongings which results in death
            elif Stranded == 2:
                Points = Points - 3
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to try to save all of your belongings from the burning plane.")
                wait_minute()
                print("As you step into the plane, you smell something funny. You start to collect your belongings when you realize that the smell in gasoline!")
                wait_minute()
                print("You try to leave the plane but it blows up! YOU DIE!!! GAME OVER!!!")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to make a fire which eventually leads to death
            else:
                Points = Points - 3
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + " , you decide to make a fire to keep you warm. You make a fire and are warm but due to the wind, the fire burns out.")
                wait_minute()
                print("You are left in the cold and have hypothermia.")
                wait_minute()
                print("You die due to hypothermia! GAME OVER!!!")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + " , you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

        #The user decides to return to their seat which results in them being stuck in their seat
        else:
            Points = Points - 1
            Health = Health - 1
            print(" ")
            wait_minute()
            print(str(Name) + ". You decide to return to your seat. The plane starts to gain altitude and you think everything is fine.")
            wait_minute()
            print("Suddenly, the plane starts to lose altitude and it crashes.")
            wait_minute()
            print("Surprisingly, you were awake the entire time. You are still in your seat but you are stuck!")
            wait_minute()
            print("What would you like to do?")
            wait_minute()
            print(" ")
            print("1. Try to free yourself from the seat")
            print("2. Wait for help to come")
            print("3. Find something that can help you free yourself from the seat")
            Stuck = raw_input("What would you like to do now (select a number from options)?")

            num = False
            while num == False:
                    try:
                        Stuck = int(Stuck)
                        if Stuck >3 or Stuck <1:
                            print ("That's an incorrect option! Try again.")
                            Stuck = raw_input("What would you like to do (select a number from options listed)?")
                        else:
                            num = True
                    except:
                        print("Invalid Input")
                        Stuck = raw_input("What would you like to do (select a number from options listed)?")

            #The user decides to try to free themselves which leads to death
            if Stuck == 1:
                Points = Points - 3
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to try to free yourself from the seat. As you are doing so, you move and you scream in pain.")
                wait_minute()
                print("You are unable to feel your legs and arms.")
                wait_minute()
                print("You are not able to move. You slowly lose consciousness and you die! GAME OVER!!!")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to wait for help to come which leads to death
            elif Stuck == 2:
                Points = Points - 2
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to wait for help to come. You are unable to move so you can't get food or water. You wait for 3 days but no one comes.")
                wait_minute()
                print("You slowly die due to dehydration. GAME OVER!!! ")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to find something that can help them get out of their seat which causes them to be free
            else:
                Points = Points + 2
                Health = Health - 1
                print(" ")
                wait_minute()
                print(str(Name) + ". You decide to find something that can help you get out of your seat. You see a knife.")
                wait_minute()
                print("You try to reach for it but can't. You see that it is on a table and so you kick the table.")
                wait_minute()
                print("The knife falls and you reach for it. You got the knife! You free yourself! Good job! You are now free but don't know what you want to do.")
                wait_minute()
                print("You see that it is getting dark.")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Stay where you are")
                print("2. Wait for help to come")
                print("3. Go into the forest")
                Free = raw_input("What would you like to do now (select a number from options)?")

                num = False
                while num == False:
                        try:
                            Free = int(Free)
                            if Free >3 or Free <1:
                                print ("That's an incorrect option! Try again.")
                                Free = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Free = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to stay right where they are which leads to death
                if Free == 1:
                    Points = Points - 2
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to stay right where you are. You try to build a fire but are unsuccessful. You have no heat, no water and no food.")
                    wait_minute()
                    print("After a few days of waiting, you die due to hypothermia. GAME OVER!!! ")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to wait for help to come which leads to death
                elif Free == 2:
                    Points = Points - 2
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to wait for help to come. You wait for many hours. You have no heat, no water and no food.")
                    wait_minute()
                    print("After a few days of waiting, you die due to dehydration. GAME OVER!!! ")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to go into the forest which leads to them finding a bear
                else:
                    Points = Points + 2
                    Health = Health - 1
                    print(" ")
                    wait_minute()
                    print("You decide to go into the forest and look for anything that can help you. As you are walking, you hear a rustling coming from the bush behind you.")
                    wait_minute()
                    print("You look and see that it's a large, black bear!")
                    wait_minute()
                    print("What do you want to do?")
                    wait_minute()
                    print(" ")
                    print("1. Run away from the bear")
                    print("2. Stay where you are")
                    print("3. Climb up a tree")
                    BlackBear = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                BlackBear = int(BlackBear)
                                if BlackBear >3 or BlackBear <1:
                                    print ("That's an incorrect option! Try again.")
                                    BlackBear = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                BlackBear = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to run away from the bear which leads to death
                    if BlackBear == 1:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to run away from the bear!!! Bad decision! You start running away and trip over a rock.")
                        wait_minute()
                        print("The bear is very angry and comes right toward you." + str(Name) + " , you are unable to get up and the bear is running fast towards you...YOU DIE!!! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to stay right where they are and get attacked by a bear
                    elif BlackBear == 2:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to stay right where you are. You stay where you are and wait for a few minutes. Then you slowly start backing away.")
                        wait_minute()
                        print("You step on a branch and it makes a sound! This catches the attention of the bear and it attacks you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you get attacked by a bear. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to cimb the tree which results in getting attacked by a bear
                    else:
                        Points = Points + 2
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to climb a tree! You are climbing up and the bear is at the bottom.")
                        wait_minute()
                        print("You are at the top when suddenly, you feel the tree shaking. The near is following you!")
                        wait_minute()
                        print("You have no where to go! You are trapped! The bear comes and attacks you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you get attacked by a bear. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

    #The user decides to stay in their seat which results in the crash
    elif Noise == 2:
        Points = Points - 1
        Health = Health - 1
        print(" ")
        wait_minute()
        print("You decide to stay in your seat and not see what the noise was. Bad choice. " + str(Name) + ", you notice the plane is spinning. You realize something is wrong.")
        wait_minute()
        print("What do you want to do?")
        wait_minute()
        print(" ")
        print("1. Get out of your seat and look out the window")
        print("2. Stay in you seat")
        print("3. Get up and check the cockpit")
        PlaneSeat = raw_input("What would you like to do now (select a number from options)?")

        num = False
        while num == False:
                try:
                    PlaneSeat = int(PlaneSeat)
                    if PlaneSeat >3 or PlaneSeat <1:
                        print ("That's an incorrect option! Try again.")
                        PlaneSeat = raw_input("What would you like to do now (select a number from options)?")
                    else:
                        num = True
                except:
                    print("Invalid Input")
                    PlaneSeat = raw_input("What would you like to do now (select a number from options)?")

        #The user decides to get out of their seat which results in death
        if PlaneSeat == 1:
            Points = Points - 1
            Health = Health * 0
            print(" ")
            wait_minute()
            print(str(Name) + "! You decide to get out of your seat and look out the window. Bad decision! Suddenly, the plane flips upside down.")
            wait_minute()
            print("You fall and break your neck! GAME OVER!!!")
            wait_minute()
            print(" ")
            print("Good game! Unfortunately " + str(Name) + ", you break you neck. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

        #The user decides to stay in their seat which results in the crash
        elif PlaneSeat == 2:
            Points = Points - 1
            Health = Health - 1
            print(" ")
            wait_minute()
            print("You decide to stay in your seat and not see what the noise was. Good choice." + str(Name) + ", you notice the plane is spinning.")
            wait_minute()
            print("The plan flips upside down and it seems to be declining! The plane crashes! You lose comciousness but wake up sometime later. Unfortunately, you are stuck in your seat!")
            wait_minute()
            print("What do you want to do?")
            wait_minute()
            print(" ")
            print("1. Try to free youself from the seat")
            print("2. Wait for help to come")
            print("3. Find something that can help you free yourself from the seat")
            Seat = raw_input("What would you like to do now (select a number from options)?")

            num = False
            while num == False:
                    try:
                        Seat = int(Seat)
                        if Seat >3 or Seat <1:
                            print ("That's an incorrect option! Try again.")
                            Seat = raw_input("What would you like to do (select a number from options listed)?")
                        else:
                            num = True
                    except:
                        print("Invalid Input")
                        Seat = raw_input("What would you like to do (select a number from options listed)?")

            #The user decides to try to free themselves which leads to death
            if Seat == 1:
                Points = Points - 3
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to try to free yourself from the seat. As you are doing so, you move and you scream in pain.")
                wait_minute()
                print("You are unable to feel your legs and arms. You are not able to move.")
                wait_minute()
                print("You slowly lose consciousness and you die! GAME OVER!!!")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to wait for help to come which leads to death
            elif Seat == 2:
                Points = Points - 2
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to wait for help to come. You are unable to move so you can't get food or water. You wait for 3 days but no one comes.")
                wait_minute()
                print("You slowly die due to dehydration. GAME OVER!!! ")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to find something that can help them get out of the seat and this causes them to be free
            else:
                Points = Points + 2
                Health = Health - 1
                print(" ")
                wait_minute()
                print(str(Name) + ". You decide to find something that can help you get out of your seat. You see a knife.")
                wait_minute()
                print("You try to reach for it but can't. You see that it is on a table and so you kick the table.")
                wait_minute()
                print("The knife falls and you reach for it. You got the knife! You free yourself! Good job! You are now free but don't know what you want to do.")
                wait_minute()
                print("You see that it is getting dark.")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Stay where you are")
                print("2. Wait for help to come")
                print("3. Go into the forest")
                Knife = raw_input("What would you like to do now (select a number from options)?")

                num = False
                while num == False:
                        try:
                            Knife = int(Knife)
                            if Knife >3 or Knife <1:
                                print ("That's an incorrect option! Try again.")
                                Knife = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Knife = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to stay right where they are which leads to death
                if Knife == 1:
                    Points = Points - 2
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to stay right where you are. You try to build a fire but are unsuccessful. You have no heat, no water and no food.")
                    wait_minute()
                    print("After a few days of waiting, you die due to hypothermia. GAME OVER!!! ")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to wait for help to come which causes them to die
                elif Knife == 2:
                    Points = Points - 2
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to wait for help to come. You wait for many hours. You have no heat, no water and no food.")
                    wait_minute()
                    print("After a few days of waiting, you die due to dehydration. GAME OVER!!! ")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you die! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to go into the forest which causes them to see a brown bear
                else:
                    Points = Points + 2
                    Health = Health - 1
                    print(" ")
                    wait_minute()
                    print("You decide to go into the forest and look for anything that can help you. As you are walking, you hear a rustling coming from the bush behind you.")
                    wait_minute()
                    print("You look and see that it's a large, brown bear!")
                    wait_minute()
                    print("What do you want to do?")
                    wait_minute()
                    print(" ")
                    print("1. Run away from the bear")
                    print("2. Stay where you are")
                    print("3. Climb up a tree")
                    BrownBear = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                BrownBear = int(BrownBear)
                                if BrownBear >3 or BrownBear <1:
                                    print ("That's an incorrect option! Try again.")
                                    BrownBear = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                BrownBear = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to run away from the bear which results in death
                    if BrownBear == 1:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to run away from the bear!!! Bad decision! You start running away and trip over a rock.")
                        wait_minute()
                        print("The bear is very angry and comes right toward you.")
                        wait_minute()
                        print(str(Name) + " , you are unable to get up and the bear is running fast towards you...YOU DIE!!! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to stay where they are which causes death
                    elif BrownBear == 2:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to stay right where you are. You stay where you are and wait for a few minutes.")
                        wait_minute()
                        print("Then you slowly start backing away. You step on a branch and it makes a sound!")
                        wait_minute()
                        print("This catches the attention of the bear and it attacks you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you get attacked by a bear. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to climb a tree which results in death
                    else:
                        Points = Points + 2
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to climb a tree! You are climbing up and the bear is at the bottom. You are at the top when suddenly, you feel the tree shaking.")
                        wait_minute()
                        print("The bear is following you! You have no where to go! You are trapped!")
                        wait_minute()
                        print("The bear comes and attacks you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you get attacked by a bear. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

        #The user decides to check the cockpit which results in death
        else:
            Points = Points - 1
            Health = Health * 0
            print(" ")
            wait_minute()
            print(str(Name) + "! You decide to get up and check the cockpit! Bad decision! You step into the cockpit and see that the pilot is unconscious.")
            wait_minute()
            print("You check his pulse and realize that he's dead!")
            wait_minute()
            print("Suddenly, the plane flips upside down. You fall and break your neck! GAME OVER!!!")
            wait_minute()
            print(" ")
            print("Good game! Unfortunately " + str(Name) + " , you break you neck. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

    #The user decides to hide which leads to the crash
    else:
        Points = Points - 1
        Health = Health - 2
        print(" ")
        wait_minute()
        print("You decide to hide. Not the best option. You hide behind a seat and notice that the plane seems to be going down. You think the plane is crashing!")
        wait_minute()
        print("What do you want to do?")
        wait_minute()
        print(" ")
        print("1. Look out the window")
        print("2. Stay in you seat")
        print("3. Get up and check the cockpit")
        PlaneHide = raw_input("What would you like to do now (select a number from options)?")

        num = False
        while num == False:
                try:
                    PlaneHide = int(PlaneHide)
                    if PlaneHide >3 or PlaneHide <1:
                        print ("That's an incorrect option! Try again.")
                        PlaneHide = raw_input("What would you like to do now (select a number from options)?")
                    else:
                        num = True
                except:
                    print("Invalid Input")
                    PlaneHide = raw_input("What would you like to do now (select a number from options)?")

        #The user decides to get out of their seat which leads to death
        if PlaneHide == 1:
            Points = Points - 1
            Health = Health * 0
            print(" ")
            wait_minute()
            print(str(Name) + "! You decide to get out of your seat and look out the window. Bad decision! Suddenly, the plane flips upside down.")
            wait_minute()
            print("You fall and break your neck! GAME OVER!!!")
            wait_minute()
            print(" ")
            print("Good game! Unfortunately " + str(Name) + ", you break you neck. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

        #The user decides to stay in their seat which causes them to eventually get lost in the forest
        elif PlaneHide == 2:
            Points = Points + 2
            Health = Health - 2
            print(" ")
            wait_minute()
            print("You decide to stay in your seat. Good choice. As you fasten your seatbelt, you feel nauseous. The plane is spinning! You lose consciousness.")
            wait_minute()
            print("When you wake up, you are stuck in your seat. You see a knife lying beside you and you free yourself. You get up and realize that you are stranded on an island!")
            wait_minute()
            print("You are feeling very hungry so you decide to go in the forest. You walk for hours and hours and then realize that you are lost!")
            wait_minute()
            print("You don't know which way to go! You better be RIGHT!")
            wait_minute()
            print("Which way would you like to turn?")
            wait_minute()
            print(" ")
            print("1. Left")
            print("2. Right")
            print("3. Straight")
            Turn = raw_input("What would you like to do now (select a number from options)?")

            num = False
            while num == False:
                    try:
                        Turn = int(Turn)
                        if Turn >3 or Turn <1:
                            print ("That's an incorrect option! Try again.")
                            Turn = raw_input("What would you like to do (select a number from options listed)?")
                        else:
                            num = True
                    except:
                        print("Invalid Input")
                        Turn = raw_input("What would you like to do (select a number from options listed)?")

            #The user decides to turn left which leads to a meeting with a leopard
            if Turn == 1:
                Points = Points + 2
                Health = Health - 2
                print(" ")
                wait_minute()
                print(str(Name) + ", you decide to turn left. Bad choice! As you are walking, you see a large spotted creature looking directly at you.")
                wait_minute()
                print("It's a leopard! And it looks hungry!")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Turn around")
                print("2. Stay where you are")
                print("3. Approach the leopard")
                Leopard = raw_input("What would you like to do now (select a number from options)?")

                num = False
                while num == False:
                        try:
                            Leopard = int(Leopard)
                            if Leopard >3 or Leopard <1:
                                print ("That's an incorrect option! Try again.")
                                Leopard = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Leopard = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to turn around which leads to death
                if Leopard == 1:
                    Points = Points - 1
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + "! You decide to turn around. Bad choice! The leopard senses movement and starts running towards you.")
                    wait_minute()
                    print("You are attacked by a leopard! GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you are attacked by a leopard. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to stay right where they are which leads them to meet a bear
                elif Leopard == 2:
                    Points = Points + 2
                    Health = Health - 2
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to stay where you are and not move. Good choice! The leopard slowly starts to back away.")
                    wait_minute()
                    print("You are free! You continue to walk trying to find your way back.")
                    wait_minute()
                    print("Suddenly, you hear another noise behind you. You turn around a see a large spectacled bear!")
                    wait_minute()
                    print("What would you like to do?")
                    wait_minute()
                    print(" ")
                    print("1. Run away from the bear")
                    print("2. Stay where you are")
                    print("3. Climb up a tree")
                    SpectacledBear = raw_input("What would you like to do now (select a number from options)?")

                    num = False
                    while num == False:
                            try:
                                SpectacledBear = int(SpectacledBear)
                                if SpectacledBear >3 or SpectacledBear <1:
                                    print ("That's an incorrect option! Try again.")
                                    SpectacledBear = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                SpectacledBear = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to run away from the bear which leads to death
                    if SpectacledBear == 1:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to run away from the bear!!! Bad decision! You start running away and trip over a rock. The bear is very angry and comes right toward you.")
                        wait_minute()
                        print(str(Name) + ", you are unable to get up and the bear is running fast towards you...YOU DIE!!! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you have died. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to stay where they are which leads to death
                    elif SpectacledBear == 2:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to stay right where you are. You stay where you are and wait for a few minutes.")
                        wait_minute()
                        print("Then you slowly start backing away. You step on a branch and it makes a sound!")
                        wait_minute()
                        print("This catches the attention of the bear and it attacks you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you get attacked by a bear. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to climb a tree which leads to death
                    else:
                        Points = Points - 1
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + "! You decide to climb a tree! You are climbing up and the bear is at the bottom. You are at the top when suddenly, you feel the tree shaking.")
                        wait_minute()
                        print("The near is following you! You have no where to go! You are trapped! The bear comes and attacks you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you get attacked by a bear. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides approach the leopard which leads to death
                else:
                    Points = Points + 2
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + "! You decide to approach the leopard! The leopard senses movement and attacks you! GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you get attacked by a leopard. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to turn right which leads to a sighting of a chopper
            elif Turn == 2:
                Points = Points + 3
                Health = Health - 2
                print(" ")
                wait_minute()
                print("You decide to turn right! Good job you took the hint! After walking for a few hours, you make it back!")
                wait_minute()
                print("Suddenly, you hear a noise. " + str(Name) + ", you realize it's a chopper!")
                wait_minute()
                print("You run into the forest again but see a clearing where the chopper will probably land!")
                wait_minute()
                print("What would you like to do?")
                wait_minute()
                print(" ")
                print("1. Hide")
                print("2. Scream and shout from inside the forest")
                print("3. Try to make a fire as a signal")
                Chopper = raw_input("What would you like to do now (select a number from options)?")

                num = False
                while num == False:
                        try:
                            Chopper = int(Chopper)
                            if Chopper >3 or Chopper <1:
                                print ("That's an incorrect option! Try again.")
                                Chopper = raw_input("What would you like to do (select a number from options listed)?")
                            else:
                                num = True
                        except:
                            print("Invalid Input")
                            Chopper = raw_input("What would you like to do (select a number from options listed)?")

                #The user decides to hide from the chopper which leads to a man approaching you
                if Chopper == 1:
                    Points = Points + 2
                    Health = Health - 1
                    print(" ")
                    wait_minute()
                    print(str(Name) + " , you decide to hide from the chopper. As you run behind a bush in the forest, you see a man step off from the chopper.")
                    wait_minute()
                    print("He is in no condition to move as he looks very ill.")
                    wait_minute()
                    print("He is also in handcuffs. Another man steps down from the chopper and seems to be wearing a uniform of some sort.")
                    wait_minute()
                    print("You overhear someone telling the man in the uniform that the criminal needs to be taken to the prison.")
                    wait_minute()
                    print("You realize that this island holds prisoners and criminals from all over the world! It holds the most wanted!")
                    wait_minute()
                    print("You move your foot and you step on a branch. The man hears you and starts walking towards you.")
                    wait_minute()
                    print("What would you do?")
                    wait_minute()
                    print(" ")
                    print("1. Try to sneak away")
                    print("2. Go talk to the man in the uniform")
                    print("3. Stay where you are")
                    Uniform = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Uniform = int(Uniform)
                                if Uniform >3 or Uniform <1:
                                    print ("That's an incorrect option! Try again.")
                                    Uniform = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Uniform = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to sneak away which leads to more choppers
                    if Uniform == 1:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + " , you decide to sneak away. As you do so, the man starts to walk slowly towards you. You run away but the man is behind you.")
                        wait_minute()
                        print("You keep walking fast and have lost the man but you are unsure where you are. Suddenly, you hear more choppers in the air and shouting voices.")
                        wait_minute()
                        print("The voices are getting closer.")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Stay where you are")
                        print("2. Run away")
                        print("3. Go hide")
                        Voices = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Voices = int(Voices)
                                    if Voices >3 or Voices <1:
                                        print ("That's an incorrect option! Try again.")
                                        Voices = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Voices = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to stay right where they are which leads to death
                        if Voices == 1:
                            Points = Points - 2
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to stay right where you are. The shouting gets closer and closer.")
                            wait_minute()
                            print("10 people with guns come towards you and you are shot right then and there.")
                            wait_minute()
                            print("The guards thought you were an escapee! You shouldn't have stayed! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to run away which leads to seeing guards at the plane crash sight
                        elif Voices == 2:
                            Points = Points + 3
                            Health = Health - 1
                            print(" ")
                            wait_minute()
                            print(str(Name) + " , you decide to run away. As you do so, you hear the shouting get quieter and quieter! Good choice! You continue to walk.")
                            wait_minute()
                            print("You know that this is an island where the world's most dangerous criminals are held as prisoners. You continue to walk when you see your plane!")
                            wait_minute()
                            print("You look through an opening through a bush and see the guards inspecting the plane.")
                            wait_minute()
                            print("What would you do?")
                            wait_minute()
                            print(" ")
                            print("1. Stay where you are")
                            print("2. Go to them")
                            print("3. Run away")
                            Inspect = raw_input("What is your next step (select a number from the options available)?")

                            num = False
                            while num == False:
                                    try:
                                        Inspect = int(Inspect)
                                        if Inspect >3 or Inspect <1:
                                            print ("That's an incorrect option! Try again.")
                                            Inspect = raw_input("What would you like to do (select a number from options listed)?")
                                        else:
                                            num = True
                                    except:
                                        print("Invalid Input")
                                        Inspect = raw_input("What would you like to do (select a number from options listed)?")

                            #The user decides to stay where they are which results in death
                            if Inspect == 1:
                                Points = Points - 2
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to stay where you are and look to see what the guards do. You walk and you make eye contact with one of the guards!")
                                wait_minute()
                                print("They see you and shoot at you! YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + ", you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to go to the guards which leads to the user being saved
                            elif Inspect == 2:
                                Points = Points + 3
                                Health = Health - 1
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to go to the guards. They see you but do not shoot. They realize that you are the plane crash survivor and decide to help you.")
                                wait_minute()
                                print("One of the guards takes you on the chopper and you are back at home!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Fortunately " + str(Name) + ", you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                            #The user decides to run away in the other direction which leads to death
                            else:
                                Points = Points - 2
                                Health = Health * 0
                                print(" ")
                                wait_minute()
                                print(str(Name) + ", you decide to run away in the other direction. As you are running away, you hear a noise behind you.")
                                wait_minute()
                                print("You turn around and it's a bear! The bear roars and comes after you.")
                                wait_minute()
                                print("You are eaten by the bear! YOU DIE!!! GAME OVER!!!")
                                wait_minute()
                                print(" ")
                                print("Good game! Unfortunately " + str(Name) + ", you get eaten by a bear! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to go hide which leads to death
                        else:
                            Points = Points - 2
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to go hide. As you are finding a good spot, you notice a spot behind a bush.")
                            wait_minute()
                            print("You hide behind a bush when suddenly you fall! It was a trap!")
                            wait_minute()
                            print("You break your neck. YOU DIE!!! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you fall and break your neck! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to go talk to the police man which leads to them being saved
                    elif Uniform == 2:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to go talk to the police man. You tell him that you are not a prisoner and were in a plane crash.")
                        wait_minute()
                        print("He doesn't believe you at first but you tell him that you will take him to the plane crash site.")
                        wait_minute()
                        print("You, the prisoner and the police officer walk for an hour and make it back to the plane crash site!")
                        wait_minute()
                        print("The police officer believes you and decides to help you and take you back! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Fortunately " + str(Name) + " , you are saved! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to stay where they are and this results in death
                    else:
                        Points = Points - 2
                        Health = Health * 0
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to stay right where you are. The man comes to you and points a gun to you. You tell him your story but he doesn't believe you.")
                        wait_minute()
                        print("He thinks you are a prisoner!!! He shoots you! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + " , you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to scream and shout which leads to the user reaching prison
                elif Chopper == 2:
                    Points = Points - 1
                    Health = Health - 4
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to scream and shout. The chopper starts to land and a man in a uniform gets out.")
                    wait_minute()
                    print("Suddenly, he knocks you out! You wake up and realize you are in handcuffs!")
                    wait_minute()
                    print("You ask the man in the uniform why you are in handcuffs and he says that he knows that you were trying to escape from prison!")
                    wait_minute()
                    print("You realize that this island holds the most dangerous criminals from all over the world!")
                    wait_minute()
                    print("You keep telling the man that you were stranded on the island but he doesn't believe you.")
                    wait_minute()
                    print("You reach the prison with the man and he locks you up in a cell.")
                    wait_minute()
                    print("What would you do?")
                    wait_minute()
                    print(" ")
                    print("1. Try to escape")
                    print("2. Stay where you are")
                    print("3. Ask for help from another prisoner")
                    Cell = raw_input("What is your next step (select a number from the options available)?")

                    num = False
                    while num == False:
                            try:
                                Siren = int(Siren)
                                if Siren >3 or Siren <1:
                                    print ("That's an incorrect option! Try again.")
                                    Siren = raw_input("What would you like to do (select a number from options listed)?")
                                else:
                                    num = True
                            except:
                                print("Invalid Input")
                                Siren = raw_input("What would you like to do (select a number from options listed)?")

                    #The user decides to try to escape from prison and stumbles upon a door
                    if Cell == 1:
                        Points = Points + 2
                        Health = Health - 4
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to try to escape from the cell. You hear a voice and notice the guard with the keys to your cell.")
                        wait_minute()
                        print("He is slowly falling asleep. He is right in front of you and you decide to try to steal the keys.")
                        wait_minute()
                        print("You reach out and grab the keys slowly and carfeully. You unlock the cell door but as you do so, a siren wails! You start to run!")
                        wait_minute()
                        print("You run and make it to a door.")
                        wait_minute()
                        print("What would you do?")
                        wait_minute()
                        print(" ")
                        print("1. Open the door")
                        print("2. Try to find another way out")
                        print("3. Turn back around and surrender")
                        Siren = raw_input("What is your next step (select a number from the options available)?")

                        num = False
                        while num == False:
                                try:
                                    Siren = int(Siren)
                                    if Siren >3 or Siren <1:
                                        print ("That's an incorrect option! Try again.")
                                        Siren = raw_input("What would you like to do (select a number from options listed)?")
                                    else:
                                        num = True
                                except:
                                    print("Invalid Input")
                                    Siren = raw_input("What would you like to do (select a number from options listed)?")

                        #The user decides to open the door and this leads to them being stuck in prison forever
                        if Siren == 1:
                            Points = Points - 1
                            Health = Health - 3
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to open the door. You open the door and on the other side is a group of guards waiting for you!")
                            wait_minute()
                            print("They catch you and you are taken back to your cell! You stay there for your entire life counting the days. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you are stuck in prison! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to try to find another way out which leads to death
                        elif Siren == 2:
                            Points = Points - 2
                            Health = Health * 0
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to try to find another way out. You turn right and you start to run. Suddenly, you hear a group of guards approaching you.")
                            wait_minute()
                            print("You start to run in the other direction but you hear guards coming from there too!")
                            wait_minute()
                            print("You hear one of the guards say to another that they have been given an order to shoot you on sight!")
                            wait_minute()
                            print("You are stuck. One of the guards sees you and you are shot multiple times. YOU DIE!!! GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you are shot trying to escape! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                        #The user decides to turn around and sureender which results in being stuck in prison
                        else:
                            Points = Points + 2
                            Health = Health - 2
                            print(" ")
                            wait_minute()
                            print(str(Name) + ", you decide to turn around and surrender. You walk back to your cell and a guard is screaming.")
                            wait_minute()
                            print("The guards shuts you in your cell and you remain there for all of eternity. GAME OVER!!!")
                            wait_minute()
                            print(" ")
                            print("Good game! Unfortunately " + str(Name) + ", you surrender and are stuck in jail! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to stay where they are which results in them being stuck in prison
                    elif Cell == 2:
                        Points = Points - 2
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you decide to stay right where you are. Every day, you keep thinking to yourself that you wished you tried to escape.")
                        wait_minute()
                        print("You are stuck in this prison with high security for all your life! GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + " , you are stuck in prison! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                    #The user decides to ask a few other prisoners to escape which leads to the user being stuck in prison
                    else:
                        Points = Points + 3
                        Health = Health - 1
                        print(" ")
                        wait_minute()
                        print(str(Name) + ", you as another few prisoners if they would help you escape. You plan for days on how to escape from prison. You decide to try to dig your way out.")
                        wait_minute()
                        print("Day by day, you and the prisoners slowly and carefully try to dig. After a few months, you make a hole large enough to escape!")
                        wait_minute()
                        print("One of the other prisoners decides to go first.")
                        wait_minute()
                        print("The other prisoner leaves and as soon as he leaves, one of the guards catches you!")
                        wait_minute()
                        print("You and the other prisoners with you, are sent back to your cells for all of your life. GAME OVER!!!")
                        wait_minute()
                        print(" ")
                        print("Good game! Unfortunately " + str(Name) + ", you are stuck in prison! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

                #The user decides to start a fire which results in death
                else:
                    Points = Points - 1
                    Health = Health * 0
                    print(" ")
                    wait_minute()
                    print(str(Name) + ", you decide to start a fire. As you get the things needed from the woods, you notice the chopper slowly landing.")
                    wait_minute()
                    print("A man with a uniform steps off the chopper and tells you to go back to prison with him.")
                    wait_minute()
                    print("You are confused and he tells you to go back to prison. You realize that you are stuck on an island with prisoners!")
                    wait_minute()
                    print("You say no to the man. He points a gun at you and you hear a gunshot. You are shot! GAME OVER!!!")
                    wait_minute()
                    print(" ")
                    print("Good game! Unfortunately " + str(Name) + ", you are shot! You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

            #The user decides to go straight which results in death
            else:
                Points = Points - 1
                Health = Health * 0
                print(" ")
                wait_minute()
                print(str(Name) + "! You decide to go straight. You keep walking and walking. You see a snake hanging from a tree. It bites you. You continue to walk.")
                wait_minute()
                print("After a few minutes, you start to feel drowsy. You realize the snake was poisonous! GAME OVER!!!")
                wait_minute()
                print(" ")
                print("Good game! Unfortunately " + str(Name) + " , you get bitten by a snake and die. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

        #The user decides to get up and check the cockpit which results in death
        else:
            Points = Points - 1
            Health = Health * 0
            print(" ")
            wait_minute()
            print(str(Name) + "! You decide to get up and check the cockpit! Bad decision! You step into the cockpit and see that the pilot is unconscious.")
            wait_minute()
            print("You check his pulse and realize that he's dead! Suddenly, the plane flips upside down. You fall and break your neck! GAME OVER!!!")
            wait_minute()
            print(" ")
            print("Good game! Unfortunately " + str(Name) + ", you break you neck. You have received " + str(Points) + " points and your health was at " + str(Health) + ". Good job!")

    #If the user runs out of health, this message will be displayed. They lose all their health if they die.
    if Health == 0:
        print("GAME OVER!!! You have no health remaining")

    #The program displays a message to the user based on the number of points that they have
    if Points < 0 or Points == 0:
        print(" ")
        wait_minute()
        print("Better luck next time! You received " + str(Points) + " points. You can try to do better! Nice try, " + str(Name) + ".")

    elif Points > 0 and Points < 10:
        print(" ")
        wait_minute()
        print("Good job! You received " + str(Points) + " points. You did well! Next time " + str(Name) + ", you can do even better!")

    elif Points > 10:
        print(" ")
        wait_minute()
        print("Awesome job! " + str(Name) + ", you sure know what you are doing! You received " + str(Points) + " points. Very well done!")

    #The user is asked if they would like to play again. If they type in anything other than yes or no, they are continued to be asked the question until they type in yes or no
    wait_minute()
    TryAgain = raw_input("Would you like to try again (type in yes or no)?")

    num = False
    while num == False:
            try:
                if TryAgain == "yes" or TryAgain == "Yes" or TryAgain == "no" or TryAgain == "No":
                    num = True
                else:
                    print ("That's an incorrect option! Try again.")
                    TryAgain = raw_input("Would you like to try again (type in yes or no)?")
            except:
                print("Invalid Input")
                TryAgain = raw_input("Would you like to try again (type in yes or no)?")

    if TryAgain == "yes" or TryAgain == "Yes":
        continue

    else:
        print(" ")
        wait_minute()
        print("Thank you for playing this game!")
        wait_minute()
        print("Bye").center(100,"*")
        break

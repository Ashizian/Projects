import random
version = "1.0.0"

## CLASSES ##

class Fighter():
  
  def __init__(self, name, weight, dexterity, strength, accuracy):
    self.name = name
    self.weight = weight
    self.dexterity = dexterity
    self.strength = strength
    self.accuracy = accuracy
    self.health = round(10 * weight)
    self.concentrate = 3
    self.is_ko = False

  def __repr__(self):
    if self.weight == 1:
        return "{name} is a lightweight fighter with {health} health.".format(name=self.name, health=self.health)
    elif self.weight == 2:
        return "{name} is a middleweight fighter with {health} health.".format(name=self.name, health=self.health)
    elif self.weight == 3:
        return "{name} is a heavyweight fighter with {health} health.".format(name=self.name, health=self.health)

  def k_o(self):
      self.is_ko = True
      if self.health != 0:
          self.health = 0
      print("{name} is K. O.!".format(name=self.name))

  def lose_health(self, amount):
      self.health -= amount
      if self.health <= 0:
          self.health = 0
          self.k_o()
      else:
          print("{name} has lost {amount} health.".format(name=self.name, amount=amount))

  def gain_health(self, amount):
      self.health += amount

  def punch(self, other_fighter):
    if random.randint(1, 10) <= self.accuracy:
      print("{name} has given a punch to {other_fighter}".format(name=self.name, other_fighter=other_fighter.name))
      other_fighter.lose_health(self.strength)
    else:
      print("{name} missed his punch!".format(name=self.name))
      
  def kick(self, other_fighter):
    if random.randint(1, 10) <= self.accuracy:
      print("{name} has given a kick to {other_fighter}".format(name=self.name, other_fighter=other_fighter.name))
      other_fighter.lose_health(round((self.dexterity + self.strength) / 2))
    else:
      print("{name} missed his kick!".format(name=self.name))

  def joint_lock(self, other_fighter):
    if random.randint(1, 10) <= self.accuracy:
      print("{name} is performing a joint lock on {other_fighter}".format(name=self.name, other_fighter=other_fighter.name))
      other_fighter.lose_health(self.dexterity)
    else:
      print("{name} botched his joint lock!".format(name=self.name))

  def concentration(self):
    if self.concentrate > 0:
      print("{name} is focusing all his thoughts on victory.".format(name=self.name))
      self.gain_health(5)
      self.concentrate -= 1
    else:
      print("{name} has no resolve left!".format(name=self.name))

class Ring():

  def __init__(self, kind, fighter_a, fighter_b):  
    self.kind = kind
    self.fighter_a = fighter_a
    self.fighter_b = fighter_b
    self.turn = 1

  def malus_bonus(self, kind, fighter_a, fighter_b):
    
    if kind == "Circle":
        pass
    elif kind == "Square":
        fighter_a.strength += 2
        fighter_b.strength += 2
        fighter_a.dexterity -= 2
        fighter_a.dexterity -= 2
    elif kind == "Rectangle":
        fighter_a.strength += 1
        fighter_b.strength += 1
        fighter_a.dexterity -= 1
        fighter_a.dexterity -= 1
    elif kind == "Hexagon":
        fighter_a.strength += 1
        fighter_b.strength += 1
    elif kind == "Octogon":
        fighter_a.strength += 2
        fighter_b.strength += 2
    elif kind == "Pentagon":
        fighter_a.dexterity += 1
        fighter_b.dexterity += 1
    elif kind == "Street":
        fighter_a.dexterity += 4
        fighter_b.dexterity += 4
        fighter_a.strength += 4
        fighter_b.strength += 4

  def adding_turn(self):
    self.turn += 1

  def fighting(self, fighter_a, fighter_b):
    turnactive = True
    while turnactive:
    
        if fighter_a.health == 0:
            print("{name} lose!".format(name=fighter_a.name))
            turnactive = False
            break
        elif fighter_b.health == 0:
            print("{name} lose!".format(name=fighter_b.name))
            turnactive = False
            break
            
        print(" ")
        print("We are now at turn {turn}".format(turn=self.turn))
        print(" ")
        print("{name} has {health} health.".format(name=fighter_a.name, health=fighter_a.health))
        print("{name} has {health} health.".format(name=fighter_b.name, health=fighter_b.health))
        viewMenu()        
        pl_input = input("Choose your attack: ")
        ad_input = random.choice(["1", "2", "3", "4"])
       
        if pl_input == "1":
            fighter_a.punch(fighter_b)
        elif pl_input == "2":
            fighter_a.kick(fighter_b)
        elif pl_input == "3":
            fighter_a.joint_lock(fighter_b)
        else:
            fighter_a.concentration()

        if ad_input == "1" and fighter_b.health != 0:
            fighter_b.punch(fighter_a)
        elif ad_input == "2" and fighter_b.health != 0:
            fighter_b.kick(fighter_a)
        elif ad_input == "3" and fighter_b.health != 0:
            fighter_b.joint_lock(fighter_a)
        elif ad_input == "4" and fighter_b.health != 0:
            fighter_b.concentration()
        else:
            pass

        self.adding_turn()

## VARIABLES ##

pl_input = ""
f_1 = Fighter("Andre", 1, 4, 2, 9)
f_2 = Fighter("Jean", 2, 6, 2, 8)
f_3 = Fighter("Brick", 3, 2, 8, 7) 
f_4 = Fighter("James", 1, 6, 2, 7)
f_5 = Fighter("Chris", 2, 2, 2, 8)
f_6 = Fighter("Liu", 3, 2, 4, 9)
f_7 = Fighter("Kokoda", 1, 4, 6, 8)
f_8 = Fighter("Ibrahim", 2, 4, 4, 8)
f_9 = Fighter("Miguel", 3, 8, 4, 9)
f_10 = Fighter("Dio", 3, 7, 7, 9)

## FUNCTIONS ##

def error():
    print("Please, hit a valid key.")

def viewMenu():
    print("""
    Press: 
    1 - Punch   3 - Joint-lock   
    2 - Kick    4 - Concentrate
    """)
    if helprep == "y" or helprep == "Y":
        print("Help: Punches needs only strength. Kicks depends on strength and dexterity.\nJoint-locks uses dexterity alone. You can only concentrate three time by fight, for 5 health each.")
        print(" ")
    else:
        pass

def fighterChoice(choice):

    if choice == "1":
        return f_1
    elif choice == "2":
        return f_2
    elif choice == "3":
        return f_3       
    elif choice == "4":
        return f_4
    elif choice == "5":
        return f_5
    elif choice == "6":
        return f_6
    elif choice == "7":
        return f_7
    elif choice == "8":
        return f_8
    elif choice == "9":
        return f_9
    elif choice == "R" or choice == "r":
        return random.choice([f_1, f_2, f_3, f_4, f_5, f_6, f_7, f_8, f_9, f_10])
    else:
        return random.choice([f_1, f_2, f_3])

def ringChoice(choice):

    if choice == "1":
        return "Circle"
    elif choice == "2":
        return "Square"
    elif choice == "3":
        return "Rectangle"
    elif choice == "4":
        return "Hexagon"
    elif choice == "5":
        return "Octogon"
    elif choice == "6":
        return "Pentagon"
    elif choice == "R" or choice_c == "r":
        return random.choice(["Circle", "Square", "Rectangle", "Hexagon", "Octogon", "Pentagon", "Street"])
    else:
        return random.choice(["Circle", "Square", "Rectangle"])

def fighterPres(choice):
    if choice == f_1:
        print("Andre is mainly known for his superhuman accuracy,\ncoupled with decent dexterity.")
    elif choice == f_2:
        print("Jean is renowned for having the best dexterity/accuracy\nratio of all fighters.")
    elif choice == f_3:
        print("Brick is an absolute monster of pure strength...\nwhen he actually hit something.")
    elif choice == f_4:
        print("James is a grappler with good dexterity,\nbut not very bright.")
    elif choice == f_5:
        print("Main rival of Brick, Chris is not as strong but\nfar more accurate.")
    elif choice == f_6:
        print("Liu can be seen as the polar opposite of Andre:\ndecent strength with superhuman accuracy.")
    elif choice == f_7:
        print("Kokoda, the late champion of MiniFight, was one\nof its most powerful fighter. He grow rusty.")
    elif choice == f_8:
        print("Ibrahim is an all round fighter, decent in strength\nand dexterity, with excellent accuracy.")
    elif choice == f_9:
        print("Miguel have the best dexterity of all fighters, a\nmortally dangerous grappler... but far too hasty!")
    elif choice == f_10:
        print("KONO DIO DA!")

def ringPres(choice):
    if choice == "Circle":
        print("The Circle is an utmost basic place to fight : you simply draw\na ring in the sand. No advantages nor setbacks.")
    elif choice == "Square":
        print("The Square is the boxing ring of choice. It's difficult for\nfighters to use their dexterity, but they can show off strength.")
    elif choice == "Rectangle":
        print("The Rectangle is an unusual ring : not as bad for dexterity\nas a Square, but not as good to show off strength.")
    elif choice == "Hexagon":
        print("The Hexagon is a decent ring to show off strength without\nlosing dexterity.")
    elif choice == "Octogon":
        print("The Octogon is the best ring to show off strength without\nlosing dexterity.")
    elif choice == "Pentagon":
        print("The gigantic Pentagon is the best ring to show off dexterity.")
    elif choice == "Street":
        print("On the street, you fight for your life... do not expect\nthat fighters will hold their blows.")

## INIT ##

print("""
    __  ____       _ _______       __    __ 
   /  |/  (_)___  (_) ____(_)___ _/ /_  / /_
  / /|_/ / / __ \/ / /_  / / __ `/ __ \/ __/
 / /  / / / / / / / __/ / / /_/ / / / / /_  
/_/  /_/_/_/ /_/_/_/   /_/\__, /_/ /_/\__/  
                         /____/             
""")
print("Made by Ashizian")
print("Welcome to Minifight {version}, the minimalist fighting game!".format(version=version))

## START ##

startAction = True
while startAction:

    ## HELP PROMPT ##

    help_prompt = True
    while help_prompt:
        helprep = input("Do you want to use the help for this game? (y/n) ")
        if helprep == "y" or helprep == "Y":
            print("Help as been set on")
            break
        elif helprep == "n" or helprep == "N":
            print("Help is set off")
            break
        else:
            error()

    ## CHARACTER SELECTION ##
    
    print("""
    You can choose between these nine fighters:
    1. Andre     4. James      7. Kokoda
    2. Jean      5. Chris      8. Ibrahim 
    3. Brick     6. Liu        9. Miguel     R. Random
    """)

    choice_a = input("Select your first fighter (use the number): ")
    fighter_one = fighterChoice(choice_a)
    print(fighter_one)
    if helprep == "y" or helprep == "Y":
        fighterPres(fighter_one)
        print(" ")
    else:
        pass
 
    choice_b = input("Select your second fighter (use the number): ")
    fighter_two = fighterChoice(choice_b)    
    print(fighter_two)
    if helprep == "y" or helprep == "Y":
        fighterPres(fighter_two)
        print(" ")
    else:
        pass

    ## RING SELECTION ##
    
    print("""
    You can now select a ring:
    1. Circle      4. Hexagon
    2. Square      5. Octogon
    3. Rectangle   6. Pentagon    R. Random
    """)
    choice_c = input("Use the number: ")
    choosen_ring = ringChoice(choice_c)
    print("You have choosen the {ring}".format(ring=choosen_ring))
    if helprep == "y" or helprep == "Y":
        ringPres(choosen_ring)
        print(" ")
    else:
        pass

    ## VARIABLES ##        

    fight = Ring(choosen_ring, fighter_one, fighter_two)
    fight.malus_bonus(choosen_ring, fighter_one, fighter_two)
    print("""
Welcome everyone! 
Our two brave warriors, {name_a} and {name_b}, have decided to manage their 
anger issues in the {kind}! 

Let's get ready to rumble!
    """.format(kind=choosen_ring, name_a=fighter_one.name, name_b=fighter_two.name))
    fight.fighting(fighter_one, fighter_two)
    startAction = False
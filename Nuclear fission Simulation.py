import turtle
#Initial COnditions 
First_Neutron_p = -750  # initial Position of the Thermal Neutron

First_Uranium_p = -250  # Posiiton of the Uranium Atom

second_Uranium_p = 100  # Posiiton of the Uranium Atom

Nuetron_speed = 3      # Neutron speed this the speed in which the initial Neutron moves.

Fission_range = (-290, -150)  # range of the nutroun ie when does the N hit the uranium atom and get absorbed.

 # range for the prmpot nutroun 

Fission_range_3=(100,200) # range for the prmpot nutroun 

# Labels for the fission fragments and the neutrons after the reaction
fragment_1_name = "Barium-141"
fragment_2_name = "Krypton-92"
Neutron1_Name = "Neutron 1"
Neutron2_Name = "Neutron 2"
Neutron3_Name = "Neutron 3"

#Function to set the moderator, initial Uranium and thermal Neutron
def setup_elements():
    screen = turtle.Screen()
    screen.title("Nuclear Fission") #give the siml a title 
    screen.bgcolor('white') #background
    
    neutron = create_particle(First_Neutron_p, 'red') # set the Thermal nutroun 
    create_label(First_Neutron_p + 50, -40, "Neutron", 'black', ('times new roman', 20, 'italic'))
    # Create the first uranium atom
    uranium = create_particle(First_Uranium_p, 'yellow', size=5)
    create_label(First_Uranium_p - 40, -85, 'Uranium-235', 'black', ('times new roman', 20, 'italic'))

    # Create the second uranium atom and it"s lable
    uranium2 = create_particle(second_Uranium_p, 'yellow', size=5)
    create_label(second_Uranium_p - 40, -85, 'Uranium-235', 'black', ('times new roman', 20, 'italic'))
    
    # Creating daughter particles for the first uranium atom 
    daughter1 = create_particle(First_Uranium_p, 'blue', size=2.5, angle=90)
    daughter2 = create_particle(First_Uranium_p, 'green', size=2.5, angle=-90)

    # Creating daughter particles for the second uranium atom 
    daughter1_2 = create_particle(second_Uranium_p, 'blue', size=2.5, angle=90)
    daughter2_2 = create_particle(second_Uranium_p, 'green', size=2.5, angle=-90)
    
    neutron = create_particle(First_Neutron_p, 'red')
    
    # create a  (rectangle) and position it between the uranium atoms as a moderator for the prompt Neutron getting out of the first atom 
    
    Mod= turtle.Turtle()
    Mod.shape("square")
    Mod.color("gray")  # Set the color of the square
    mid_x = (First_Uranium_p + second_Uranium_p) / 2  # Midpoint between the two uranium atoms
    Mod.penup()
    Mod.goto(mid_x, 0)  # Adjust y-coordinate as needed
    Mod.setheading(90) # make it vertical 
    Mod_size = abs(second_Uranium_p - First_Uranium_p) / 20  # Adjust the size factor as needed
    Mod.shapesize(stretch_wid=1, stretch_len=Mod_size)  # Stretch to make it more rectangular
    create_label(mid_x-45,200, "Moderator", 'black', ('times new roman', 20, 'italic'))

    
    return neutron, uranium, daughter1, daughter2, uranium2, daughter1_2, daughter2_2

# Function to create a particle
def create_particle(x, color, size=1, angle=0):
    particle = turtle.Turtle()
    particle.shape('circle')
    particle.color(color)
    particle.speed(0)
    particle.penup()
    particle.setx(x)
    particle.shapesize(size)
    particle.setheading(angle)
    return particle
# Function to create a label (in the set up elemnt ) 
def create_label(x, y, text, color, font):
    label = turtle.Turtle()
    label.hideturtle()
    label.speed(0)
    label.color(color)
    label.penup()
    label.setposition(x, y)
    label.write(text, font=font)
# Function to label the daughter particles
def label_daughters(daughters):
    daughters[0].hideturtle()
    daughters[1].hideturtle()
    create_label(daughters[0].xcor() - 25, daughters[0].ycor() + 30, fragment_1_name, 'black', ('times new roman', 15, 'italic'))
    create_label(daughters[1].xcor() - 25, daughters[1].ycor() - 50, fragment_2_name, 'black', ('times new roman', 15, 'italic'))
    daughters[0].showturtle()
    daughters[1].showturtle()
# Function to simulate fission
def simulate_fission(neutron, daughters, neutrons, labels):
    neutron.hideturtle()
    labels[0].clear()
    labels[1].clear()
   
    for daughter in daughters:
        daughter.showturtle()
        daughter.forward(200)
   
    for i in range(3):
        neutrons[i].showturtle()
        neutrons[i].forward(175)
        
    label_daughters(daughters)

# Main function
def main():
    turtle.speed(0)
    neutron, uranium, daughter1, daughter2, uranium2, daughter1_2, daughter2_2 = setup_elements()
    
    neutron1 = create_particle(First_Uranium_p, 'violet', size=1, angle=60)
    neutron2 = create_particle(First_Uranium_p, 'violet', size=1, angle=-60)
    neutron3 = create_particle(First_Uranium_p, 'red', size=1, angle=0)
    
    
    neutron4, neutron5, neutron6 = [create_particle(second_Uranium_p, 'violet', size=1, angle=angle) for angle in [60, -60, 0]]
    labels = [daughter1, daughter2] 

    # Move the initial neutron
    while neutron.xcor() < Fission_range[1]:
        neutron.forward(Nuetron_speed)
        if Fission_range[0] <= neutron.xcor() <= Fission_range[1]:
            simulate_fission(neutron, [daughter1, daughter2], [neutron1, neutron2, neutron3], labels)
            uranium.hideturtle()  # Hide the first uranium atom after collision 
            break
    # Move neutron3 with speed 1
    
    while neutron3.xcor() < Fission_range_3[1]:
        neutron3.forward(3)       
        
        
        if Fission_range_3[0] <= neutron3.xcor() <= Fission_range_3[1]:
           simulate_fission(neutron3, [daughter1_2, daughter2_2], [neutron4, neutron5, neutron6], labels)
           uranium2.hideturtle()
           break
                
    turtle.done()

if __name__ == "__main__":
    main()

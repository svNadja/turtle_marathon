
names =['mike','lui','ray','lana','may']

#create random color
def createColor ():

    arrayForcol = ['A','B','C','D','E', '1','4','6','2','7','8']
        
    import random
    color ='#'
    for i in range(6):
        val = random.choice(arrayForcol)
        color += val
    print(color)
    return color

from projekt6_haupt import make_finish_line
make_finish_line()

import turtle

class Teilnehmer:
  def __init__(self, name,color):
      self.name =name
      self.color = color
      self.turtle = turtle.Turtle()
      self.turtle.shape('turtle')
      self.turtle.color(self.color)

  def createTurtle(self,posX, posY):
       
        self.turtle.penup()
        self.turtle.goto(-500,posY)
        self.turtle.pendown()

  def move_turtle(self,steps,speed):

    self.turtle.forward(steps)
    self.turtle.speed(speed)
        
#CREATE TURTLES FOR EACH
participants = []
#for i in range(len(names)):
    #part_obj= Teilnehmer(names[i],createColor())
    #participants.append(part_obj)
    #part_obj.createTurtle(300 - 50*i)
participants = [Teilnehmer(name, createColor()) for name in names]
print(participants)

#random values for steps
def randSteps():
  import random
  
  steps = random.randint(10, 50)
  print('\n Steps:',steps)
  return steps

#random values for speed 
def randSpeed():
  import random
  numForSpeed = random.randint(3,11)
  print('\nSpeed:', numForSpeed)
  return numForSpeed

finish = 300
#start for mooving
while True: 
  for part_obj in participants:
    
      steps= randSteps()
      speed = randSpeed()
      part_obj.move_turtle(steps,speed)

      if part_obj.turtle.setpos(finish,None) == True :
         turtle.hideturtle()
         turtle.write(part_obj.name +'has won!')
      break
    

  turtle.done()
  turtle.mainloop()
     
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




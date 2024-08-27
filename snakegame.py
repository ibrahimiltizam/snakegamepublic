#Simple snake game

import turtle
import time
import random

delay = 0.1


#tampilan screen
sc = turtle.Screen()
sc.title  ("Game Ular pixel by @ibrhimiltzm")
sc.bgcolor ("black")
sc.setup (width= 600, height= 600)
sc.tracer(0) #Turn off the screen updates

# Kepala ular
kepala = turtle.Turtle()
kepala.speed(0)
kepala.shape("square")
kepala.color("green")
kepala.penup()
kepala.goto(0,1)
kepala.direction = "up"

#Makanan ular
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []


# Perintah bergerak
def go_up() :
    if kepala.direction != "down":
        kepala.direction ="up"

def go_down() :
    if kepala.direction != "up":
        kepala.direction ="down"

def go_right() :
    if kepala.direction != "left":
     kepala.direction ="right"

def go_left() :
    if kepala.direction != "right":
        kepala.direction ="left"

#instruksi bergerak
def move():
     if kepala.direction == "up" :
        y = kepala.ycor()
        kepala.sety(y + 20)
    
     if kepala.direction == "down" :
        y = kepala.ycor()
        kepala.sety(y - 20)

     if kepala.direction == "left" :
        x = kepala.xcor()
        kepala.setx(x - 20)

     if kepala.direction == "right" :
        x = kepala.xcor()
        kepala.setx( x + 20)
   
#perintah keyboards untuk interaksi game
sc.listen ()
sc.onkeypress(go_up, "w" )
sc.onkeypress(go_down, "s")
sc.onkeypress(go_right, "d")
sc.onkeypress(go_left, "a")
      
#Tampilan awal ular 
while True:
    sc.update()

    #Batas game ular
    if kepala.xcor()>290 or kepala.xcor()<-290 or kepala.ycor()>290 or kepala.ycor()<-290:
        time.sleep(1)
        kepala.goto(0,0)
        kepala.direction = "stop"

       


    #Tabrakan kepala ular dengan makanan
    if kepala.distance(food) < 20 :
        #memindahkan makanan ke tempat acak
        x = random.randint(-290, 290)
        y = random. randint(-290, 290)
        food.goto(x, y)

        #Menambahkan segment/ buntut
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#808000")
        new_segment.penup()
        segments.append(new_segment)

    
    #Bergerak dari segment akhir
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor() 
        segments[index].goto(x,y)

    # Bergerak dari segment 0 mengikuti kepala bergerak
    if len(segments) > 0:
        x = kepala.xcor()
        y = kepala.ycor()
        segments[0].goto(x,y)

    

    move()

    #kepala bertabrakan dengan badan
    for segment in segments:
        if segment.distance(kepala) < 20: 
            time.sleep(1)
            kepala.goto(0,0)
            kepala.direction = "stop"

         #menyebunyikan ekor dan badan
            for segment in segments:
                segment.goto(1000, 1000)

             #menghilangkan segments/ekor
            segments.clear()

            
    time.sleep(delay)
sc.mainloop()
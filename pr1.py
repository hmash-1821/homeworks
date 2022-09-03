from turtle import *

print("temo maghlakeldize")
print(5) #string   #str
print("5") #integer   #int

print(5 + int("5"))
print("5" + str(5))

#building a house

#square 
speed(30)
width(7)
color("brown") #color of the house walls
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(200)

#end of square

#door

left(90)
forward(80)
color("red") #color of the door
begin_fill()  #painting door with red color
left(90)
forward(70)  #height of the door
right(90)
forward(40)
right(90)
forward(70)
end_fill()

#end of door


#roof

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(140)
forward(160)
left(100)
forward(160)
end_fill()

#end of roof

#windows

#first window
penup()
goto(0, 0)
right(140)
forward(110)
right(90)
forward(30)
pendown()
color("brown")        
left(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

right(90)
forward(40)

#second window

penup()
goto(200, 200)
left(90)
forward(50)
right(90)
forward(30)
left(90)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)


exitonclick()
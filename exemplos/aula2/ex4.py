import turtle
import time

#conf
turtle.speed(1)

#I
turtle.pu()
turtle.goto(-200,200)
turtle.pd()
turtle.goto(-200,0)
turtle.goto((-200+25),0)
turtle.goto((-200+25),200)
turtle.goto(-200,200)
turtle.pd()

#N
turtle.pu()
turtle.goto(-170,200)
turtle.pd()
turtle.goto(-170,0)
turtle.goto((-170+25),0)
turtle.goto((-170+25),120)
turtle.goto((-170+50),0)
turtle.goto((-170+75),0)
turtle.goto((-170+75),200)
turtle.goto((-170+50),200)
turtle.goto((-170+50),80)
turtle.goto((-170+25),200)
turtle.goto((-170),200)

#F
turtle.pu()
turtle.goto(-90,200)
turtle.pd()
turtle.goto(-90,0)
turtle.goto((-90+25),0)
turtle.goto((-90+25),100)
turtle.goto((-90+50),100)
turtle.goto((-90+50),125)
turtle.goto((-90+25),125)
turtle.goto((-90+25),175)
turtle.goto((-90+75),175)
turtle.goto((-90+75),200)
turtle.goto((-90),200)

#O
turtle.pu()
turtle.goto(-10,200)
turtle.pd()
turtle.goto(-10,0)
turtle.goto((-10+75),0)
turtle.goto((-10+75),200)
turtle.goto((-10),200)
turtle.pu()
turtle.goto((-10+25),175)
turtle.pd()
turtle.goto((-10+25),25)
turtle.goto((-10+50),25)
turtle.goto((-10+50),175)
turtle.goto((-10+25),175)

#O
turtle.pu()
turtle.goto(70,200)
turtle.pd()
turtle.goto(85,100)
turtle.goto(70,0)
turtle.goto(95,0)
turtle.goto(105,85)
turtle.goto(115,0)
turtle.goto(140,0)
turtle.goto(125,100)
turtle.goto(140,200)
turtle.goto(115,200)
turtle.goto(105,95)
turtle.goto(95,200)
turtle.goto(70,200)

#O
turtle.pu()
turtle.goto(-200,-10)
turtle.pd()
turtle.goto(140,-10)
turtle.goto(140,-20)
turtle.goto(-200,-20)
turtle.goto(-200,-10)
time.sleep(100)

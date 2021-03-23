import turtle

turtle.setup(500,600) 

turtle.penup()
turtle.hideturtle()

#       STARS


a_X = -50
a_Y = -150

DEMEBOLA_X = -150
DEMEBOLA_Y = -150

ZOSMA_X = -50
ZOSMA_Y = -80

b_X = 30
b_Y = -80

ALGEIBA_X = 10
ALGEIBA_Y = 0


SICKLE_X = 30
SICKLE_Y = 30

e_X = 50
e_Y = 50

R_ELASED_X = 100
R_ELASED_Y = 60

c_X = 100
c_Y = -150

KEGULUS_X = 100
KEGULUS_Y = -200

#       STAR PLOT & NAME

# a
turtle.goto(a_X, a_Y)
turtle.dot()

# demebola
turtle.goto(DEMEBOLA_X, DEMEBOLA_Y)
turtle.dot()
turtle.write(' demebola ')

# zosma
turtle.goto(ZOSMA_X, ZOSMA_Y)
turtle.dot()
turtle.write(' zosma ')

# b
turtle.goto(b_X, b_Y)
turtle.dot()

# algeiba
turtle.goto(ALGEIBA_X, ALGEIBA_Y)
turtle.dot()
turtle.write(' algeiba ')

# the sickle
turtle.goto(SICKLE_X, SICKLE_Y)
turtle.dot()
turtle.write(' the sickle ')

# e
turtle.goto(e_X, e_Y)
turtle.dot()

# ras elased
turtle.goto(R_ELASED_X, R_ELASED_Y)
turtle.dot()
turtle.write(' ras elased ')

# c
turtle.goto(c_X,c_Y)
turtle.dot()

# kegulus
turtle.goto(KEGULUS_X,KEGULUS_Y)
turtle.dot()
turtle.write(' kegulus ')

#       DRAW AND CONNECT STARS
#
#       A --> DEMEBOLA
turtle.goto(a_X, a_Y)
turtle.pendown()
turtle.goto(DEMEBOLA_X, DEMEBOLA_Y)
turtle.penup()
#
#
#       DEMEBOLA --> ZOSMA
turtle.goto(DEMEBOLA_X, DEMEBOLA_Y)
turtle.pendown()
turtle.goto(ZOSMA_X, ZOSMA_Y)
turtle.penup()
#
#
#       ZOSMA --> B
turtle.goto(ZOSMA_X, ZOSMA_Y)
turtle.pendown()
turtle.goto(b_X, b_Y)
turtle.penup()
#
#
#       B --> ALGEIBA
turtle.goto(b_X, b_Y)
turtle.pendown()
turtle.goto(ALGEIBA_X, ALGEIBA_Y)
turtle.penup()
#
#
#       B --> C
turtle.goto(b_X, b_Y)
turtle.pendown()
turtle.goto(c_X,c_Y)
turtle.penup()
#
#
#       ALGEIBA --> THE SICKLE
turtle.goto(ALGEIBA_X, ALGEIBA_Y)
turtle.pendown()
turtle.goto(SICKLE_X, SICKLE_Y)
turtle.penup()
#
#
#       C --> KEGULUS
turtle.goto(c_X,c_Y)
turtle.pendown()
turtle.goto(KEGULUS_X,KEGULUS_Y)
turtle.penup()
#
#
#       THE SICKLE --> E
turtle.goto(SICKLE_X, SICKLE_Y)
turtle.pendown()
turtle.goto(e_X, e_Y)
turtle.penup()
#
#
#       E --> RAS ELASED
turtle.goto(e_X, e_Y)
turtle.pendown()
turtle.goto(R_ELASED_X, R_ELASED_Y)
turtle.penup()
#
#
#       KEGULUS --> A
turtle.goto(KEGULUS_X,KEGULUS_Y)
turtle.pendown()
turtle.goto(a_X, a_Y)
turtle.penup()



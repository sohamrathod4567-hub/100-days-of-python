import turtle

# -----------------------------
# Setup
# -----------------------------
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#FFF3D6")
screen.title("Lord Ganesha - Python Turtle")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# -----------------------------
# Helper functions
# -----------------------------
def circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def polygon(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)

    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()


def line(points, color, width=3):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.pencolor(color)
    t.pensize(width)

    for point in points[1:]:
        t.goto(point)


# -----------------------------
# Crown
# -----------------------------
polygon(
    [
        (-95, 240),
        (-70, 330),
        (-35, 285),
        (0, 350),
        (35, 285),
        (70, 330),
        (95, 240)
    ],
    "#F4B400"
)

# Crown decoration
circle(-45, 285, 10, "#E53935")
circle(0, 315, 13, "#43A047")
circle(45, 285, 10, "#E53935")


# -----------------------------
# Large ears
# -----------------------------
circle(-150, 120, 75, "#F2A65A")
circle(150, 120, 75, "#F2A65A")

# Inner ears
circle(-150, 120, 48, "#FFD09B")
circle(150, 120, 48, "#FFD09B")


# -----------------------------
# Head
# -----------------------------
circle(0, 140, 125, "#F2A65A")


# -----------------------------
# Eyes
# -----------------------------
circle(-48, 175, 17, "white")
circle(48, 175, 17, "white")

circle(-48, 175, 7, "black")
circle(48, 175, 7, "black")


# Eyebrows
line([(-70, 205), (-48, 215), (-25, 205)], "#5D4037", 5)
line([(25, 205), (48, 215), (70, 205)], "#5D4037", 5)


# -----------------------------
# Trunk
# -----------------------------
t.penup()
t.goto(0, 125)
t.setheading(-90)
t.pendown()

t.pencolor("#F2A65A")
t.pensize(42)

t.circle(70, 110)
t.circle(-45, 80)

# Trunk tip
circle(20, 40, 20, "#F2A65A")


# -----------------------------
# Tusks
# -----------------------------
polygon(
    [
        (-35, 105),
        (-85, 65),
        (-30, 75)
    ],
    "white"
)

polygon(
    [
        (35, 105),
        (85, 65),
        (30, 75)
    ],
    "white"
)


# -----------------------------
# Tilak
# -----------------------------
line([(-15, 235), (0, 255), (15, 235)], "#D32F2F", 6)
line([(-10, 245), (10, 245)], "#D32F2F", 5)


# -----------------------------
# Body
# -----------------------------
circle(0, -80, 150, "#F2A65A")


# Belly
circle(0, -120, 105, "#FFD09B")


# -----------------------------
# Arms
# -----------------------------
t.pensize(35)
t.pencolor("#F2A65A")

line(
    [(-100, -30), (-190, -80), (-210, -145)],
    "#F2A65A",
    35
)

line(
    [(100, -30), (190, -80), (210, -145)],
    "#F2A65A",
    35
)

# Hands
circle(-210, -145, 25, "#F2A65A")
circle(210, -145, 25, "#F2A65A")


# -----------------------------
# Modak
# -----------------------------
polygon(
    [
        (-245, -115),
        (-220, -80),
        (-195, -115),
        (-220, -160)
    ],
    "#D8892B"
)

# Modak lines
line([(-220, -150), (-220, -100)], "#8D5524", 3)
line([(-235, -135), (-220, -100)], "#8D5524", 3)
line([(-205, -135), (-220, -100)], "#8D5524", 3)


# -----------------------------
# Dhoti
# -----------------------------
polygon(
    [
        (-105, -210),
        (105, -210),
        (75, -310),
        (0, -275),
        (-75, -310)
    ],
    "#E53935"
)

# Dhoti decoration
line([(-75, -245), (0, -215), (75, -245)], "#F4B400", 8)


# -----------------------------
# Feet
# -----------------------------
circle(-70, -315, 38, "#F2A65A")
circle(70, -315, 38, "#F2A65A")


# -----------------------------
# Mouse (Vahana)
# -----------------------------
circle(0, -355, 35, "#555555")

# Mouse ears
circle(-25, -325, 15, "#555555")
circle(25, -325, 15, "#555555")

# Mouse eyes
circle(-12, -355, 4, "white")
circle(12, -355, 4, "white")

# Mouse nose
circle(0, -375, 6, "black")


# -----------------------------
# Decorative base
# -----------------------------
polygon(
    [
        (-260, -395),
        (260, -395),
        (230, -350),
        (-230, -350)
    ],
    "#F4B400"
)

# Base decoration
circle(-190, -375, 8, "#E53935")
circle(-95, -375, 8, "#43A047")
circle(0, -375, 8, "#E53935")
circle(95, -375, 8, "#43A047")
circle(190, -375, 8, "#E53935")


# -----------------------------
# Finish
# -----------------------------
turtle.done()
# Tízszög rajzolás - Tóth kevin Dorián MAXEBH

import turtle
while True:
    meret_input = input("Add meg az oldal hosszát (csak pozitív egész szám): ")
    if meret_input.isdigit() and int(meret_input) > 0:
        meret = int(meret_input)
        break
    else:
        print("Hibás adat, kérlek próbáld újra!")

ablak = turtle.Screen()
ablak.title("Szabályos tízszög")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(5)
t.penup()
t.goto(-meret/2, -meret/2)  # kb. középre igazít
t.pendown()


# Szabályos tízszög
for _ in range(10):
    t.forward(meret)
    t.left(36)   # 360 / 10 = 36 fok

ablak.exitonclick()

#TKD+MAXEBH

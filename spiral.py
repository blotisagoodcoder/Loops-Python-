import turtle

s = turtle.Screen()
s.bgcolor("light blue")
s.title("HELLO MORTAL BEINGS!")
s = turtle.Turtle()
size=0
while True:
  for i in range(4):
    s.fd(size+1)
    s.left(90)
    size = size - 5
    size = size + 1
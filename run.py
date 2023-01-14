from turtle import *



bgcolor("black")
speed(0)
colors = ['white', 'red']

for i in range (180):
      pencolor(colors[i%len(colors)])
      rt(i)
      circle(100,i)
      fd(i)
      rt(180)
      fd(i)



mainloop()

import turtle

# 거북이 초기화
t = turtle.Turtle()
t.speed(3)  # 거북이 속도 설정


# screen = turtle.Screen()
# screen.addshape('a.png')
# t.shape('a.png')
# screen.mainloop()
# s = turtle.Shape("image")
# poly1 = ((0, 0), (10, -5), (0, 10), (-10, -5))
# s.addcomponent(poly1, "yellow", "black")
# poly2 = ((0, 0), (10, -5), (-10, -5))
# s.addcomponent(poly2, "blue", "red")
turtle.register_shape('trumph.gif')
t.shape('trumph.gif')


def draw_star():

    for steps in range(5):
        for c in ('blue', 'red', 'green'):
            t.color(c)
            t.forward(steps)
            t.right(30)

    # t.color('red')

    turtle.fillcolor('yellow')
    turtle.begin_fill()

    count = 0

    while True:
        t.forward(100)
        if count % 12 == 0:
            t.left(30)
        else:
            if count % 2 == 0:
                t.right(120)
            else:
                t.left(60)
        count += 1
        if abs(t.pos()) < 1:
            break

        # if count == 36:
        #     break

    turtle.end_fill()


# 거북이 위치 설정
t.penup()
t.goto(-100, 0)  # 시작 위치 설정
t.pendown()

# 별 그리기
draw_star()

# 창 유지
turtle.done()

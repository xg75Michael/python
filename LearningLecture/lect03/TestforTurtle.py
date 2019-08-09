"""
    作者： Michael Gao
    功能： 具体测试各种方法
    日期： 18／11／2018
"""

import turtle


def turn(x, y):
    turtle.left(180)


def main():
    """
        主函数
    """
    # turtle.fd(100)
    # turtle.pu()
    # turtle.lt(60)
    # turtle.bk(100)
    # turtle.pd()
    # turtle.rt(60)
    # turtle.fd(100)
    #
    # turtle.setposition(100, 100)
    # turtle.dot(30, 'green')
    # turtle.setx(50)
    # turtle.sety(50)
    # turtle.seth(90)
    # print(turtle.heading())
    # print(turtle.ycor())
    # print(round(turtle.ycor(), 5))
    # turtle.home()

    # turtle.circle(100)
    #
    # for i in range(4):
    #     turtle.bk(50)
    #     turtle.lt(80)
    # for i in range(8):
    #     turtle.undo()

    turtle.goto(30, 30)
    print(turtle.towards(0, 0))
    print(turtle.distance(0, 0))
    turtle.fillcolor('blue')

    turtle.color("black", "green")
    turtle.begin_fill()
    turtle.circle(-20)
    turtle.end_fill()

    turtle.hideturtle()
    print(turtle.isvisible())
    turtle.showturtle()
    turtle.shape('circle')
    turtle.setpos(-100, -100)
    turtle.shape('turtle')

    turtle.resizemode('auto')
    turtle.pensize(7)
    turtle.fd(200)

    turtle.shape('circle')
    turtle.shapesize(5, 2)
    turtle.shearfactor(0)

    turtle.shape('square')
    turtle.shapesize(4, 2)
    turtle.shearfactor(-0.5)
    print(turtle.shapetransform())

    turtle.onclick(turn)

    turtle.exitonclick()


if __name__ == '__main__':
    main()







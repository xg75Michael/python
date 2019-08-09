"""
    作者： Michael Gao
    功能： 自画像
    日期： 18／11／2018
"""

import turtle


def main():
    """
        主函数
    """
    turtle.speed('slow')
    turtle.pensize(5)
    turtle.pu()
    turtle.fd(30)
    turtle.pd()
    turtle.fd(30)
    turtle.pu()
    turtle.bk(90)
    turtle.pd()
    turtle.bk(30)
    turtle.pu()
    turtle.setpos(-20, -60)
    turtle.pensize(7)
    turtle.color('red')
    turtle.pd()
    turtle.fd(40)

    turtle.color('black')
    turtle.pensize(3)
    turtle.pu()
    turtle.setpos(0, -130)
    turtle.pd()
    turtle.circle(100)
    turtle.pu()

    turtle.exitonclick()


if __name__ == '__main__':
    main()







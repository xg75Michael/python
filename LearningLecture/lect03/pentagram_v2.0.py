"""
    作者： Michael Gao
    功能： 五角星的绘制
    版本： 2.0
    日期： 16／11／2018
    新增功能： 加入循环操作来绘制大小不同的五角星
"""

import turtle


def dram_pentagram(size):
    count = 1
    """
        绘制五角星
    """
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1


def main():
    """
        主函数
    """

    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(0.1)
    turtle.pencolor('red')
    turtle.speed(0)

    size = 100

    while size <= 300:
        # 调用函数
        dram_pentagram(size)
        size += 40

    turtle.exitonclick()


if __name__ == '__main__':
    main()







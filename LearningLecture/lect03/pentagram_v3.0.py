"""
    作者： Michael Gao
    功能： 五角星的绘制
    版本： 3.0
    日期： 18／11／2018
    新增功能： 加入循环操作来绘制大小不同的五角星
    新增功能： 使用迭代汗水绘制大小不同的五角星
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


def draw_recursive_pentagram(size):
    """
        主函数
    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1
    # 五角星绘制完成，更行参数
    size += 40
    if size <= 300:
        draw_recursive_pentagram(size)


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
    draw_recursive_pentagram(size)

    turtle.exitonclick()


if __name__ == '__main__':
    main()







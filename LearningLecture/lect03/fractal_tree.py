"""
    作者： Michael Gao
    功能： 分形树-递归函数
    版本： 1.0
    日期： 18／11／2018
"""

import turtle


def draw_branch(branch_length):
    """
        绘制分形树
    """
    if branch_length > 5:

        if 5 < branch_length < 30:
            turtle.color('green')
        else:
            turtle.color('brown')

        if 70 < branch_length <= 100:
            turtle.pensize(3)
        elif 40 < branch_length <= 70:
            turtle.pensize(2)
        else:
            turtle.pensize(1)

        # 绘制右侧的树枝
        turtle.forward(branch_length)
        print('向前 branch_length ', branch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length - 15)

        # 返回之前的树枝
        turtle.right(20)
        print('右转 20')
        turtle.backward(branch_length)
        print('向后 ', branch_length)


def main():
    """
        主函数
    """

    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.speed(0)

    draw_branch(100)

    turtle.exitonclick()


if __name__ == '__main__':
    main()







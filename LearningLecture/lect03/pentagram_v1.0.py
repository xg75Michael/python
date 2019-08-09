"""
    作者： Michael Gao
    功能： 五角星的绘制
    版本： 1.0
    日期： 16／11／2018
          已个人加入循环功能
"""

import turtle


def main():
    """
        主函数
    """
    # 计数器
    count = 1
    loopcircle = 1
    forwardvalue = 300
    turningrate = 144

    while loopcircle <= 4:

        while count <= 5:

            turtle.forward(forwardvalue)
            turtle.right(turningrate)

            count = count + 1

        forwardvalue = forwardvalue - 50
        loopcircle = loopcircle + 1
        count = 1

    turtle.exitonclick()


if __name__ == '__main__':
    main()







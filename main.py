"""游戏的入口"""
import sys

import pygame
from my_plane import MyPlane

class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""

        # 初始化pygame库
        pygame.init()

        screen_width = 700
        screen_height = 900
        # 创建指定尺寸的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        self.window = pygame.display.set_mode([screen_width, screen_height])

        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")

        # 加载窗口图标
        window_icon = pygame.image.load('images/s1.ico')

        # 设置窗口的图标
        pygame.display.set_icon(window_icon)

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.window, (299, 824))

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

    def run_game(self):
        """运行游戏"""

        # 让创建的窗口一直显示
        while True:
            # 从事件队列中将所有事件全部取出并逐个进行处理
            for event in pygame.event.get():
                # 如果某个事件是退出程序
                if event.type == pygame.QUIT:
                    # 卸载pygame库
                    pygame.quit()
                    # 退出程序
                    sys.exit()

            # 设置窗口的背景色
            self.window.fill(pygame.Color('gray'))

            # 在窗口中绘制我方飞机
            self.my_plane.draw()

            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()

            # 更新我方飞机的位置
            self.my_plane.update()

            # 设置while循环体在一秒内执行的最大次数（设置动画的最大帧率）
            self.clock.tick(10)

# 只有当直接运行main.py时
if __name__ == '__main__':
    PlaneWar().run_game()

"""我方飞机"""
import pygame

class MyPlane:
    """我方飞机类"""

    def __init__(self, window, pos):
        """初始化我方飞机"""

        # 获得窗口对象
        self.window = window

        # 获得我方飞机的位置
        self.pos_x, self.pos_y = pos

        # 加载我方飞机图片
        self.image = pygame.image.load('images/my_plane.png')

    def update(self):
        """更新我方飞机的位置"""

        # 减少我方飞机的y坐标以向上移动
        self.pos_y -= 20

    def draw(self):
        """在窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, (self.pos_x, self.pos_y))
"""子弹"""
import pygame

class Bullet:
    """子弹类"""

    def __init__(self, window, my_plane):
        """初始化子弹"""

        # 获得窗口对象
        self.window = window

        # 加载子弹图片
        self.image = pygame.image.load('images/bullet.png')

        # 获取子弹的矩形
        self.image.get_rect()

        # 获得我方飞机的的矩形
        self.my_plane_rect = my_plane.rect

        # 设置子弹的矩形的初始位置为：我方飞机的矩形的顶部居中位置
        self.rect.midtop = self.my_plane_rect.midtop

        # 子弹每次移动时的偏移量
        self.offset = 50

    def update(self):
        """更新子弹的位置"""

        self.rect.top -= self.offset

    def draw(self):
        """在窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, self.rect)
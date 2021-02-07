"""大型敌机"""
import random
import pygame

class BigEnemy:
    """大型敌机类"""

    def __init__(self, window):
        """初始化大型敌机"""

        # 获得窗口对象
        self.window = window

        # 加载大型敌机图片
        self.image = pygame.image.load("images/big_enemy.png")

        # 获得大型敌机的矩形
        self.rect = self.image.get_rect()

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 设置大型敌机的矩形的初始位置为：窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width -
                                        self.rect.width)

        # 大型敌机每次移动时的偏移量
        self.offset = 5

    def update(self):
        """更新大型敌机的位置"""

        # 增大大型敌机的矩形的属性top以向下移动
        self.rect.top += self.offset

    def draw(self):
        """在窗口中绘制大型敌机"""

        # 在窗口的指定位置绘制一架大型敌机
        self.window.blit(self.image, self.rect)
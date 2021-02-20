"""中型敌机"""

import random
import pygame
from pygame.sprite import Sprite
import constants

class MidEnemy(Sprite):
    """中型敌机类"""

    def __init__(self, window):
        """初始化中型敌机"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象
        self.window = window

        # 加载中型敌机图片
        self.image = self.mid_image = pygame.image.load("images/mid_enemy.png")

        # 加载小型敌机爆炸的第1张图片
        self.explode_image1 = pygame.image.load("images/mid_enemy_explode1.png")

        # 加载小型敌机爆炸的第2张图片
        self.explode_image2 = pygame.image.load("images/mid_enemy_explode2.png")

        # 加载小型敌机爆炸的第3张图片
        self.explode_image3 = pygame.image.load("images/mid_enemy_explode3.png")

        # 加载小型敌机爆炸的第4张图片
        self.explode_image4 = pygame.image.load("images/mid_enemy_explode4.png")

        # 获得中型敌机的矩形
        self.rect = self.image.get_rect()

        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()

        # 设置中型敌机的矩形的初始位置为：窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width -
                                        self.rect.width)

        # 中型敌机每次移动时的偏移量
        self.offset = 5

        # 标记中型敌机没有在切换爆炸图片
        self.is_switching_explode_image = False

        # 切换中型敌机爆炸图片的计数器
        self.switch_explode_counter = 0

        # 中型敌机的能量
        self.energy = 5

    def update(self):
        """更新中型敌机的位置"""

        # 增大中型敌机的矩形的属性top以向下移动
        self.rect.top += self.offset

    def play_explode_sound(self):
        """播放中型敌机爆炸的声音"""

        # 加载中型敌机爆炸的声音文件
        explode_sound = pygame.mixer.Sound("sounds/mid_enemy_explode.wav")

        # 设置爆炸声音的音量
        explode_sound.set_volume(constants.EXPLODE_SOUND_VOLUME)

        # 播放爆炸的声音
        explode_sound.play()

    def switch_explode_image(self):
        """切换中型敌机爆炸的图片"""

        # 切换中型敌机爆炸图片的计数器加1
        self.switch_explode_counter += 1

        # 如果计数器加到指定的值，才切换一次中型敌机爆炸的图片
        if self.switch_explode_counter == \
                constants.MID_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY:
            # 如果是中型敌机的图片
            if self.image == self.mid_image:
                # 切换到爆炸的第1张图片
                self.image = self.explode_image1
            # 如果是爆炸的第1张图片
            elif self.image == self.explode_image1:
                # 切换到爆炸的第2张图片
                self.image = self.explode_image2
            # 如果是爆炸的第2张图片
            elif self.image == self.explode_image2:
                # 切换到爆炸的第3张图片
                self.image = self.explode_image3
            # 如果是爆炸的第3张图片
            elif self.image == self.explode_image3:
                # 切换到爆炸的第4张图片
                self.image = self.explode_image4
            # 如果是爆炸的第4张图片
            elif self.image == self.explode_image4:
                # 将中型敌机从所有分组中删除
                self.kill()

            # 计数器重置为0
            self.switch_explode_counter = 0

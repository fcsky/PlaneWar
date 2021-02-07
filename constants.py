"""所有常量"""

import pygame


# 在水平方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5
# 在竖直方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5

# 动画的最大帧率
MAX_FRAMERATE = 10

# 自定义事件"创建子弹"的id
ID_OF_CREATE_BULLET = pygame.USEREVENT
# 自定义事件"创建小型敌机"的id
ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1
# 自定义事件"创建中型敌机"的id
ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2
# 自定义事件"创建大型敌机"的id
ID_OF_CREATE_BIG_ENEMY = pygame.USEREVENT + 3

# 自定义事件"创建子弹"时间间隔
INTERVAL_OF_CREATE_BULLET = 500
# 自定义事件"创建小型敌机"的时间间隔
INTERVAL_OF_CREATE_SMALL_ENEMY = 2000
# 自定义事件"创建中型敌机"的时间间隔
INTERVAL_OF_CREATE_MID_ENEMY = 3600
# 自定义事件"创建大型敌机"的时间间隔
INTERVAL_OF_CREATE_BIG_ENEMY = 18000
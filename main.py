"""游戏的入口"""
import sys

import pygame
from my_plane import MyPlane
from bullet import Bullet
from small_enemy import SmallEnemy
from mid_enemy import MidEnemy
from big_enemy import BigEnemy
from pygame.sprite import Group
import constants


class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""

        # 初始化pygame库
        pygame.init()

        # 创建窗口
        self._create_window()

        # 设置窗口
        self._set_window()

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.window)

        # 创建管理精灵的分组
        self._create_groups()

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

        # 设置定时器
        self._set_timers()

    def get_screen_size(self):
        """获取当前电脑屏幕的尺寸"""

        # 创建一个视频显示信息对象
        info = pygame.display.Info()
        # 获得当前电脑屏幕的宽度
        screen_width = info.current_w
        # 获得当前电脑屏幕的高度
        screen_height = info.current_h

        # 返回当前电脑屏幕的尺寸
        return screen_width, screen_height

    def _create_window(self):
        """创建窗口"""

        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_size()

        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * \
                                      constants.SCALE_HORIZONTAL, \
                                      screen_height * \
                                      constants.SCALE_VERTICAL

        # 创建指定尺寸的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        self.window = pygame.display.set_mode((round(window_width), round(window_height)))

        # 创建全屏模式的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        # self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def _set_window(self):
        """设置窗口"""

        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")

        # 加载窗口图标
        window_icon = pygame.image.load('images/s1.ico')

        # 设置窗口的图标
        pygame.display.set_icon(window_icon)

    def _create_groups(self):
        """创建管理精灵的分组"""

        # 创建一个管理所有子弹的分组
        self.bullet_group = Group()

        # 创建一个管理所有小型敌机的分组
        self.small_enemy_group = Group()

        # 创建一个管理所有中型敌机的分组
        self.mid_enemy_group = Group()

        # 创建一个管理所有大型敌机的分组
        self.big_enemy_group = Group()

        # 创建一个管理所有敌机的分组
        self.enemy_group =  Group()

    def _set_timers(self):
        """设置定时器"""

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建子弹"
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET,
                              constants.INTERVAL_OF_CREATE_BULLET)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建小型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_SMALL_ENEMY,
                              constants.INTERVAL_OF_CREATE_SMALL_ENEMY)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建中型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_MID_ENEMY,
                              constants.INTERVAL_OF_CREATE_MID_ENEMY)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建大型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_BIG_ENEMY,
                              constants.INTERVAL_OF_CREATE_BIG_ENEMY)

    def run_game(self):
        """运行游戏"""

        # 让创建的窗口一直显示
        while True:
            # 处理事件
            self._handle_events()

            # 设置窗口的背景色
            self.window.fill(pygame.Color('gray'))

            # 在窗口中绘制所有画面元素
            self._draw_elements()

            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()

            # 更新窗口中所有画面元素的位置
            self._update_positions()

            # 删除窗口中所有不可见的画面元素
            self._delete_invisible_elements()

            # 设置while循环体在一秒内执行的最大次数（设置动画的最大帧率）
            self.clock.tick(constants.MAX_FRAMERATE)

    def _handle_events(self):
        """处理事件"""

        # 从事件队列中将所有事件全部取出并逐个进行处理
        for event in pygame.event.get():
            # 如果某个事件是退出程序
            if event.type == pygame.QUIT:
                # 卸载 pygame 库
                pygame.quit()
                # 退出程序
                sys.exit()
            # 如果某个事件是用户按下了键盘上的某个键
            elif event.type == pygame.KEYDOWN:
                # 处理键盘按下的事件
                self._handle_keydown_events(event)
            # 如果某个事件是用户松开了键盘上的某个键
            elif event.type == pygame.KEYUP:
                # 处理键盘松开的事件
                self._handle_keyup_events(event)
            # 如果某个事件是自定义事件"创建子弹"
            elif event.type == constants.ID_OF_CREATE_BULLET:
                # 创建一颗子弹
                bullet = Bullet(self.window, self.my_plane)
                # 将创建的子弹添加到子弹分组中
                self.bullet_group.add(bullet)
            # 如果某个事件是自定义事件"创建小型敌机"
            elif event.type == constants.ID_OF_CREATE_SMALL_ENEMY:
                # 创建一架小型敌机
                small_enemy = SmallEnemy(self.window)
                # 将创建的小型敌机添加到小型敌机分组中
                self.small_enemy_group.add(small_enemy)
                # 将创建的小型敌机添加到管理所有敌机分组中
                self.enemy_group.add(small_enemy)
            # 如果某个事件是自定义事件"创建中型敌机"
            elif event.type == constants.ID_OF_CREATE_MID_ENEMY:
                # 创建一架中型敌机
                mid_enemy = MidEnemy(self.window)
                # 将创建的中型敌机添加到中型敌机分组中
                self.mid_enemy_group.add(mid_enemy)
                # 将创建的中型敌机添加到管理所有敌机分组中
                self.enemy_group.add(mid_enemy)
            # 如果某个事件是自定义事件"创建大型敌机"
            elif event.type == constants.ID_OF_CREATE_BIG_ENEMY:
                # 创建一架大型敌机
                big_enemy = BigEnemy(self.window)
                # 将创建的大型敌机添加到大型敌机分组中
                self.big_enemy_group.add(big_enemy)
                # 将创建的大型敌机添加到管理所有敌机分组中
                self.enemy_group.add(big_enemy)

    def _handle_keydown_events(self, event):
        """处理键盘按下的事件"""

        # 如果按下的键是上箭头
        if event.key == pygame.K_UP:
            # 标记我方飞机向上移动
            self.my_plane.is_move_up = True
        # 如果按下的键是下箭头
        elif event.key == pygame.K_DOWN:
            # 标记我方飞机向下移动
            self.my_plane.is_move_down = True
        # 如果按下的键是左箭头
        elif event.key == pygame.K_LEFT:
            # 标记我方飞机向左移动
            self.my_plane.is_move_left = True
        # 如果按下的键是右箭头
        elif event.key == pygame.K_RIGHT:
            # 标记我方飞机向右移动
            self.my_plane.is_move_right = True
        # 如果按下的键是Esc键
        elif event.key == pygame.K_ESCAPE:
            # 卸载pygame库
            pygame.quit()
            # 退出游戏
            sys.exit()

    def _handle_keyup_events(self, event):
        """处理键盘松开的事件"""

        # 如果松开的键是上箭头
        if event.key == pygame.K_UP:
            # 标记我方飞机不向上移动
            self.my_plane.is_move_up = False
        # 如果松开的键是下箭头
        elif event.key == pygame.K_DOWN:
            # 标记我方飞机不向下移动
            self.my_plane.is_move_down = False
        # 如果松开的键是左箭头
        elif event.key == pygame.K_LEFT:
            # 标记我方飞机不向左移动
            self.my_plane.is_move_left = False
        # 如果松开的键是右箭头
        elif event.key == pygame.K_RIGHT:
            # 标记我方飞机不向右移动
            self.my_plane.is_move_right = False

    def _draw_elements(self):
        """在窗口中绘制所有画面元素"""

        # 在窗口中绘制我方飞机
        self.my_plane.draw()

        # 在窗口中绘制所有子弹
        self.bullet_group.draw(self.window)

        # 在窗口中绘制所有小型敌机
        self.small_enemy_group.draw(self.window)

        # 在窗口中绘制所有中型敌机
        self.mid_enemy_group.draw(self.window)

        # 在窗口中绘制所有大型敌机
        self.big_enemy_group.draw(self.window)

    def _update_positions(self):
        """更新窗口中所有画面元素的位置"""

        # 更新我方飞机的位置
        self.my_plane.update()

        # 更新所有子弹的位置
        self.bullet_group.update()

        # 更新所有小型敌机的位置
        self.small_enemy_group.update()

        # 更新所有中型敌机的位置
        self.mid_enemy_group.update()

        # 更新所有大型敌机的位置
        self.big_enemy_group.update()

    def _delete_invisible_elements(self):
        """删除窗口中所有不可见的画面元素"""

        # 删除窗口中所有不可见的子弹
        self._delete_invisible_bullets()

        # 删除窗口中所有不可见的敌机
        self._delete_invisible_enemies()

    def _delete_invisible_bullets(self):
        """删除窗口中所有不可见的子弹"""

        # 遍历子弹的列表
        for bullet in self.bullet_group.sprites():
            # 如果某颗子弹在窗口中不可见了
            if bullet.rect.bottom <= 0:
                # 从子弹列表中删除该颗子弹
                self.bullet_group.remove(bullet)

    def _delete_invisible_enemies(self):
        """删除窗口中所有不可见的敌机"""

        # 遍历管理所有敌机的分组
        for enemy in self.enemy_group.sprites():
            # 如果某架敌机在窗口中不可见了
            if enemy.rect.top >= self.window.get_rect().height:
                # 将该架敌机从管理它的所有分组中删除
                enemy.kill()


if __name__ == '__main__':
    """只有当直接运行main.py时"""

    # 运行游戏
    PlaneWar().run_game()

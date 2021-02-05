"""游戏的入口"""
import sys

import pygame
from my_plane import MyPlane

# 在水平方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_HORIZONTAL = 2 / 5
# 在竖直方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5

# 动画的最大帧率
MAX_FRAMERATE = 10

class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""

        # 初始化pygame库
        pygame.init()

        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_siz()
        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * SCALE_HORIZONTAL, screen_height * SCALE_VERTICAL
        # 创建指定尺寸的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        self.window = pygame.display.set_mode((round(window_width), round(window_height)))

        # 创建全屏模式的窗口（游戏画面的所有元素都将在创建的这个窗口中绘制）
        # pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # 设置窗口
        self._set_window()

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.window)

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

    def get_screen_siz(self):
        """获取当前电脑屏幕的尺寸"""

        # 创建一个视频显示信息对象
        info = pygame.display.Info()
        # 获得当前电脑屏幕的宽度
        screen_width = info.current_w
        # 获得当前电脑屏幕的高度
        screen_height = info.current_h

        # 返回当前电脑屏幕的尺寸
        return screen_width, screen_height

    def _set_window(self):
        """设置窗口"""

        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")

        # 加载窗口图标
        window_icon = pygame.image.load('images/s1.ico')

        # 设置窗口的图标
        pygame.display.set_icon(window_icon)

    def run_game(self):
        """运行游戏"""

        # 让创建的窗口一直显示
        while True:
            # 处理事件
            self._handle_events()

            # 设置窗口的背景色
            self.window.fill(pygame.Color('gray'))

            # 在窗口中绘制我方飞机
            self.my_plane.draw()

            # 将内存中的窗口对象绘制到屏幕上以更新屏幕
            pygame.display.flip()

            # 更新我方飞机的位置
            self.my_plane.update()

            # 设置while循环体在一秒内执行的最大次数（设置动画的最大帧率）
            self.clock.tick(MAX_FRAMERATE)

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
        elif

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


# 只有当直接运行main.py时
if __name__ == '__main__':
    PlaneWar().run_game()

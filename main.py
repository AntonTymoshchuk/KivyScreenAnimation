from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager


class MyLayout(RelativeLayout):
    def __init__(self, **kwargs):
        RelativeLayout.__init__(self, **kwargs)


class AnimationButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)
        self.change_values = [15, 5]
        Clock.schedule_interval(self.update_method, 1 / 120)

    def update_method(self, *args):
        if self.x < 0 or (self.x + self.width) > Window.width:
            self.change_values[0] *= -1
        if self.y < 0 or (self.y + self.height) > Window.height:
            self.change_values[1] *= -1

        self.x += self.change_values[0]
        self.y += self.change_values[1]


class FiButton(Button):
    def __init__(self, **kwargs):
        Button.__init__(self, **kwargs)

    def animate(self):
        Animation.cancel_all(self)
        animation = Animation(width=self.width+50, height=self.height+50,
                              x=self.x-25, y=self.y-25, duration=1,
                              t='out_elastic')
        animation.start(self)


# class ScreenAnimationApp(App):
#     def build(self):
#         return MyLayout()


class HelloScreen(Screen):
    pass


class OllehScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class ReenApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    ReenApp().run()

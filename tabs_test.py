from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar
# from kivy.uix.button import Button
from kivy.garden.androidtabs import AndroidTabsBase, AndroidTabs


Builder.load_string('''
<Tab1>:
    canvas:
        Color:
            rgba: .5, 0, .5, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "rollan!"

<Tab2>:
    canvas:
        Color:
            rgba: 0, .5, .5, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: "reagan!"

<Bar>:
    pos_hint: {'top':1}
    ActionView:
        use_separator: True
        ActionPrevious:
            title: 'Nostra Plata'
            with_previous: False
        ActionOverflow:
        ActionButton:
            text: 'Btn1'

# <AndroidTabsBar>:
#     canvas:
#         Color:
#             rgba: 0,0,0,.3
#         Rectangle:
#             pos: self.pos[0], self.pos[1] - 1
#             size: self.size[0], 1
#         Color:
#             rgba: 0,0,0,.2
#         Rectangle:
#             pos: self.pos[0], self.pos[1] - 2
#             size: self.size[0], 1
#         Color:
#             rgba: 0,0,0,.05
#         Rectangle:
#             pos: self.pos[0], self.pos[1] - 3
#             size: self.size[0], 1
''')


class Tab1(BoxLayout, AndroidTabsBase):
    pass


class Tab2(BoxLayout, AndroidTabsBase):
    pass


class Bar(ActionBar):
    pass


class Example(App):

    def build(self):
        bar = Bar()

        android_tabs = AndroidTabs()
        tab1 = Tab1(text="Status")
        tab2 = Tab2(text="History")

        android_tabs.add_widget(tab1)
        android_tabs.add_widget(tab2)

        main_screen = BoxLayout(orientation="vertical")
        main_screen.add_widget(bar)
        main_screen.add_widget(android_tabs)

        return main_screen

app = Example()
app.run()

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.factory import Factory

from kivymd.toast import toast
from kivymd.theming import ThemeManager
from kivymd.uix.useranimationcard import MDUserAnimationCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch

# Your content for a contact card.
Builder.load_string('''
#:import get_hex_from_color kivy.utils.get_hex_from_color


<TestAnimationCard@MDBoxLayout>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    adaptive_height: True

    MDBoxLayout:
        adaptive_height: True

        Widget:
        MDRoundFlatButton:
            text: "Free call"
        Widget:
        MDRoundFlatButton:
            text: "Free message"
        Widget:

    OneLineIconListItem:
        text: "Video call"
        IconLeftSampleWidget:
            icon: 'camera-front-variant'

    TwoLineIconListItem:
        text: "Call Viber Out"
        secondary_text: "[color=%s]Advantageous rates for calls[/color]" % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'phone'

    TwoLineIconListItem:
        text: "Call over mobile network"
        secondary_text: "[color=%s]Operator's tariffs apply[/color]" % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'remote'
''')


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class Example(MDApp):
    title = "Example Animation Card"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_animation_card = None

    def build(self):
        def main_back_callback():
            toast('Close card')

        if not self.user_animation_card:
            self.user_animation_card = MDUserAnimationCard(
                user_name="Lion Lion",
                path_to_avatar="./assets/african-lion-951778_1280.jpg",
                callback=main_back_callback)
            self.user_animation_card.box_content.add_widget(
                Factory.TestAnimationCard())
        self.user_animation_card.open()


Example().run()
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton,MDRectangleFlatButton
#from kivymd.uix.textfield import MDTextField
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
#builser part
username_helper = """
MDTextField:
    hint_text:"Enter user name"
    helper_text:"or click on forgotusername"
    helper_text_mode:"on_focus"
    pos_hint:{'center_x':0.5,'center_y':0.5}
    icon_rifght_color:app.theme_cls.primary_color
    size_hint_x:None
    width:300

    icon_right:"language-python"
"""


class Demo(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"
        sc = Screen()
        #username = MDTextField(text="enter user name",pos_hint={'center_x':0.5,'center_y':0.5},size_hint_x=None,width=300)
        #user input buider method
        self.username = Builder.load_string(username_helper)

        #theme is a property where evry element will have the color specified heere
        #self.theme_cls.primary_palette="Green"
        #self.theme_cls.theme_style="Dark"

        #buttons
        bt = MDRectangleFlatButton(text="Show",pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)
        #label=MDLabel(text="first text",halign='center',theme_text_color='Custom',text_color=(0,1,0,1),font_style='H1')
        #coloring the label with theme_text_color='colorname'
        #or with custom color theme_text_color='Custom'
        #lab=MDIcon(icon='language-python')
        sc.add_widget(self.username)
        sc.add_widget(bt)
        return sc
    def show_data(self,obj):
        dailog = MDDialog(text=self.username.text,title="username check",size_hint=(0.5,0.5))
        dailog.open()

if __name__=="__main__":
    Demo().run()
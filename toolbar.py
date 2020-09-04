from kivymd.app import MDApp
from kivy.lang.builder import Builder


kv ="""
MDBoxLayout:
    orientation:"vertical"

    MDToolbar:
        title:"toolbar"
        left_action_items: [["menu", lambda x: app.callback()]]
        right_action_items: [["dots-vertical", lambda x: app.callback()],["clock",lambda x: app.callback()]]
    
    MDLabel:
        text:"content"
        halign:"center"





"""

#from kivymd.uix.screen import Screen
#from kivy.uix.scrollview import ScrollView
#from kivymd.uix.boxlayout import MDBoxLayout
#from kivymd.uix.label import MDLabel
#without builder method
#class Myapp(MDApp):
 #   def build(self):
  #      sz = Screen()
   #     sc = ScrollView()
    #    bl = MDBoxLayout(orientation="vertical")
     #   lb = MDLabel(text="content",halign="center")
      #  tb = MDToolbar(title="toolbar")
       # bl.add_widget(tb)
        #bl.add_widget(lb)
        #sc.add_widget(bl)
        #sz.add_widget(sc)
        #return sz

#with builder method
class Myapp(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__=="__main__":
    Myapp().run()
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList,IconLeftWidget,OneLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox


#lists1
class myapp(MDApp):
    def build(self):
        sc = Screen()
        #one line list item
        list_view = MDList()
        scrool = ScrollView()
        #item1 = OneLineListItem(text="line1")
        #item2 = OneLineListItem(text="line2")
        #item3 = OneLineListItem(text="line3")
        #list_view.add_widget(item1)
        #list_view.add_widget(item2)
        #list_view.add_widget(item3)
        #scrool.add_widget(list_view)

        #two line list item
        #item1 = TwoLineListItem(text="firs tline",secondary_text="second line")
        #item2 = TwoLineListItem(text="firs tline",secondary_text="second line")
        #list_view.add_widget(item1)
        #list_view.add_widget(item2)
        #scrool.add_widget(list_view)
        #sc.add_widget(scrool)

        #three line list item
        #item1 = ThreeLineListItem(text="line1",secondary_text="line2",tertiary_text="line3")
        #item2 = ThreeLineListItem(text="line1",secondary_text="line2",tertiary_text="line3")
        #list_view.add_widget(item1)
        #list_view.add_widget(item2)
        #scrool.add_widget(list_view)
        #sc.add_widget(scrool)

        #custamizing the list
        #oneline avatar item
        #item1 = OneLineAvatarListItem(text="line1")
        #subitem = IconLeftWidget(icon="language-python")
        #tem1.add_widget(subitem)
        
        #two line avatrar list item
        #item1 = TwoLineAvatarListItem(text="line1",secondary_text="line2")
        #subitem = IconLeftWidget(icon="language-python")
        #item1.add_widget(subitem)

        #three line avatar list item
        #item1 = ThreeLineAvatarListItem(text="line1",secondary_text="line2",tertiary_text="line3")
        #subitem = IconLeftWidget(icon="language-python")
        #item1.add_widget(subitem)

        
        
        #item1 = OneLineAvatarIconListItem(text="python")
        #ic = IconLeftWidget(icon="language-python")
        #chek=CheckBox()
        #item1.add_widget(ic)
        #item1.add_widget(chek)
        #sc.add_widget(item1)
        return sc



if __name__=="__main__":
    myapp().run()

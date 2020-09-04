import kivy
from kivy.app import App
from kivy.uix.button import Button

class Myapp(App):
	def build(self):
		return Button(text="click me",size_hint=(0.1,0.2),font_size='20sp',pos_hint={'center_x':0.5,'center_y':0.5}
		,on_press=self.printpress,on_release=self.printrelease)
	def printpress(self,obj):
		print('Button has pressed')
	def printrelease(self,obj):
		print('i am relsed')


if __name__=="__main__":
	Myapp().run()

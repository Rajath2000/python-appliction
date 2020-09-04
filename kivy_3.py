from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

energy = 100
hours = 4

class app1(App):
    def build(self):
        self.f = FloatLayout()

        #Labels
        self.energy_label = Label(text = "Energy = " + str(energy), size_hint=(.1, .15),pos_hint={'x':.05, 'y':.9})
        self.time_label = Label(text = "Hours = " + str(hours), size_hint=(.1, .15),pos_hint={'x':.9, 'y':.9})
        self.name_label = Label(text = "Game", size_hint=(.1, .15),pos_hint={'x':.45, 'y':.9})
        self.main_label = Label(text = "Default_text", size_hint=(1, .55),pos_hint={'x':0, 'y':.35})

        #Main Buttons
        self.inventory_button = Button(text = "Inventory", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.2})
        self.help_button = Button(text = "Help", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.1})
        self.craft_button = Button(text = "Craft", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.1})
        self.food_button = Button(text = "Food", size_hint=(.3, .1),pos_hint={'x':.35, 'y':.2})
        self.go_button = Button(text = "Go", size_hint=(.3, .1),pos_hint={'x':.35, 'y':.1})
        self.walk_button = Button(text = "Walk", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.2})

        def update(self, *args):
            self.main_widget.text = str(self.current_text)

        self.f.add_widget(self.energy_label)
        self.f.add_widget(self.main_label)
        self.f.add_widget(self.time_label)
        self.f.add_widget(self.inventory_button)
        self.f.add_widget(self.help_button)
        self.f.add_widget(self.craft_button)
        self.f.add_widget(self.food_button)
        self.f.add_widget(self.go_button)
        self.f.add_widget(self.walk_button)
        self.f.add_widget(self.name_label)
        self.current_text = "Default"
        Clock.schedule_interval(update, 1)
        return self.f


        def update_label(input):
            input = self.current_text

        help_button.bind(on_press = update_label("success!"))


app1().run()

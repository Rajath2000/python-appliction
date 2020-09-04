from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker,MDThemePicker,MDDatePicker
from kivymd.uix.screen import Screen

class Myapp(MDApp):
    def build(self):
        tp = MDTimePicker()
        thp = MDThemePicker()
    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        dp = MDDatePicker(callback=self.get_date)
        dp.open()

        


if __name__=="__main__":
    Myapp().run()
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

class SahilApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.lbl = Label(text="Tap button to create file", font_size='20sp', halign='center')
        btn = Button(text="Create sahil_hero.py", size_hint=(1, 0.4), font_size='18sp')
        btn.bind(on_press=self.create_file)
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def on_start(self):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

    def create_file(self, instance):
        try:
            if platform == 'android':
                from android.storage import primary_external_storage_path
                path = primary_external_storage_path()
            else:
                path = os.getcwd()

            file_path = os.path.join(path, "sahil_hero.py")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("# Auto-generated file by Sahil App\nprint('Sahil Hero Working!')\n")
            
            self.lbl.text = f"File Created:\n{file_path}"
        except Exception as e:
            self.lbl.text = f"Error: {str(e)}"

if __name__ == '__main__':
    SahilApp().run()

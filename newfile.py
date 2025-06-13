from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
import requests

URL_WEBAPP = "https://script.google.com/macros/s/AKfycbw5u5gtwdjCohro-0k6fL9wnWBP0mtH8gpwLQHPB5ChhOA8eGL76YtMTHt8wz_o3F2D/exec"

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"

        screen = MDScreen()

        self.nome_input = MDTextField(hint_text="Nome", size_hint_x=0.9, pos_hint={"center_x": 0.5})
        self.email_input = MDTextField(hint_text="Email", size_hint_x=0.9, pos_hint={"center_x": 0.5})
        self.idade_input = MDTextField(hint_text="Idade", size_hint_x=0.9, pos_hint={"center_x": 0.5})

        enviar_button = MDRaisedButton(
            text="Enviar",
            pos_hint={"center_x": 0.5},
            on_release=self.enviar_dados
        )

        self.status_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(0, 0.6, 0, 1)
        )

        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)
        layout.add_widget(self.nome_input)
        layout.add_widget(self.email_input)
        layout.add_widget(self.idade_input)
        layout.add_widget(enviar_button)
        layout.add_widget(self.status_label)

        screen.add_widget(layout)
        return screen

    def enviar_dados(self, instance):
        dados = {
            "nome": self.nome_input.text,
            "email": self.email_input.text,
            "idade": self.idade_input.text
        }
        try:
            resposta = requests.post(URL_WEBAPP, json=dados)
            if resposta.status_code == 200:
                self.status_label.text = "Enviado com sucesso!"
                self.limpar_campos()
            else:
                self.status_label.text = f"Erro: {resposta.status_code}"
        except Exception as e:
            self.status_label.text = f"Erro: {str(e)}"

    def limpar_campos(self):
        self.nome_input.text = ""
        self.email_input.text = ""
        self.idade_input.text = ""

MainApp().run()

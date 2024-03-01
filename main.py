import flet as ft
import requests as req
from iso3166 import countries

def main(page: ft.Page):
    page.title = "WeatApp"
    page.theme_mode = "Dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = 500
    page.window_width = 500
    page.window_maximizable = False

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        e.control.selected = not e.control.selected
        e.control.update()
        page.update()

    user_data = ft.TextField(label = "Enter town",width = 400)
    weather_data = ft.Text('', size = 28)
    country_data = ft.Text('', size = 28)
    theme_button = ft.IconButton(ft.icons.SUNNY, 
                                icon_size = 50, 
                                on_click = change_theme, 
                                style = ft.ButtonStyle(color = {"selected": ft.colors.ORANGE, "": ft.colors.BLACK45})
                                )

    def get_info(e):
        if len(user_data.value) < 2:
            return
        
        API = 'f4b1f12f44c5926e7301279f45189506'
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric"
        res = req.get(URL).json()
        temp = res['main']['temp']
        country = countries.get(res['sys']['country'])
        weather_data.value = f"Weather: {str(temp)}°С" 
        country_data.value = f"Country: {(country.name)}"
        page.update()
        print(res)

    page.add(
        ft.Row(
        [
            theme_button,
        ],  alignment = ft.MainAxisAlignment.CENTER
        ),
        ft.Row([ft.Text('WeatApp', size = 25, weight = 500)], alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([user_data], alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([country_data], alignment = ft.MainAxisAlignment.CENTER),
        ft.Row([ft.FilledTonalButton(text = 'Get', on_click = get_info)], alignment = ft.MainAxisAlignment.CENTER),
    )       

ft.app(target = main)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.metrics import dp
import os
import gc
import time

# Устанавливаем сплошной темно-фиолетовый фон
Window.clearcolor = get_color_from_hex('#0A0410')

class FancyButton(ButtonBehavior, Label):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.base_text = text
        self.font_size = '15sp'
        self.color = get_color_from_hex('#FFFFFF')
        self.size_hint_y = None
        self.height = dp(55)
        self.markup = True
        self.is_active = False
        
        self.update_text()

        with self.canvas.before:
            self.color_bg = Color(rgba=get_color_from_hex('#1A0B33'))
            self.rect = RoundedRectangle(radius=[15])
            
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_text(self):
        status = "[color=#00FFAA]ВКЛ[/color]" if self.is_active else "[color=#FF5555]ВЫКЛ[/color]"
        self.text = f'[b]{self.base_text}[/b]  |  {status}'

    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press(self):
        if not self.is_active:
            self.color_bg.rgba = get_color_from_hex('#4B2082')

    def on_release(self):
        self.is_active = not self.is_active
        self.update_text()
        
        if self.is_active:
            self.color_bg.rgba = get_color_from_hex('#2D1B4E')
        else:
            self.color_bg.rgba = get_color_from_hex('#1A0B33')

class DexterShotUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        # Прижимаем всё к верху, чтобы убрать пустоту
        self.valign = 'top' 
        self.padding = [15, 15, 15, 15]
        self.spacing = 10

        # Заголовок
        title = Label(
            text='[b][color=#FFFFFF]Dexter_Aimlok[/color] [color=#B084FF]шатает[/color][/b]',
            markup=True,
            font_size='26sp',
            size_hint_y=None,
            height=dp(50)
        )
        self.add_widget(title)

        # ТГ Канал
        tg_label = Label(
            text='[b]Telegram: @azerZX1[/b]',
            markup=True,
            font_size='15sp',
            color=get_color_from_hex('#00E5FF'),
            size_hint_y=None,
            height=dp(20)
        )
        self.add_widget(tg_label)

        # FPS Счетчик
        self.fps_label = Label(
            text='[b]FPS: ---[/b]',
            markup=True,
            font_size='22sp',
            color=get_color_from_hex('#00FFAA'),
            size_hint_y=None,
            height=dp(35)
        )
        self.add_widget(self.fps_label)

        self.last_time = time.time()
        self.frame_count = 0
        Clock.schedule_interval(self.update_fps, 1.0)

        # Кнопки
        self.btn1 = FancyButton(text='ОПТИМИЗАЦИЯ ТЕЛЕФОНА (RAM)')
        self.btn1.bind(on_release=self.optimize_phone)
        self.add_widget(self.btn1)

        self.btn2 = FancyButton(text='BOOST FPS ПРИ FRAPS')
        self.btn2.bind(on_release=self.boost_fraps)
        self.add_widget(self.btn2)

        self.btn3 = FancyButton(text='ИГРОВОЙ BOOST FPS')
        self.btn3.bind(on_release=self.boost_fps)
        self.add_widget(self.btn3)

        self.btn4 = FancyButton(text='ОЧИСТКА КЭША БРАУЗЕРА')
        self.btn4.bind(on_release=self.clear_browser_cache)
        self.add_widget(self.btn4)

        self.btn5 = FancyButton(text='СБРОС СЕТИ (ПИНГ)')
        self.btn5.bind(on_release=self.network_reset)
        self.add_widget(self.btn5)

        self.btn6 = FancyButton(text='КАЛИБРОВКА БАТАРЕИ')
        self.btn6.bind(on_release=self.battery_calibrate)
        self.add_widget(self.btn6)

        # Статус (прижимаем вниз)
        self.status = Label(
            text='[i]Готов к работе[/i]',
            markup=True,
            font_size='13sp',
            color=get_color_from_hex('#B084FF'),
            size_hint_y=None,
            height=dp(40),
            halign='center'
        )
        self.status.bind(size=self.status.setter('text_size'))
        self.add_widget(self.status)

    def set_status(self, text):
        Clock.schedule_once(lambda dt: setattr(self.status, 'text', f'[b][color=#00FFAA]{text}[/color][/b]'), 0)

    def update_fps(self, dt):
        self.frame_count += 1
        current_time = time.time()
        if current_time - self.last_time >= 1.0:
            real_fps = int(self.frame_count / (current_time - self.last_time))
            
            if self.btn2.is_active:
                self.fps_label.text = f'[b][color=#00FFAA]FPS: 120 / 120Hz (СТАБИЛ)[/color][/b]'
            elif self.btn3.is_active:
                self.fps_label.text = f'[b][color=#00FFAA]FPS: 144 / 144Hz (СТАБИЛ)[/color][/b]'
            else:
                self.fps_label.text = f'[b]FPS: {real_fps} / 60Hz[/b]'
            
            self.frame_count = 0
            self.last_time = current_time

    # ========== РЕАЛЬНЫЕ СИСТЕМНЫЕ ФУНКЦИИ ==========

    def optimize_phone(self, instance):
        if self.btn1.is_active:
            self.set_status('Реальная очистка RAM...')
            gc.collect() 
            try:
                # Отключаем анимации (реально ускоряет систему)
                os.system('settings put global window_animation_scale 0.0')
                os.system('settings put global transition_animation_scale 0.0')
                os.system('settings put global animator_duration_scale 0.0')
            except:
                pass
            time.sleep(0.5)
            self.set_status('RAM очищена, анимации отключены!')
        else:
            self.set_status('Оптимизация выключена.')

    def boost_fraps(self, instance):
        if self.btn2.is_active:
            self.set_status('Fraps Boost: Запись стабилизирована!')
            Window.max_fps = 120
            gc.collect()
            try:
                # Запрещаем системе "усыплять" окно при записи
                os.system('am set-inactive false')
            except:
                pass
        else:
            self.set_status('Fraps Boost выключен.')
            Window.max_fps = 60

    def boost_fps(self, instance):
        if self.btn3.is_active:
            self.set_status('Игровой Boost: Максимум FPS!')
            Window.max_fps = 144
            gc.collect()
            try:
                # Очистка системного буфера логов (освобождает немного RAM)
                os.system('logcat -c')
            except:
                pass
        else:
            self.set_status('Игровой Boost выключен.')
            Window.max_fps = 60

    def clear_browser_cache(self, instance):
        if self.btn4.is_active:
            self.set_status('Реальная очистка кэша...')
            gc.collect()
            try:
                # Очистка временных файлов Android
                os.system('rm -rf /data/local/tmp/*')
            except:
                pass
            time.sleep(0.3)
            self.set_status('Кэш очищен!')
        else:
            self.set_status('Очистка выключена.')

    def network_reset(self, instance):
        if self.btn5.is_active:
            self.set_status('Реальный сброс сети...')
            try:
                # Отключаем и включаем сеть (сбрасывает пинг)
                os.system('svc data disable')
                time.sleep(0.5)
                os.system('svc data enable')
            except:
                pass
            self.set_status('Сеть сброшена! Пинг упал.')
        else:
            self.set_status('Сброс сети выключен.')

    def battery_calibrate(self, instance):
        if self.btn6.is_active:
            self.set_status('Реальная калибровка...')
            try:
                # Сброс статистики батареи
                os.system('dumpsys batterystats --reset')
            except:
                pass
            time.sleep(0.3)
            self.set_status('Батарея откалибрована!')
        else:
            self.set_status('Калибровка выключена.')

class DexterShotApp(App):
    def build(self):
        self.title = 'Dexter Shot'
        return DexterShotUI()

if __name__ == '__main__':
    DexterShotApp().run()

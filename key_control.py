from pynput.keyboard import Key, Controller
keyboard = Controller()  # Создаём контроллер клавиатуры
from pynput.mouse import Button, Controller
mouse = Controller()  # Создаём контроллер мышки


def ir_print(var):
    print(var)
    print(type(var))


def push(key):
    try:
        keyboard.press(KEYS[key])
        keyboard.release(KEYS[key])
    except KeyError:
        keyboard.press(key)
        keyboard.release(key)


def shortcut(*keys):
    for key in keys:
        keyboard.press(KEYS[key])
    for key in keys:
        keyboard.release(KEYS[key])


move_step = 20
scroll_step = 1
KEYS = {
    'alt': Key.alt,
    'alt_l': Key.alt_l,
    'alt_r': Key.alt_r,
    'backspace': Key.backspace,
    'caps_lock': Key.caps_lock,
    'cmd': Key.cmd,
    'cmd_r': Key.cmd_r,
    'ctrl': Key.ctrl,
    'ctrl_l': Key.ctrl_l,
    'ctrl_r': Key.ctrl_r,
    'delete': Key.delete,
    'down': Key.down,
    'end': Key.end,
    'enter': Key.enter,
    'esc': Key.esc,
    'f1': Key.f1,
    'f2': Key.f2,
    'f3': Key.f3,
    'f4': Key.f4,
    'f5': Key.f5,
    'f6': Key.f6,
    'f7': Key.f7,
    'f8': Key.f8,
    'f9': Key.f9,
    'f10': Key.f10,
    'f11': Key.f11,
    'f12': Key.f12,
    'f13': Key.f13,
    'f14': Key.f14,
    'f15': Key.f15,
    'f16': Key.f16,
    'f17': Key.f17,
    'f18': Key.f18,
    'f19': Key.f19,
    'f20': Key.f20,
    'home': Key.home,
    'insert': Key.insert,
    'left': Key.left,
    'media_next': Key.media_next,
    'media_play_pause': Key.media_play_pause,
    'media_previous': Key.media_previous,
    'media_volume_down': Key.media_volume_down,
    'media_volume_mute': Key.media_volume_mute,
    'media_volume_up': Key.media_volume_up,
    'menu': Key.menu,
    'num_lock': Key.num_lock,
    'page_down': Key.page_down,
    'page_up': Key.page_up,
    'pause': Key.pause,
    'print_screen': Key.print_screen,
    'right': Key.right,
    'scroll_lock': Key.scroll_lock,
    'shift': Key.shift,
    'shift_r': Key.shift_r,
    'space': Key.space,
    'tab': Key.tab,
    'up': Key.up
}
ir_keys = [
    {"name": "POWER", "ru_name": "Питание", "key": 33454215},
    {"name": 'BGM', 'ru_name': 'Фоновая музыка', "key": 33446055},
    {"name": 'MUTE', 'ru_name': 'отключить громкость', 'icon': '🔇', 'key': 33441975},
    {"name": 'PHOTO', 'ru_name': 'Фото', 'key': 33456255},
    {"name": 'MUSIC', 'ru_name': 'Музыка', 'key': 33439935},
    {"name": 'MOVIE', 'key': 33472575},
    {"name": 'Play/pause', 'ru_name': 'Пауза/воспроизведение', 'icon': '⏯', 'key': 33431775},
    {"name": 'RETURN', 'ru_name': 'Возврат', 'key': 33448095},
    {"name": 'Up', 'ru_name': 'Вверх', 'icon': '🔼', 'key': 33464415},
    {"name": 'Down', 'ru_name': 'Вниз', 'icon': '🔽', 'key': 33478695},
    {"name": 'Left', 'ru_name': 'Влево', 'icon': '◀', 'key': 33480735},
    {"name": 'Right', 'ru_name': 'Вправо', 'icon': '▶', 'key': 33460335},
    {"name": 'Ok', 'icon': '🆗', 'key': 33427695},
    {"name": 'SETUP', 'ru_name': 'Настройки', 'key': 33444015},
    {"name": 'CALENDAR', 'ru_name': 'Календарь', 'key': 33486855},
    {"name": 'VOL+', 'ru_name': 'Громкость+', 'key': 33435855},
    {"name": 'ZOOM', 'ru_name': 'Масштабирование', 'key': 33468495},
    {"name": 'Next Track', 'ru_name': 'Следующий трек', 'icon': '⏭', 'key': 33462375},
    {"name": 'VOL-', 'ru_name': 'Громкость-', 'key': 33423615},
    {"name": 'ROTATE', 'ru_name': 'Поворот', 'key': 33484815},
    {"name": 'Last Track', 'ru_name': 'Предыдущий трек', 'icon': '⏮', 'key': 33452175}
]
modes = [
    {"name": 'media', 'function': {
        'POWER': lambda x='POWER': ir_print(x),
        'BGM': lambda x='BGM': ir_print(x),
        'MUTE': lambda x='media_volume_mute': push(x),
        'PHOTO': lambda: push('t'),
        'MUSIC': lambda x='MUSIC': ir_print(x),
        'MOVIE': lambda: push('f'),
        'Play/pause': lambda: push('media_play_pause'),
        'RETURN': lambda: mouse.click(Button.right, 1),
        'Up': lambda: mouse.move(0, -move_step),
        'Down': lambda: mouse.move(0, move_step),
        'Left': lambda: mouse.move(-move_step, 0),
        'Right': lambda: mouse.move(move_step, 0),
        'Ok': lambda: mouse.click(Button.left, 1),
        'SETUP': lambda: push('left'),
        'CALENDAR': lambda: push('right'),
        'VOL+': lambda: push('media_volume_up'),
        'ZOOM': lambda x='ZOOM': ir_print(x),
        'Next Track': lambda: push('media_next'),
        'VOL-': lambda: push('media_volume_down'),
        'Last Track': lambda: push('media_previous')
    }},
    {"name": 'mouse_control', 'function': {
        'POWER': lambda x='POWER': ir_print(x),
        'BGM': lambda x='BGM': ir_print(x),
        'MUTE': lambda: push('media_volume_mute'),
        'PHOTO': lambda x='PHOTO': ir_print(x),
        'MUSIC': lambda x='MUSIC': ir_print(x),
        'MOVIE': lambda x='MOVIE': ir_print(x),
        'Play/pause': lambda x='media_play_pause': push(x),
        'RETURN': lambda: mouse.click(Button.right, 1),
        'Up': lambda x='Up': mouse.move(0, -move_step),
        'Down': lambda x='Down': mouse.move(0, move_step),
        'Left': lambda x='Left': mouse.move(-move_step, 0),
        'Right': lambda x='Right': mouse.move(move_step, 0),
        'Ok': lambda x='Ok': mouse.click(Button.left, 1),
        'SETUP': lambda x='SETUP': mouse.scroll(0, -scroll_step),
        'CALENDAR': lambda x='CALENDAR': mouse.scroll(0, scroll_step),
        'VOL+': lambda x='media_volume_up': push(x),
        'ZOOM': lambda: shortcut('alt', 'tab'),
        'Next Track': lambda: shortcut('ctrl', 'tab'),
        'VOL-': lambda x='media_volume_down': push(x),
        'Last Track': lambda: shortcut('ctrl', 'shift', 'tab')
    }}
]
modes_list = []
for i in modes:
    modes_list.append(i['name'])

import serial
import key_control
import time
import datetime


def do_nothing():
    pass


def case(key, default=do_nothing, dic=None, **kw):
    if dic is None:
        keys = kw.keys()
        if key in keys:
            kw[key]()
        else:
            default()
        return None
    keys = dic.keys()
    if key in keys:
        dic[key]()
    else:
        if not default is None:
            default()


def my_print(dic: dict):
    tmp = (list(dic.keys()))
    # print(tmp)
    if 'key' in tmp:
        if 'name' in tmp:
            if 'ru_name' in tmp:
                if 'icon' in tmp:
                    print(f"""Pressed "{dic['ru_name']}" [{dic['icon']}]""")
                else:
                    print(f"""Pressed "{dic['ru_name']}" """)
            elif 'icon' in tmp:
                print(f"""Pressed "{dic['name']}" [{dic['icon']}]""")
            else:
                print(f"""Pressed "{dic['name']}" """)


ser = serial.Serial(
    port='COM9',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)

print("connected to: " + ser.portstr)
count = 1
mode = 0

while True:
    # for line in ser.read():
    #     print(str(count) + str(': ') + chr(line))
    #     count = count + 1
    data = ser.readline()
    if not data == b'':
        in_data = str(data.strip())[2:-1]
        if len(in_data) == 8:
            # print(in_data)
            for i in key_control.ir_keys:
                if int(in_data) == i['key']:
                    if i['name'] == 'ROTATE':
                        mode += 1
                        if mode > len(key_control.modes_list) - 1:
                            mode = 0
                        print(f'set mode {key_control.modes_list[mode]}')
                    else:
                        print(i['name'])
                        case(i['name'], dic=key_control.modes[mode]['function'])

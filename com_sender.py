import serial
import key_control

ser = serial.Serial(
    port='COM11',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0)

print("connected to: " + ser.portstr)

while True:
    a = input()
    if str(type(a)) == "<class 'str'>":
        for i in key_control.ir_keys:
            for j in i.keys():
                if a == i[j]:
                    ser.write(str(i['key']).encode())
    elif str(type(a)) == "<class 'int'>":
        ser.write(str(a).encode())

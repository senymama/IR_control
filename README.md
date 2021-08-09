Я хотел сделать удалённое управление своим компьютером при помощи ик пульта.
Для обработки данных приёмника я использую плату arduino nano, 
а для выполнения команд программу написанную мной на python.
Я использовал 21 кнопочный пульт от фото-рамки DEXP.
Для обработки данных принятых ик приёмником используется библиотека iarduino_IR.
Через COM порт данные о нажатой кнопке получает python и обрабатывает.
Файл main.py обрабатывает данные из Serial порта и выполняет функции из key_control.py.

I wanted to make remote control of my computer using an IR remote control.
To process the receiver data, I use the arduino nano board,
and to execute commands, a program written by me in python.
I used a 21 button remote control from the DEXP photo frame.
The iarduino_IR library is used to process the data received by the IR receiver.
Python receives the data about the pressed button through the COM port and processes it.
The main.py file processes data from the Serial port and executes functions from key_control.py.
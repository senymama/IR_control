Для использования в своих условиях вам необходимо записать в массив ir_keys из key_control.py
коды всех своих клавиш и их названия (можно без этого).
Сделать функции для каждой кнопки в каждом режиме(кнопка переключения режима настраивается в main.py).
Далее при запуске main.py он подключится к указанному порту
(указан в коде т.к. не планируется отключать плату от компьютера)

To use it in your conditions, you need to write to the ir_keys array from key_control.py
codes of all your keys and their names (you can do without it).
Make functions for each button in each mode (the mode toggle button is configurable in main.py).
Next, when you run main.py, it will connect to the specified port
(specified in the code because it is not planned to disconnect the board from the computer)

Немного об истории проекта
A little about the history of the project

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
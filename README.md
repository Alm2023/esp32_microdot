# esp32_microdot

Проект полезен для изучающих Python и интересующихся направлением IoT

Цель проекта - веб интерфейс микроконтроллера ESP32 позволяющий включать/выключать 2 светодиода

Веб интерфейс микроконтроллера ESP32 создан на фреймворке Microdot (micropython)
Microdot - упрощенный аналог фреймворка Flask
веб интерфейс позволяет включать и выключать два светодиода,
подключенных  к ножкам микроконтроллера

Для использования проекта необходимо все файлы скопировать в микроконтроллер ESP32.
Первый светодиод подсоединяется на ножки с номером 13 (+) и рядом находящуюся ножку  GND (-), светодиод на 3 вольта, желательно с резистором на 220 ОМ, чтобы избежать перегорания ножки микроконтроллера
Второй светодиод на ножки с номером 18 (+) и рядом находящийся GND (-), светодиод на 3 вольта, желательно с резистором на 220 ОМ, чтобы избежать перегорания ножки микроконтроллера

Подключение и перенос файлов можно сделать согласно инструкции https://youtu.be/1efsWgK_QaU

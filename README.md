# Дипломный проект

## Структура 

### test_framework
Папка с утилитарными классами

### tests
Папка с файлами тестовых сценариев

### configuration.py
Файл с конфигурационными параметрами такими, как url  API сервиса и ендпоинтов

### data.py
Скрипт с тестовыми данными

### requirements.txt
Список установленных модулей
- pytest - библиотека запуска тестов
- requests - библиотека для создания веб запросов
- urllib3 - служебная библиотека для корректной работы requests(скорректированая версия)

### SQL_Request_1.txt 
Скрипт по заданию номер 1 работы с базой данных

### SQL_Request_2.txt 
Скрипт по заданию номер 2 работы с базой данных


## Для запуска тестов неоходимо:
- выполнить установку всех компонентов командой python3 -m pip install -r requirements.txt, находясь в корне папке проекта
- запустить тесты из командной строки python3 -m pytest tests/test_order_creation.py, находясь в корне папки проекта
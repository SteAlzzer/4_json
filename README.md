# 4_json

## Назначение скрипта
Когда-нибудь видели, как выглядит контент json-файла? Вот вам:
`[{"Id":"79742784-9ef3-4543-bc98-a219a8903c18","Number":1,"Cells":{"global_id":14371450,"Name":"Ароматный Мир","IsNetObject":"да","OperatingCompany":"Ароматный Мир","TypeService":"реализация продовольственных товаров","AdmArea":"Западный административный округ","District":"район Кунцево","Address":"улица Академика Павлова, дом 10","PublicPhone":[{"PublicPhone":"(495) 777-51-95"}],"WorkingHours":[{"Hours":"09:30-22:30","DayOfWeek":"понедельник"},{"Hours":"09:30-22:30","DayOfWeek":"вторник"},{"Hours":"09:30-22:30","DayOfWeek":"среда"},{"Hours":"09:30-22:30","DayOfWeek":"четверг"},{"Hours":"09:30-22:30","DayOfWeek":"пятница"},{"Hours":"09:30-22:30","DayOfWeek":"суббота"},{"Hours":"09:30-22:30","DayOfWeek":"воскресенье"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.39703804817934,55.740999719549094]}}}, {"Id":"1bd07c21-05de-4015-b015-d22657168ded","Number":2,"Cells":{"global_id":14934782,"Name":"Массандра в Алтуфьево","IsNetObject":"да","OperatingCompany":"Массандра","TypeService":"реализация продовольственных товаров","AdmArea":"Северо-Восточный административный округ","District":"район Бибирево","Address":"улица Лескова, дом 6","PublicPhone":[{"PublicPhone":"(499) 909-40-08"}],"WorkingHours":[{"Hours":"10:00-22:00","DayOfWeek":"понедельник"},{"Hours":"10:00-22:00","DayOfWeek":"вторник"},{"Hours":"10:00-22:00","DayOfWeek":"среда"},{"Hours":"10:00-22:00","DayOfWeek":"четверг"},{"Hours":"10:00-22:00","DayOfWeek":"пятница"},{"Hours":"10:00-22:00","DayOfWeek":"суббота"},{"Hours":"10:00-22:00","DayOfWeek":"воскресенье"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.593177064306758,55.897722369367969]}}}, {"Id":"a16c8154-09d8-4207-8e13-cb8db654e95c","Number":3,"Cells":{"global_id":14937274,"Name":"Соната-М","IsNetObject":"нет","OperatingCompany":null,"TypeService":"реализация продовольственных товаров","AdmArea":"Северо-Восточный административный округ","District":"район Бибирево","Address":"Алтуфьевское шоссе, дом 72","PublicPhone":[{"PublicPhone":"(905) 791-87-13"}],"WorkingHours":[{"Hours":"09:00-22:00","DayOfWeek":"понедельник"},{"Hours":"09:00-22:00","DayOfWeek":"вторник"},{"Hours":"09:00-22:00","DayOfWeek":"среда"},{"Hours":"09:00-22:00","DayOfWeek":"четверг"},{"Hours":"09:00-22:00","DayOfWeek":"пятница"},{"Hours":"09:00-22:00","DayOfWeek":"суббота"},{"Hours":"09:00-22:00","DayOfWeek":"воскресенье"}],"ClarificationOfWorkingHours":null,"geoData":{"type":"Point","coordinates":[37.588035999647531,55.89020100016689]}}}]`

Отвратительно, не так ли?
>*Нечитаемо!*

>*Неприемлемо!*

>*Мерзость! Фу!*

А этот скрипт предлагает вам *никогда ранее не виданое* ~~(маркетинговый bullshit, куда без него)~~ красивое и прелестное отображение содержимого json-файла.

Не попробуете, не увидите!

## Как использовать?
Тут есть два момента:

1. Запустить через **cmd**

	Юзадж: `python pprint_json.py p path_to_json`.
	- `-p (--path)` путь к json-файлу.
	

2. Подключить в качестве модуля в ваш скрипт
	
	Вот пример:
```python
import pprint_json

data = pprint_json.load_data('file.json')
pprint_json.pretty_print_json(data)
```

## Урок 1
Программа является решением урока 2 по курсу `Знакомство с Django: ORM`. Код находит из базы данных активные пропуска, посещения отдельного человека и подозрительные посещения среди них. 
Эту информацию код выводит на сайт.
### Запуск программы
Шаги:
1. Скачать весь проект к себе. 
Установить библиотеки:
```python:
pip install -r requirments.txt
```
Для корректной работы должен быть установлен `python3`
2. Создать файл `.env`, и заполнить его следующим образом, (сможете заполнить только если с вами поделились правами):

```
HOST = 'адрес хоста'
PORT = 'порт'
NAME = 'имя базы'
ALLOWED_HOSTS = [домен, где развернут сайт( (!)не безопасно, но можно ввести ["*"])]
SECRET_KEY = 'секретный ключ'
USER =  'пользователь'
PASSWORD = 'пароль'
```
необязательно:
```
DEBUG = дефолтно False. Для отладки ввести True
```
3. Запустить программу/сервер:\
`python manage.py runserver 127.0.0.1:8000`
4. Если все верно, программа даст ссылку на сайт с актуальной информацией.
###Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
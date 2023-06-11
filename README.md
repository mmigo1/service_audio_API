# Web - audio service Django

 Это приложение представляет собой  WEB сервис реализованный на Фреймворке Django


## Функции веб сервиса

- Реализация  REST методов
- Регистрация пользователей и сохранение их данных в БД
- Добавление аудиозаписи в формате .wav, преобразование в формат .mp3 и сохранение в БД
- Возможность загрузки аудиозаписей из БД


## Установка
По умолчанию докер будет использовать порт 8000.
1)Используйте docker-compose что бы построить образ
```sh
docker-compose build
```
2)Выполните миграции
```sh
docker compose run --rm web-app sh -c "python manage.py migrate"
```
3)Создайте суперпользователя
```sh
docker compose run --rm web-app sh -c "python manage.py createsuperuser"
```
4)Запустите образ
```sh
docker-compose up
```
## Примеры запросов к POST API
Приложение работает по на хост-машине по адресу http://localhost:8000/ и обрабатывает запросы по четырём url адресам:

1)admin/ - служит для входа в панель администратора и взаимодействия с БД

2)/regis - служит для регистрации пользоватлей и принимает POST метод и запросы вида -
```sh
{
    "username": "user",
    "password": "123"
}
```
После чего пользователь с таким логином и паролем будет зарегистрирован в БД.
Ответом  на запрос будет ID и токен пользователя.

3)/add - служит для добавление аудиозаписи и принимает POST метод и запросы вида - 
```sh
{
    "file": "sample.wav",
    "id": "1",
    "token": "03511705-8698-4524-9af5-729b2cc0fb8f"
}
```
Ответом на запрос будет url для скачивания записи 

4)/record - предоставляет возможность скачать аудиозапись из БД в формате ".mp3".

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

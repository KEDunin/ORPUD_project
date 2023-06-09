# ORPUD_project

    Основное предназначение данной платформы - предоставление пользователям информации по интересукщим их товарам. 
    На данный момент БД загружена далеко не большим массивом данных, а содержит лишь сведения о продуктах, 
    выпускаемых под торговой маркой Apple и находящихся в продаже на интернет-магазинах.
    В существующих таблицах хранится информация об основных характеристиках Iphone различных поколений,
    позволяя найти на сайте ту или иную модель телефона. 
    Созданный веб-сайт генерирует своеобразный мини-отчет по устройству, технические характеристики которого
    совпадают с теми, которые указывает пользователь в форме-ввода. Отчет содержит информацию о внешнем виде и 
    об актуальной цене товара, а также предоставляет возможность просмотреть динамику изменения цен на телефоны с помощью
    инструментов графического моделирования. 
    Преимущество платформы заключается в ее простоте и удобстве, вся информация по девайсам с различных 
    интернет-магазинов содержится в одном месте.


## Установка и запуск

- Входим в виртуальное окружение
```sh
venv/scripts/activate
```
- Подгружаем необходимые библиотеки, содержащиеся в файле requirements.txt
```sh
pip install -r requirements.txt
```
- Выполняем миграции БД
```sh
python manage.py migrate
```
- Запускаем сервер
```sh
python manage.py runserver 
```

Проверьте подключение к проекту, путем перехода по предложенной ссылке, которая должна
открыться в вашем браузере по умолчанию

```
127.0.0.1:8000
```

### Парсер

Дополнительно в проекте предусмотрена возможность сбора необходимых данных и сохранение их
в определенном формате путем использования парсера. Все зависимые файлы находятся в директории 
./parser.
Программа запуска:
```sh
cd parser
```
```sh
python main.py
```
Извлеченный датасет будет сохранен в директории ./parser/tables 
Имя файла будет соответствовать дате запуска данного кода

## Видео, демонстрирующее функционал веб-сайта

https://youtu.be/zhh0Jk6MvQw

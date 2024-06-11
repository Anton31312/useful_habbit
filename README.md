<h1>Useful habbit</h1>

<h3>Установка и использование (для Windows)</h3>

<p>
<br>1. Клонируйте репозиторий.
<br>2. Создайте и активируйте виртуальное окружение (проект использует Poetry, за информацией по установке https://pythonchik.ru/okruzhenie-i-pakety/menedzher-zavisimostey-poetry-polnyy-obzor-ot-ustanovki-do-nastroyki).
<br>3. Для работы программы необходимо установить зависимости, пропишите "poetry init" в командную строку.
<br>4. Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample.
<br>5. Создайте базу данных ( Например, через консоль: 1 - psql -U postgres; 2 - create database online_studing; 3 - выход: \q)
<br>6. Сделайте и примените миграции. 
    <br><br>6.1 python manage.py makemigrations 
    <br><br>6.2 python manage.py migrate
<br>7.Можете загрузить тестовые данные: 
    <br><br>7.1 python manage.py loaddata data_habbit.json 
    <br><br>7.2 python manage.py loaddata data_users.json либо создать свои.
<br>8. Создайте суперпользователя: python manage.py csu
<br>9. Запустите сервер: python manage.py runserver
<br>10. Настройка для кеша. Перед тем как использовать пакет redis внутри Django, не забудьте установить БД Redis. 
    <br><br>Для этого: в Linux используется команда sudo apt install redis или sudo yum install redis, 
    <br><br>в macOS — команда brew install redis, 
    <br><br>в случае с Windows воспользуйтесь инструкцией: https://redis.io/docs
</p>
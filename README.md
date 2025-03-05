# Homework_L10 - Allure Reports

https://github.com/qa-guru/knowledge-base/wiki/9.-Allure-Reports-Python



ИНСТРУКЦИЯ ПО УСТАНОВКЕ ALLURE


Устанавливаем Аллюр с помощью инсталлятора как в лекции(в конспекте лекций подробно описаны шаги по настройке).

Если по каким-то причинам аллюр не удаётся установить с помощью инсталлятора, тогда действуем так:



Как приготовить Аллюр по быстрому:

1. Если не установлена Java - установить

2. Отсюда https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/

забираем последнюю версию (или какая тебе нужна)

допустим это 2.20.1:

здесь https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.20.1/

качаем архив allure-commandline-2.20.1.zip

3. Разархивируем в корень проекта, получаем папку allure-2.20.1

4. Переименовываем для удобства папку allure-2.20.1 в allure

Аллюр по быстрому готов, теперь запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):

Mac: allure/bin/allure serve

Win: allure/bin/allure.bat serve


Вариант чуть сложнее, но один раз сделал, и будет работать всегда (начиная с п.3 примерно так делают установщики аллюра):


1. как п.1 в аллюр по быстрому

2. как п.2 в аллюр по быстрому

3. разархивируем куда тебе удобно

4. прописываем в переменную окружения PATH полный путь до папки allure/bin/ в которой лежат исполняемые файлы allure для Mac и allure.bat для Win

Например путь для Mac: /Users/User_name/PythonProject/tests_demoqa/allure/bin

Теперь запускать отчет можно из корня проекта командой (если папка с результатами в allure-result и она в корне проекта):

Mac: allure serve

Win: allure.bat serve


Аттеншн:

1. Если ты креативен, и папка с результатами называется не allure-results, то после serve надо указать имя этой папки

2. В случае, если папка с результатами формируется не в корне проекта, то в конфгурации запуска надо поправить working directory - указать корневую папку проекта, это исправит ситуацию

3. Параметры запуска:

--alluredir=allure-results - указывает аллюру имя папки куда записывать результаты

--clean-alluredir - указывает аллюру, что при запуске надо удалить содержимое папки alluredir (удалить результаты предыдущего запуска, обычно полезно при разработке и отладке, чтобы не было мусора)

4. В корне проекта можно создать файл pytest.ini следующего содержания:

[pytest]

addopts =

    --clean-alluredir

    --alluredir=allure-results

в таком случае, параметры запуска будут браться из этого файла, и указывать отдельно в команде запуска эти параметры будет не нужно 

5. Папку  с аллюром allure (если она лежит в проекте) и папку с результатами allure-results (или твое имя папки, если ты задавал другое) надо добавить в .gitignore, эти папки не должны попасть в репозиторий

дока https://docs.qameta.io/allure-report/#_installing_a_commandline

п 2.1.4. Manual installation



для настройки теста добавить в modify --alluredir=allure-results
для отображения результат выполнить команду: kuznetsova@MBP16M1MAX Homework_L10 % allure serve homework_10/allure-results


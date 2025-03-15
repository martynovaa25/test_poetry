#Проект "Виджет банковских операций клиента"

##Описание: 

Это виджет, который показывает несколько последних успешных банковских операций клиента.
Номер карты и счета клиента замаскирован, а операции отсортированы по дате и ключу.

##Установка

Клонируйте репозиторий:
```
https://github.com/martynovaa25/test_poetry.git
```

#Зависимости

Установите зависимости:
```
pip install -r requirements.txt
```

#Используемые методы

Для работы виджета реализованы следующие функции:
- функция маскировки номера карты (получает на вход номер карты и маскирует его в соответствии со стандартом маскировки)
- функция маскировки номера счета (аналогично функции максировки номера карты)
- функция, которая определяет, что ввел пользователь - номер карты или номер счета и маскирует их согласно предыдущим функциям
- функция отображения даты в формате ДД.ММ.ГГ
- функция сортировки данных по ключу (состояние функции маскировки = выполнено)
- функция сортировки данных по дате произведения маскировки

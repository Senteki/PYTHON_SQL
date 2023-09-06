# Наталья Янчич - 8-я когорта  — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


# Создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.body_order)


# Сохранение трека
def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_INFO,
                        json=data.track,
                        params={'t': track})


# Запрос на получение по треку
def get_order():
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_INFO,
                        json=data.body_order)


response = post_new_order()

print(post_new_order())
print(get_track_order('t'))
print(get_order())
print(response.json())

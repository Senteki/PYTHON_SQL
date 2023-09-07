import sender_stand_request

# Cоздаем функцию заказа и получения его трека
def get_track():
    # В переменную response сохраняется результат запроса создания заказа
    response = sender_stand_request.post_new_order()
    # Успешное создание заказа
    if response.status_code == 201:
        return response.json()["track"]


    # Если заказ не создан выводим сообщение об ошибке
    else:
        print(f"Заказ не создан, код - {response.status_code}")

# Функция получения заказа по его треку
def test_order_by_track():

    # В track сохраняем трек заказа
    track = get_track()
    # В response сохраняем результат запроса на получение информации о заказе по треку
    response = sender_stand_request.get_track_order(track)

    # Проверяем код ответа: -> 200
    assert response.status_code == 200
    print(response)


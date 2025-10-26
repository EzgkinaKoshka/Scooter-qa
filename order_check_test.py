import data
import tasks_order


def test_get_order_by_track_status_200():
    response_track = tasks_order.new_order(data.order_body) #создаем заказ
    track = response_track.json()['track']  #сохраняем номер заказа
    response = tasks_order.get_order(track) #получаем заказ по номеру
    assert response.status_code == 200



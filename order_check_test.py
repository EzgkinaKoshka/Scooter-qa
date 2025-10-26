import data
import tasks_order


def test_get_order_by_track_status_200():
    response_track = tasks_order.new_order(data.order_body)
    track = response_track.json()['track']
    response = tasks_order.get_order(track)
    assert response.status_code == 200



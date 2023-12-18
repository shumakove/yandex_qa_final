import data
import pytest
from test_framework.utils import *


class TestOrderCreation:

    def setup_class(self):
        self.order_list = data.orders


    # Проверка корректного кода возврата
    def test_create_order_with_correct_data_return_code_201(self):
        body = self.order_list[0]
        response = create_new_order(body, debug=True)

        assert response.status_code == 201

    # Проверка, что трек генеируется корректно
    def test_create_order_with_correct_data_return_track_id(self):
        body = self.order_list[0]
        response = create_new_order(body)

        assert response.json()['track'] is not None

    # Проверка, что трек уникальный
    def test_create_order_with_correcr_data_return_unique_track(self):
        body = self.order_list[0]
        response_one = create_new_order(body)
        first_track = response_one.json()['track']

        body["firstName"] = "ДругоеИмяДляПримера"
        response_two = create_new_order(body)
        second_track = response_two.json()['track']

        assert first_track != second_track, 'track имеет не уникальное значение'



    # Здесь есть баг API, некоторые поля при возвращении зачем-то меняют тип данных ( например станция метро и срок аренды)
    def test_create_order_with_correct_data_save_all_information(self):
        body = self.order_list[0]
        response = create_new_order(body, debug=True)

        track_number = response.json()['track']
        track_information = get_information_by_order_track(track_number)
        print(track_information["order"])

        fields_to_check = {'firstName', 'lastName', 'address', 'comment', 'metroStation', 'phone', 'rentTime',
                           'comment'}
        for field in fields_to_check:
            assert track_information['order'][field] == body[field], f"{field} сохраняется некорректно"

    # Пример кейса, находящий баг в API
    def test_create_order_with_incorrect_phone_number_not_allowed(self):
        body = self.order_list[0]
        body['phone'] = None
        response = create_new_order(body, debug=True)

        assert response.status_code != 201

    # Еще один кейс с багом в API
    def test_create_order_with_empty_body_not_allowed(self):
        body = self.order_list[1] # указываем пустое тело запроса из шаблона
        response = create_new_order(body)

        assert response.status_code != 201, 'Создается заказ, используя пустое тело запроса'

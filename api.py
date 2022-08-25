import requests

PASSWORD = 'S7w973oiJ8TNbb1gp403V27gsUr61jT8'
USER = 'andreykutenkikh@gmail.com'

URL = 'http://dvkeramik.ru/api/products?q='
PREFIX = '&page=1&items_per_page=30'

token='5795693615:AAHZGhvouRTcQh_JmC1SWdNBuh5y7QuyXrg'
chat_id = 279293973

session = requests.Session()
session.auth = (USER, PASSWORD)


def make_url(search_phrase):
    """Создает URL запрос"""
    new_url = URL + search_phrase + PREFIX
    return new_url


def take_availability(endpoint):
    """Отправляет запрос на сервер и возвращает товары и их доступное для
       заказа количество. Записывает полученные значения в словарь."""
    dict_amount = {}
    response = session.get(endpoint).json()
    for product in response["products"]:
        name_product = product["product"]
        amount = product["amount"]
        dict_amount[name_product] = amount
    return dict_amount


def new_search(argument):
    answer = take_availability(make_url(argument))
    return answer

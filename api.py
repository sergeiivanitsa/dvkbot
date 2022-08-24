import requests

PASSWORD = 'S7w973oiJ8TNbb1gp403V27gsUr61jT8'
USER = 'andreykutenkikh@gmail.com'


session = requests.Session()
session.auth = (USER, PASSWORD)

def make_url(url):
    """Создает URL запрос"""
    name = input().replace(' ', '+')
    new_url = str(url + name)
    return new_url


def take_availability(endpoint):
    """Отправляет запрос на сервер и возвращает товары и их доступное для заказа количество"""
    response = session.get(endpoint)
    return response.content["products"]


if __name__ == '__main__':
    url = 'http://dvkeramik.ru/api/products?q='
    print(take_availability(make_url(url)))
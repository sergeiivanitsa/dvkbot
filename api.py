import requests

PASSWORD = 'S7w973oiJ8TNbb1gp403V27gsUr61jT8'
USER = 'andreykutenkikh@gmail.com'

token='5795693615:AAHZGhvouRTcQh_JmC1SWdNBuh5y7QuyXrg'
chat_id = 279293973

URL = 'http://dvkeramik.ru/api/products?q='


session = requests.Session()
session.auth = (USER, PASSWORD)

def make_url(URL):
    """Создает URL запрос"""
    name = input().replace(' ', '+')
    new_url = str(URL + name)
    return new_url


def take_availability(endpoint):
    """Отправляет запрос на сервер и возвращает товары и их доступное для заказа количество"""
    dict_amount = {}
    response = session.get(endpoint).json()
#    name_product = response["products"][0]["product"]
#    amount = response["products"][0]["amount"]
#    dict_amount = {}
#    dict_amount[name_product] = amount
#    return dict_amount
    for product in response["products"]:
        name_product = product["product"]
        amount = product["amount"]
        dict_amount[name_product] = amount
    return dict_amount


def print_dict(dict):
    for key in dict.keys():
        print(f'{key} — {dict[key]} шт.')


#if __name__ == '__main__':
#    url = 'http://dvkeramik.ru/api/products?q='
#    currency_dict = take_availability(make_url(url))
#    print_dict(currency_dict)


def new_weather(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat.id, print_dict(take_availability(make_url(URL))))
import xml.dom.minidom as minidom
import urllib.request


def get_data(xml_url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'MyApp/1.0')]
    urllib.request.install_opener(opener)
    web_file = urllib.request.urlopen(xml_url)
    return web_file.read()


def get_currencies_dictionary(xml_content):

    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("offer")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'name':
                    value = child.firstChild.data
                    id = node.getAttribute("id")
        currency_dict[value] = id
    return currency_dict


def print_dict(dict):
    for key in dict.keys():
        print(key, dict[key])


if __name__ == '__main__':
    url = 'https://dvkeramik.ru/yml_get/2w5s1ullhoxf'
    currency_dict = get_currencies_dictionary(get_data(url))
    print_dict(currency_dict)

from xml.etree import ElementTree
import requests

url = 'https://dvkeramik.ru/yml_get/2w5s1ullhoxf'

response = requests.get(url)

tree = ElementTree.parse(response.content)
root = tree.getroot()

print(root)
print(root.tag, root.attrib)

#import urllib.request
#import requests


#def get_data(xml_url):
#    web_file = urllib.request.urlopen(xml_url)
#    return web_file.read()


#if __name__ == '__main__':
#    url = 'https://dvkeramik.ru/yml_get/2w5s1ullhoxf'
#    response = requests.get(url)
#    data = get_data(response)

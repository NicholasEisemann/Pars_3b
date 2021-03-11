import requests
from lxml import etree

# Кодируем в Win-1251
xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
# Получаем заначение "Value"
curs = xml_response.find("Valute[@ID='R01200']/Value").text

print(f"Курс Гонконского Доллара к Российскому рублю: {curs} ")

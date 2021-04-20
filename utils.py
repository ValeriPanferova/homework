from requests import get


def get_exchange_rate():
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.content.decode(encoding=response.encoding)
    dictionary = dict()
    keys = []
    values = []
    for el in content.split('<CharCode>')[1:]:
        key = el.split('<')[0]
        keys.append(key)
    for el in content.split('<Value>')[1:]:
        value = el.split('<')[0]
        values.append(value)
    i = 0
    while i < len(keys):
        dictionary.setdefault(keys[i], values[i])
        i += 1
    return dictionary


def currency_rates(key):
    rate_dict = get_exchange_rate()
    return rate_dict.get(key.upper())


if __name__ == "__main__":
    print(currency_rates('AZN'))

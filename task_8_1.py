import re


def email_parse(email_address):
    email_address_parser = re.compile(r'(?P<username>\b\w+).(?P<domain>\b\w+\.\w+)')
    result_iter = email_address_parser.match(email_address)
    if not result_iter:
        raise ValueError(f"Адрес не валиден: {email_address}")
    return result_iter.groupdict()


print(email_parse('someone@geekbrains.ru'))

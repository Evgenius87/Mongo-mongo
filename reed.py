from pprint import pprint

from models import Authors, Quotes
from conect import connect



def find_quotes_by_tags(some_tags: list)->list:
    quotes_list = []
    for tag in some_tags:
        quotes = Quotes.objects(tags=tag)   
        for quote in quotes:
            quotes_list.append(quote.quote)
    return quotes_list

def find_qoutes_by_name(some_name: list)->list:
    quotes_list = []
    full_name = ''
    for name in some_name:
        full_name += f"{name} "
    auth = Authors.objects(fullname=full_name.strip())
    for a in auth:
        quotes = Quotes.objects(author=a)
        for quote in quotes:
            quotes_list.append(quote.quote)
        return quotes_list


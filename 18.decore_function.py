# Ход к сайту

#import webbrowser

#def oper_url(url):
#    webbrowser.open(url)

#oper_url('https://www.codewars.com/dashboard')

# 2

import webbrowser

def validator(func):
    def wrapper(url):
        if '.' in url:
            func(url)
        else:
            print('Неверный URl')
    return wrapper


@validator
def oper_url(url):
    webbrowser.open(url)

oper_url('https://www.codewarscom/dashboard')
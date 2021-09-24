from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

CENSORED = ['мат', 'матт']
@register.filter(name='censor')
def censor(value):
    text = value.split()
    for word in text:
        if word.lower() in CENSORED:
            value = value.replace(word, '****')
    return value


from pyweb import pydom
from random import randint

ciertamente = ['cositas', 'a ver', 'ciertamente']

def get_joke(event):
    n = randint(0,2)
    pydom["div#jokes"].html = ciertamente[n]

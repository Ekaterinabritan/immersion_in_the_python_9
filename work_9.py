#Домашняя работа №9

from typing import Callable
import csv
from math import sqrt
from random import randint
import json

def decor_disc(function:Callable):
    func_csv()
    def coef_disc():
        with open('testcsv.csv', 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for f_coef in reader:
                if f_coef and f_coef[0] != 0:
                    function(*f_coef)

    return coef_disc





def func_csv(csv_file: str = 'testcsv.csv'):
    with open(csv_file, 'w', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for row in range(0, 100):
            csv_list = writer.writerow([randint(0, 10), randint(0, 10), randint(0, 10)])
        return csv_list




@decor_disc
def quadratic_equation():
    disc_result: int = b** 2 - 4*a*c
    if disc_result > 0:
        x_1 = (-b + sqrt(disc_result)) / 2 * a
        x_2 = (-b - sqrt(disc_result)) / 2 * a
        print(x_1,x_2)
    elif disc_result == 0:
        x = ( - b ) / 2 * a
        print(f' один корень {x} ')
    else:
        print('корней нет')




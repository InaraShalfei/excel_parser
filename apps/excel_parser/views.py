import datetime
import os

import pandas as pd
import numpy as np

from .models import UserModel


def parse_file(request):
    df = pd.read_excel('/home/user/PycharmProjects/excel_parser/test.xlsx')
    df = df.replace(np.nan, None)

    for worker in df.to_dict('records'):
        document_date = datetime.datetime.strptime(worker['Дата табеля'], '%d.%m.%Y')

        UserModel.objects.create(name=worker['Сотрудник'], position=worker['Функция клиента'],
                                 IIN=worker['ИНН сотрудника'],
                                 company=worker['Контрагент'], planned_start_time=worker['Плановое начало смены'],
                                 planned_finish_time=worker['Плановое окончание смены'],
                                 company_branch=worker['Организация'],
                                 real_start_time=worker['Отметка на приход'],
                                 real_finish_time=worker['Отметка на уход'],
                                 document_date=document_date)

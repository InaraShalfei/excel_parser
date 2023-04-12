import datetime

import pandas as pd
import numpy as np

from excel.excel_sqlite.models import UserModel

df = pd.read_excel('test.xlsx')
df = df.replace(np.nan, None)


for worker in df.to_dict('records'):
    UserModel.objects.create(name=worker['Сотрудник'], position=worker['Функция клиента'], IIN=worker['ИНН сотрудника'],
                             company=worker['Контрагент'], planned_start_time=worker['Плановое начало смены'],
                             planned_finish_time=worker['Плановое окончание смены'], company_branch=worker['Организация'],
                             real_start_time=worker['Отметка на приход'], real_finish_time=worker['Отметка на уход'],
                             document_date=datetime.datetime.strptime(worker['Дата табеля'], '%d%m%y').date())

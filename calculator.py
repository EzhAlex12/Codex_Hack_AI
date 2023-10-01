import numpy as np
from statsmodels.tsa.arima.model import ARIMA
#Данные ключевой ставки ЦБ РФ с 2013 по 2023 год по кварталам
rates = np.array([5.5, 6.25, 7.25, 7.75, 11.25, 15.3, 12.6, 11.25, 11.0, 11.0, 10.75, 10.25, 10.0, 9.875, 9.3, 8.75, 8.17, 7.5, 7.25, 7.375, 7.625, 7.75, 7.625, 7.25, 6.58, 6.4375, 6.125, 5.3, 4.375, 4.25, 4.375, 5.0, 6.25, 7.58, 12.67, 14.3, 8.3, 7.5, 7.5, 7.5, 10.25])
#содание модели
model = ARIMA(rates, order=(5,1,0))
#тренировка модели
model_fit = model.fit()

forecast_quarter = model_fit.predict(start=len(rates), end=len(rates)+3)  # Прогноз на 4 квартала


from math import ceil
print("Введите свой возраст: ")
age = int(input())
print("Введите свой пол (0 - мужской/ 1 - женский): ")
gndr = input()
print("Введите свой баланс: ")
balance = int(input())
if gndr == 1:
    ost_pens_srok = 60 - age
else:
    ost_pens_srok = 65 - age
print("Введите размер пенсии, которую Вы хотите получать в месяц: ")
wish_pens = int(input())
print("Введите количество лет, на протяжении которых Вы хотите получать пенсию: ")
srok = int(input())
if srok >= 264:
    srok = 264
else:
    srok = int(srok) * 12
wish_sum = wish_pens * srok #вычисляем итоговый размер всей пенсии
k_pens_1_q = ceil(forecast_quarter[0])  #коэффициент пенсии за первый квартал
k_pens_2_q = ceil(forecast_quarter[1])  #коэффициент пенсии за второй квартал
k_pens_4_q = ceil(forecast_quarter[3])  #коэффициент пенсии за четвёртый квартал
#количество платежей в год
kol_vo_payments_per_year_1_q = 4
kol_vo_payments_per_year_2_q = 2
kol_vo_payments_per_year_4_q = 1
if ost_pens_srok <= 0:
    future_pay_per_month = 0
    print(future_pay_per_month)
else:
    future_pay_per_1_q = (wish_sum - balance) / (ost_pens_srok * kol_vo_payments_per_year_1_q * (1 + 0.01 * k_pens_1_q)) #вычисление единичного плажтежа по первому тарифу
    future_pay_per_2_q = (wish_sum - balance) / (ost_pens_srok * kol_vo_payments_per_year_2_q * (1 + 0.01 * k_pens_2_q)) #вычисление единичного плажтежа по второму тарифу
    future_pay_per_4_q = (wish_sum - balance) / (ost_pens_srok * kol_vo_payments_per_year_4_q * (1 + 0.01 * k_pens_4_q)) #вычислениеединичного плажтежа по третьему тарифу
    print("Первый тариф: " + "единичный платёж - " + str(ceil(future_pay_per_1_q)) + ",", "количесвто выплат в год - " +str(kol_vo_payments_per_year_1_q))
    print("Первый тариф: " + "единичный платёж - " + str(ceil(future_pay_per_2_q)) + ",", "количесвто выплат в год - " +str(kol_vo_payments_per_year_2_q))
    print("Первый тариф: " + "единичный платёж - " + str(ceil(future_pay_per_4_q)) + ",", "количесвто выплат в год - " +str(kol_vo_payments_per_year_4_q))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Сумма вклада : ")
depozits=[int(money)*per_cent['ТКБ']/100,int(money)*per_cent['СКБ']/100,int(money)*per_cent['ВТБ']/100,int(money)*per_cent['СБЕР']/100]
depozits_int = list(map(int,depozits))
print("Максимальная сумма, которую вы можете заработать — ", max(depozits_int))


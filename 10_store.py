goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamp_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamp_code = goods['Лампа']
lamp_item = store[lamp_code][0]
lamp_quantity = lamp_item['quantity']
print('Лампа -', lamp_quantity, 'шт, стоимость', lamp_cost, 'руб')
stol_cost = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
stol_cost1 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']
stol_cost = stol_cost + stol_cost1
stol_code = goods['Стол']
stol_item = store[stol_code][0]
stol_item1 = store[stol_code][1]
stol_quantity0 = stol_item['quantity']
stol_quantity1 = stol_item1['quantity']
stol_quantity = stol_item['quantity'] + stol_item1['quantity']
print('Стол -', stol_quantity, 'шт, стоимость', stol_cost, 'руб')

divan_cost = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
divan_cost1 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']
divan_cost = divan_cost + divan_cost1
divan_code = goods['Диван']
divan_item = store[divan_code][0]
divan_item1 = store[divan_code][1]
divan_quantity0 = divan_item['quantity']
divan_quantity1 = divan_item1['quantity']
divan_quantity = divan_item['quantity'] + divan_item1['quantity']
print('Диван -', divan_quantity, 'шт, стоимость', divan_cost, 'руб')


stul_cost = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
stul_cost1 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
stul_cost2 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']
stul_cost = stul_cost + stul_cost1 + stul_cost2
stul_code = goods['Стул']
stul_item = store[stul_code][0]
stul_item1 = store[stul_code][1]
stul_item2 = store[stul_code][2]
stul_quantity0 = stul_item['quantity']
stul_quantity1 = stul_item1['quantity']
stul_quantity2 = stul_item2['quantity']
stul_quantity = stul_item['quantity'] + stul_item1['quantity'] + stul_item2['quantity']
print('Стул -', stul_quantity, 'шт, стоимость', stul_cost, 'руб')


# js={
#     'ID.IFCE':{
#         'ID-S':[0.2131,0.1244]
#     },
#     'ID.WEBER':{
#         'ID-S-WEBER':[0.1342,0.4285]
#     }
# }
# for i in js:
#     print(i)
# for uni,json in js.items():
#     print(f'\nUnidade: {json}')

#     for sensor,valor in json.items():
#         print(f'Sensor: {sensor} \nConsumo: {valor}\n')


json={
    'CATEGORIA 1':{
        'ID-SENSOR':['consumo', 0.2131,0.1244]
    },
    'ID.WEBER':{
        'ID-S-':['consumo', 0.1342,0.4285]
    }
}

for var1, var2 in json.items():
    print(f'Var1: {var1}\nVar2: {var2}')
    for var3, var4 in var2.items():
        print(f'var3: {var3}\nvar4: {var4}')
    print('-------------')
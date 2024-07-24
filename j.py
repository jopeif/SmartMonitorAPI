js={
    'ID.IFCE':{
        'ID-S':[0.2131,0.1244]
    },
    'ID.WEBER':{
        'ID-S-WEBER':[0.1342,0.4285]
    }
}
for i in js:
    print(i)
for uni,json in js.items():
    print(f'\nUnidade: {json}')

    for sensor,valor in json.items():
        print(f'Sensor: {sensor} \nConsumo: {valor}\n')

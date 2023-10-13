import json

# data2 = '{"car": "a1", "name": "name1", "test":[1,2]}'
# data1 = '{"cars":[{"a":"1", "b":"2"}, {"c":"3", "d":"4"}]}'

data = '''
{
    "cars": [
        {
            "brand": "Mercedes",
            "model": "clx",
            "year": 2023,
            "color": "Red"
        },
        {
            "brand": "Romet",
            "model": "superslider",
            "year": 2022,
            "color": "Silver"
        },
        {
            "brand": "Ford",
            "model": "Mustang",
            "year": 2021,
            "color": "Red"
        },
        {
            "brand": "Honda",
            "model": "Civic",
            "year": 2020,
            "color": "Blue"
        },
        {
            "brand": "Chevrolet",
            "model": "Camaro",
            "year": 2023,
            "color": "Black"
        },
        {
            "brand": "BMW",
            "model": "X5",
            "year": 2022,
            "color": "White"
        }
    ]
}
'''

def save_to_file(filename, datain):
    data1 = json.loads(datain)
    with open(filename, 'w') as json_data:
        json.dump(data1, json_data)


def read_from_data( jsondata):
    data1 = json.loads(jsondata)
    for car in data1['cars']:
        for feature in car:
            print(feature, "=>", car[feature])

def read_from_file( filename):
    with open(filename) as json_data:
        data1 = json.load(json_data)
        for car in data1['cars']:
            for feature in car:
                print(feature, "=>", car[feature])


read_from_data(data)
# save_to_file('dane3.json', data)
# read_from_file('dane3.json')

#{"Mercedes": {"brand": "Mercedes", "model": "clx", "year": 2023, "color": "Red"},"Romet":{}}
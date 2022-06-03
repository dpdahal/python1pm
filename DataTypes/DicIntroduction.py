# data = {
#     'name': 'zhangsan',
#     'age': 18,
#     'phone': 123456789,
# }
#
# print(data['name'])


# data = [
#     {'name': 'zhangsan', 'age': 18, 'phone': 123456789},
#     {'name': 'lisi', 'age': 19, 'phone': 123456789},
#     {'name': 'wangwu', 'age': 20, 'phone': 40000},
# ]
#
# print(data[1]['name'])
# print(data[2]['phone'])

# data={'name': 'zhangsan', 'age': 18, 'phone': 123456789}
# print(dir(data))
# print(data.keys())
# print(data.values())
# print(data.get('name'))


# data = []
#
# data.append('zhangsan')
# print(data)

# a = 234
# print(id(a))

# a = 10
# c = 10
# print(id(a))
# print(id(c))

# data = (1, 2, 3, 4, 5)
# data = list(data)
# print(data)


user = {
    'name': 'zhangsan',
    "address": {
        "province": "Nepal",
        "city": {
            "name": "Kathmandu",
        },
    }
}

print(user['address']['city']['name'])

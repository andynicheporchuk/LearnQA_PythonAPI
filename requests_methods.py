import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Запрос без параметра method: ", response1.text)

response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Запрос не из списка: ", response2.text)

response3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print("Запрос с верным параметром method: ",response3.text)

print("---------------------------------")
print("---------------------------------")

methods = [{"method": "POST"}, {"method": "GET"}, {"method": "PUT"}, {"method": "DELETE"}]


for method_type in methods:
     print("Значение параметра: ", method_type) # выводим тип метода
     response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method_type)
     # делаем запрос с вышевыведенным на экран методом
     print("Результат методом GET: ", response1.text) #  результат отправки запроса с параметром method_type

print("---------------------------------")

for method_type in methods:
    print("Значение параметра: ", method_type)
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method_type)
    print("Результат методом POST: ",response2.text)

print("---------------------------------")

for method_type in methods:
    print("Значение параметра: ", method_type)
    response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method_type)
    print("Результат методом PUT: ",response3.text)

print("---------------------------------")

for method_type in methods:
    print("Значение параметра: ", method_type)
    response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method_type)
    print("Результат методом DELETE: ",response4.text)


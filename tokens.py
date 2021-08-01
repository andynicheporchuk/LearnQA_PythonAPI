import requests, time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job") #создается задача
print(response.text)

parsed_response_text = response.json() # парсим json из первого запроса в текст
token = parsed_response_text["token"]
sec = parsed_response_text["seconds"]
# print(token)


response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
# делаем запрос с токеном ДО того как задача завершена
parsed_response_text2 = response2.json() # парсим json из второго запроса в текст
status = parsed_response_text2["status"]
print(response2.text)
# print(status)


if status == "Job is NOT ready":            # проверка правильности поля status ДО того как задача готова
    print("Статус верный, но токен был отправлен ДО готовности задачи")
else:
    print("Статус неверный, программа остановлена")
    quit()

time.sleep(sec)  # ждем определенное кол-во секунд до выполнения
print("Задача готова, выполнение последнего запроса")

response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
# # делаем запрос с токеном ПОСЛЕ того как задача завершена
parsed_response_text3 = response2.json() # снова парсим json из второго запроса в текст
status = parsed_response_text3["status"]
result = parsed_response_text3["result"]
print(response2.text)

if status == "Job is ready" and result: # проверка правильности поля status  наличия result после того как задача готова
    print("Статус верный, result присутствует - программа выполнена")
else:
    print("Статус неверный, программа остановлена")
    quit()

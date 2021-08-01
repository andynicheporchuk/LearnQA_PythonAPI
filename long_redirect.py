import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

all_responses = response.history
count_redirects = len(all_responses)

print("Количество переходов: ", count_redirects)
print("Итоговый URL: ",all_responses[-1].url)


import json

try:
    with open("data.json", "r", encoding="utf8") as file:
        dano = json.load(file)

    age_result = 0
    adult = []
    cnt = 0

    for element in dano:
        try:
            name = element["name"]
            age = element["age"]
            city = element["city"]
        except KeyError:
            print("Данных нет")
            continue
        
        cnt += 1
        age_result += age
        if age > 18:
            adult.append(element)
    
    age_avg = age_result / cnt
    result = (
        f"Средний возраст всех людей из списка: {age_avg}\n"
        f"Люди старше 18 лет: {adult}"
    )
    
    with open("result.json", "w", encoding="utf8") as result_file:
        json.dump({"average_age": age_avg, "adult": adult}, result_file, ensure_ascii=False, indent=4)
    

except FileNotFoundError or json.JSONDecodeError:
    print("Такого файла не существует или повреждён")
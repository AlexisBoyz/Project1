from typing import Dict

# ages = {
#     "Руслан": 10,
#     "Кирилл": 20,
#     "Оксана": 30,
# }
# print(f"Руслану {ages["Руслан"]} лет")

ages: Dict[str, int] = {
    "Руслан": 10,
     "Кирилл": 20,
    "Оксана": 30,
}
# ages["Petr"] = 30
ages.update({15: 15})
print(f"Анжелике {ages[15]} лет")
print(f"Руслану {ages["Руслан"]} лет")

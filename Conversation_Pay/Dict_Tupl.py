from typing import Dict, Tuple, List, Optional

def user_data(user_id:int, data: Dict[str, str]) -> Tuple[bool, str]:
    if user_id <= 0:
        return (False, "Передан некорректный ID")

    name = data.get("name", "Гость")
    # name = data['name']
    return (True,f"Пользователь '{name}' обработан")

def get_user_hobbies(user_id:int, database: Dict[int, Tuple[str, int, List[str]]]) -> List[str]:
    user = database.get(user_id, 0)
    if user == 0:
        return [f"error: {user}","Пользователь не найден"]

    return user[2]

def get_user_info(user_id:int, database: Dict[int, Tuple[str, int, List[str]]]) -> Optional[Tuple[str, int, List[str]]]:
    user =database.get(user_id)
    if user:
        return user
    return None

def add_hobby(user_id:int, database: Dict[int, Tuple[str, int, List[str]]], hobby: str) -> bool:
    user = database.get(user_id)
    if not user:
        return False

    name, age, hobbies = user
    hobbies.append(hobby)
    return True

user_database: Dict[int, Tuple[str, int, List[str]]] = {
    1: ("Petr", 25, ["Sport","Football", "swimming"]),
    2: ("Olga", 18, ["Cooking","shopping", "dancing"])
}


badID = 0
resultList = get_user_info(badID, user_database)
print(resultList)

goodID = 2
newHobby = "music listening"
res = add_hobby(goodID, user_database, newHobby)
if res == True:
    print(f"Новое хобби '{newHobby}' успешно добавлено")
resultList = get_user_info(goodID, user_database)
if resultList:
    name, age, hobbies = resultList
    print(f"{name} {age} лет, хобби: {', '.join(hobbies)}")



# badID = 0
# goodID = 1
# data: Dict[str, str] = {
#     "name": "Petr"
# }
# badResult = user_data(badID, data)
# goodResult =user_data(goodID, data)
#
# print(badResult)
# print(goodResult)
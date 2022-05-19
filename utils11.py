import json

def get_data_from_json():
    """Извлекаем данные из файла candidates"""
    with open('../11/candidates.json', encoding='utf-8') as file:
        raw_json = file.read()
    return json.loads(raw_json)

def load_candidates_from_json():
    """Функция возвращает список всех кандидатов"""
    full_list = get_data_from_json()
    candidates_list = [] #список всех кандидатов
    for i in full_list:
        x = (i['name'])
        candidates_list.append(x)
    return candidates_list

def get_candidate(candidate_id):
    """Функция возвращает одного кандидата по его id"""
    full_list = get_data_from_json()
    if 0 < candidate_id <= len(full_list):
        for i in full_list:
            if candidate_id == int(i['id']):
                return i
    else:
        return f'Неверный id'


def get_candidates_by_name(candidate_name):
    """Функция возвращает кандидата по имени"""
    candidate_list = []
    for i in load_candidates_from_json():
        if candidate_name.lower() in i.lower():
            candidate_list.append(i)
    return candidate_list


def get_candidates_by_skill(skill_name):
    """Функция возвращает кандидата по навыку"""
    k = 0
    candidates_list = []
    for i in get_data_from_json():
        if skill_name.lower() in i['skills'].lower():
            k += 1
            candidates_list.append(i)
    if k == 0:
        return f'Кандидатов с такими навыками не найдено'
    else:
        return candidates_list

#print(get_data_from_json())
#print(load_candidates_from_json())
#print(get_candidate(0))
#print(get_candidates_by_name('burt'))
#print(get_candidates_by_skill('python'))
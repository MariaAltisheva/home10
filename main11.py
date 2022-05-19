from flask import Flask, render_template
import json
from utils11 import *
app = Flask(__name__)

@app.route("/")
def page_all_candidates(): #выводим стартовую страницу со списком кандидатов
    all_candidates = load_candidates_from_json()
    name1 = all_candidates[0]
    name2 = all_candidates[1]
    name3 = all_candidates[2]
    name4 = all_candidates[3]
    name5 = all_candidates[4]
    name6 = all_candidates[5]
    name7 = all_candidates[6]
    return render_template('list.html', name1=name1, name2=name2, name3=name3, name4=name4, name5=name5, name6=name6, name7=name7)

@app.route('/candidate/<int:x>') #выводим кандидата по номеру
def page_candidate(x):
    all_canddates = get_data_from_json()
    for i in range(len(all_canddates)): #перебираем список c данными словаря
        if i == (x - 1):
            name1 = all_canddates[i]['name']
            position1 = all_canddates[i]['position']
            skills1 = all_canddates[i]['skills']
            picture1 = all_canddates[i]['picture']
    candidate = render_template('single11.html', name=name1, position=position1, skills=skills1, picture=picture1)
    return candidate

@app.route('/search/<candidate_name>') #выводим кандидатов по скиллам
def page_name_candidate(candidate_name):
    name1 = get_candidates_by_name(candidate_name)[0]
    count1 = len(get_candidates_by_name(candidate_name))
    id = load_candidates_from_json().index(name1)
    candidate = render_template('search11.html', count=count1, name=name1, x=id)
    return f'<h1>Найдено кандидатов: {count1}<h1>\n{candidate}'

@app.route('/skill/<skill_name>') #выводим кандидатов по скиллам
def page_skill_candidate(skill_name):
    candidate_list = get_candidates_by_skill(skill_name)
    skill_list = [] #список содержит только имена
    for i in candidate_list:
        skill_list.append(i['name'])
    count = len(skill_list)
    candidate = render_template('skill.html', count=count, items=skill_list)
    return candidate



app.run(host='127.0.0.1', port=800, debug=True)

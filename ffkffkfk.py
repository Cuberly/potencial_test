import csv


with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)[1:]
    count_class = {}
    sum_class = {}
    for id, name, titleProject_id, level, score in answer:
        if 'Хадаров Владимир' in name:
            print(score)
        count_class[level] = count_class.get(level, 0) + 1
        sum_class[level] = sum_class.get(level, 0) + (int(score) if score != 'None' else 0)

    for id, name, titleProject_id, level, score in answer:
        if score == 'None':
            score = round(sum_class[level] / count_class[level], 3)
with open() as file:
    w = csv.writer(file)
    w.writerow(['id', 'name', 'titleProject_id', 'class', 'score'])
    w.writerows(answer)


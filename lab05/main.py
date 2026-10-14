from tablestats import read_rows,count_types,total_minutes,to_csv

filename = 'events.csv'

with open(filename,'r',encoding = 'utf-8') as table:
    rows = read_rows(table)
res = count_types(rows)
print(total_minutes(rows,'ошибка'))
resualt = to_csv(counts)


if __name__ == '__main__':
    print(rows)
    print(res)
    print(total_minutes(rows,'ошибка'))
    print(resualt)

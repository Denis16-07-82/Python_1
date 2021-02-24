# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура',
# 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#Приступил к задаче 3
# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.
my_list=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
data='1234567890+-'
data_list=[]
print(id(my_list))
for ln in range(len(my_list)):
    for ln_1 in my_list[ln]:
        if data.count(ln_1)==1:
            data_list.append(ln)
            break
        else:
            ln+=1
            break
print(data_list)
for ln in data_list:
    if len(my_list[ln])==1:
        new_list=list(my_list.pop(ln))
        new_list.insert(0,'0')
        new_str=''.join(new_list)
        print(new_str)
        my_list.insert(ln,new_str)
    elif len(my_list[ln])==2 and (my_list[ln][0]=='+' or my_list[ln][0]=='-'):
        new_list = list(my_list.pop(ln))
        new_list.insert(1, '0')
        new_str = ''.join(new_list)
        print(new_str)
        my_list.insert(ln,new_str)
number=0
for index in range(len(data_list)):
    data_list[index]+=number
    my_list.insert(data_list[index],'"')
    my_list.insert(data_list[index]+2,'"')
    number+=2
print(my_list)
print(id(my_list))
print(' '.join(my_list))


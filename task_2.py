#TASK_2
data_list = list(input('введите свои данные:'))
num = 0
while data_list[num + 1]:
    element = data_list[num]
    data_list[num] = data_list[num+1]
    data_list[num+1] = element
    num = num + 2
    print(data_list)
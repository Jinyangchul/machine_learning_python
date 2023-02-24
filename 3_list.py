# list comprehension
# @@ for @@ in @@의 형태

# 0부터 3까지 x의 제곱수 리스트
print(list_data := [x**2 for x in range(4)])


raw_data = [[1, 5], [12, 234], [234, 2345], [3225, 2351], [2341, 235112]]

# 전체 x값의 리스트
print(all_data := [x for x in raw_data])
# x[0]값의 리스트
print(x_data := [x[0] for x in raw_data])
# y[1]값의 리스트
print(y_data := [y[1] for y in raw_data])


all_number = [x for x in range(10)]
# all_number 중 짝수만 담긴 리스트
even_number = [x for x in all_number if x % 2 == 0]

print(all_number, even_number)

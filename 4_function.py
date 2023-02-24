# 여러 값을 리턴 가능
def plusfunc(x):
    return x, x + 1, x + 2

# 튜플 형태로도 출력 가능


def plusfunc_tuple(x):
    return (x, x + 1, x + 2)


z, z1, z2 = plusfunc(3)
ans_tuple = (y, y1, y2) = plusfunc_tuple(3)
print(z, z1, z2, ans_tuple)


# default parameter : 따로 지정하지 않으면 기본 설정값을 사용함

def print_name(name, count=2):
    for i in range(count):
        print("name == ", name)


print_name("DAVE")
print_name("DAVE", 5)


# mutable / immutable parameter : list, numpy, dict / int, string, tuple
# mutable: 원래의 데이터형에 변화가 일어남

def mutable_immutable_func(int_x, input_list):
    int_x + 1
    input_list.append(100)


x, list = 10, [10, 20, 30]
mutable_immutable_func(x, list)

# x에는 아무 일도 안 일어나지만 list에는 100 원소가 추가됨
print(x, list)


# lambda function: 한 줄로 함수 작성, 수학에서 함수 표현 f(x)와 유사하다

f = lambda x: x + 100

for i in range(3):
    print(f(i))


# lambda function에서 입력받은 input 값을 꼭 : 이후의 식에 추가 하지 않아도 된다

def print_hello():
    print("Hello")


def test_lambda(s, t):
    print("input1 = ", s, "input2 = ", t)


s, t = 100, 200

fx = lambda x, y: test_lambda(s, t)
fy = lambda x, y: print_hello()

# 300, 600은 쓰이지 않는 값
fx(300, 600)
fy(300, 600)

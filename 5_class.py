class Person:

    # init: 생성자, 인스턴스가 만들어 질 때 한번만 호출됨
    # 파이썬에서는 class 매서드에 '자신의 인스턴스'를 나타내는 self를 반드시 써야함
    def __init__(self, name):
        self.name = name
        print(self.name, "is initiallized")

    def work(self, company):
        print(self.name, "is working in", company)

    def sleep(self):
        print(self.name, "is sleeping")


obj = Person("Park")
obj.work("Samsung")
obj.sleep()

# 파이썬에서는 메서드와 속성 모두 public
print("Current person object is", obj.name)


class Person_1:

    count = 0       # class variable : 해당 클래스로 생성된 모든 인스턴스가 공통으로 사용하는 변수

    def __init__(self, name):
        Person_1.count += 1
        self.name = name
        print(self.name, "is initiallized")

    def work(self, company):
        print(self.name, "is working in", company)

    def sleep(self):
        print(self.name, "is sleeping")

    @classmethod
    def getCount(cls):
        return cls.count


# Person_1에서 instance 2개 생성
obj1 = Person_1("Park")
obj2 = Person_1("Kim")

# method call
obj1.work("Samsung")
obj2.sleep()

# 파이썬에서는 메서드와 속성 모두 public
print("Current person object is", obj1.name, "and", obj2.name)

# class method 호출
print("Person Count ==", Person_1.getCount())

# class variable direct access
print(Person_1.count)


class PrivateMemberTest:

    def __init__(self, name1, name2):
        self.name1 = name1
        self.__name2 = name2        # private member variable
        print(name1, ",", name2, "is initiallized")

    def getNames(self):
        self.__printNames()
        return self.name1, self.__name2

    def __printNames(self):     # private member method
        print(self.name1, self.__name2)


obj = PrivateMemberTest("Park", "Kim")
print(obj.name1)
print(obj.getNames())
# 내부에서는 __method, __variable로 선언 가능하지만 외부에서 생성된 인스턴스에서 호출하면 에러
print(obj.__printNames())
print(obj.__name2)

# 외부 함수와 클래스 내부 매서드의 이름이 같을 때 벌어지는 일
# -> self 사용하지 않으면 외부 함수가 호출됨


def print_name(name):
    print("[def]", name)


class Sametest:

    def __init__(self):
        pass

    def print_name(self, name):
        print("[Sametest]", name)

    def call_test(self):
        print_name("Kim")           # 외부 함수가 호출
        self.print_name("Kim")      # 클래스 내부 메서드가 호출


obj = Sametest()

print_name("Kim")       # 클래스 외부의 def가 호출
obj.print_name("Kim")   # 클래스 메서드가 호출
obj.call_test()         # 클래스 메서드가 호출

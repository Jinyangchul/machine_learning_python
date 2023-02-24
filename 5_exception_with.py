def calc(list_data):
    sum = 0

    try:
        sum = list_data[0] + list_data[1] + list_data[2]
        if sum < 0:
            raise Exception("Sum is minus")     # 인위적으로 error 발생

    except IndexError as err:
        print(str(err))
    except Exception as err:
        print(str(err))
    finally:                                    # try 실행되든 except 실행되든 항상 마지막에 실행됨
        print(sum)


calc([1, 2])

calc([2, 3, -100])


# 일반적으로 파일, 세션을 사용할 때:

f = open("./file_test", "w")
f.write("Hello Python!!!")
f.close()

# with를 사용할 때: with 블록을 벗어나는 순간 파일이나 세션을 자동으로 close함
# 텐서플로우의 session 사용 시 자주 활용됨

with open("./file_test", "w") as f:
    f.write("Hello Python!!!")

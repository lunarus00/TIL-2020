def outer_func():
    id = 0

    def inner_func():
        nonlocal id
        id += 1
        return id
    return inner_func

make_id = outer_func()
print("make_id() 호출의 결과 : {0}".format(make_id()))
print("make_id() 호출의 결과 : {0}".format(make_id()))
print("make_id() 호출의 결과 : {0}".format(make_id()))

"""
8행의 return inner_func
outer_func의 id = 0 에 inner_func가 반환되어 id값이 증가하게 됨.
"""
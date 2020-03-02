print("jai mataji")

#Example1
'''
def function1():
    print("Subscribe Now!!")
fun2 = function1
del function1
fun2()
'''
# Example2
'''
def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = funcret(1)
print(a)
'''
# Example3
def db1(fun1):
    def nowexecut():
        print("Executing Now!!")
        fun1()
        print("Executed")
    return nowexecut
@db1
def who_is_gohil():
    print("Gohilo is Good Boy")
# who_is_gohil = db1(who_is_gohil)
who_is_gohil()

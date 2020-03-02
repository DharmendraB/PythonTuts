print("jai mataji")
import time

initial1 = time.time()
k = 0
while (k<45):
    print("This is Gohil DB")
    k +=1
print("while loop run in ",time.time()-initial1," Second")

initial2 = time.time()
for i in range(45):
    print("This is Gohil DB")
print("while loop run in ",time.time()-initial2," Second")


# local time print
localtime = time.asctime(time.localtime(time.asctime()))
print(localtime)

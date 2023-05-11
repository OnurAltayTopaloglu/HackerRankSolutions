# Direct Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

# if the code is wrong, change pypy3 to python3
# .pop() is used to remove a random element from the set in pypy3
# .pop() is used to remove the first element from the set in python3
x = int(input())
myset = set(map(int,input().split()))
cmd = int(input())
for i in range(cmd):
    cmds = list(input().split())
    if cmds[0] == "pop":
        try:
            myset.pop()
        except:
            pass
    elif cmds[0] == "remove":
        try:
            myset.remove(int(cmds[1]))
        except:
            pass
    elif cmds[0] == "discard":
        try:
            myset.discard(int(cmds[1]))
        except:
            pass
print(sum(myset))

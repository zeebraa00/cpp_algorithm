n,s = map(int,input().split())
num = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum) :
    global cnt

    if idx == n :
        return
    sum += num[idx]
    if sum == s :
        cnt += 1

    dfs(idx+1,sum)
    dfs(idx+1,sum-num[idx])

dfs(0, 0)
print(cnt)
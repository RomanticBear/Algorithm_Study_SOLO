# DFS, BFS Youtube(이코테 예제)

# DFS 연습예제

'''
gragh=[
    [], #0번(없는 노드)
    [2,3,8], #1번 노드
    [1,7],
    [4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited=[False]*9

def dfs(gragh,v,visited):

    visited[v]=True #방문 표시
    print(v,end=' ')

    for i in gragh[v]:
        if visited[i]!=True:
            dfs(gragh,i,visited)

dfs(gragh,1,visited)

'''
'''
# 코드설명

1. 첫 노드 방문 -> 방문 표시(True)

2. 인접 노드 전부 접근 -> 1과정 반복(재귀)

+ gragh 위에서 부터 아래까지 노드 번호 순
+ 노드 번호 안헷갈리게 접근하기 위해 첫번째 원소 -> []

'''


# BFS 연습문제
'''
from collections import deque

gragh=[
    [], 
    [2,3,8], 
    [1,7],
    [4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited=[False]*9


def bfs(gragh,start,visited):
    # 시작 노드값 담은 자료형 선언
    queue=deque([start])
    visited[start]=True

    # 큐가 빌 때까지 반복
    while queue:
        v=queue.popleft()
        print(v,end=' ')

        for i in gragh[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i]=True

bfs(gragh,1,visited)
'''
'''
# 코드설명

1. 시작 노드 -> 큐에 담기, 방문 표시
2. 큐에 제일 앞에 담긴 값(v) pop, 인접 노드 중 방문 하지 않은 노드 -> 큐에 추가
3. 2번 과정 반복 -> 큐가 빌 때까지 반복(while문)
'''


# DFS 실전문제 _ 음료수 얼려 먹기

# 내 풀이

'''
# gragh생성
n,m=map(int,input().split())
gragh=[]

for i in range(n):
    gragh.append(list(map(int,input())))


# 상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]


result=0

# DSF
def dsf(gragh,x,y):
    global result
    
    if gragh[x][y]==0:
        gragh[x][y]=True # 방문처리

        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if nx<0 or nx>n-1 or ny<0 or ny>m-1:
                continue

            if gragh[nx][ny]==0:
                dsf(gragh,nx,ny)  # 문제점 -> for문 처음 부터 시작, for문 ->함수 밖
            else:
                pass
    

# result 위치 어디하면 될까..?

for i in range(n):
    for j in range(m):
        if gragh[i][j]==0:
            result+=1
            dsf(gragh,i,j)

print(result) 

'''


'''
# Youtube 풀이

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if gragh[x][y]==0:
        # 방문처리
        gragh[x][y]=1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)  # 나머지는 인접 노드 -> 방문 처리
        return True
    else:
        return False 
        

n, m = map(int,input().split())

gragh=[]
for i in range(n):
    gragh.append(list(map(int,input())))

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1 # 처음 방문 한 노드 -> result 1추가

print(result)

'''


# BFS 실전문제 _ 미로 탈출

'''

from collections import deque

n,m = map(int,input().split())
gragh=[]

for i in range(n):
    gragh.append(list(map(int,input())))

# 상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bsf(x,y):
    queue=deque()
    queue.append((x,y)) # 튜플 형태로 좌표값 입력
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 벽
            if nx<0 or nx>n-1 or ny<0 or ny>m-1:
                continue  # 재귀x -> return 반환 X / pass, continue O
            # 몬스터
            if gragh[nx][ny]==0:
                continue
            
            # 방문하지 않은 노드
            if gragh[nx][ny]==1:
                gragh[nx][ny]=gragh[x][y]+1
                queue.append((nx,ny))

    return gragh[n-1][m-1]

print(bsf(0,0))


'''

# 1303 전투

'''
import sys
sys.setrecursionlimit(10**6)

N,M=map(int,input().split())

gragh=[]
for i in range(N):
    gragh.append(list(input()))


dx=[-1,1,0,0]
dy=[0,0,-1,1]


def dsf(x,y,cnt,col):
    
    gragh[x][y]==0 # 방문처리

    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        # 벽
        if 0<=nx<N and 0<=ny<M:
            if gragh[nx][ny]==col:
                cnt=dsf(nx,ny,cnt+1,col)
    return cnt
    

white=0
black=0

for i in range(N):
    for j in range(M):
        if gragh[i][j]=='W':
            white+=(dsf(i,j,1,'W'))**2
        elif gragh[i][j]=='B':
            black+=(dsf(i,j,1,'B'))**2
            
print(white,black)

# [참고]
# https://hseungyeon.tistory.com/232

'''


# 24463 미로

# bfs 구현 시도 -> 지나온 좌표를 저장해야할 방법 모르겠음,, dfs시도
'''
from collections import deque

N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(str,input())))

v=[[False for _ in range(M)] for _ in range(N)]
print(v)
est=[]  # 시작점, 끝점 좌표 담을 변수
for i in range(N):
    for j in range(M):
        if i==0 or j==0 or i==N-1 or j==M-1:
            if arr[i][j]=='.':
                est.append((i,j))

ax,ay=est[0][0],est[0][1]
bx,by=est[1][0],est[1][1]

def bfs(x,y):
    q=deque()
    v[x][y]=True # 방문 표시
    q.append((x,y))
    
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    
    while q:
        x,y=q.popleft()
        
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            
            if v[nx][ny]!=True and arr[nx][ny]=='.':
                q.append((nx,ny))
                
'''



# dfs 도전, 런타임에러

'''
N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(str,input())))

v=[[False for _ in range(M)] for _ in range(N)]

est=[]  # 시작점, 끝점 좌표 담을 변수
for i in range(N):
    for j in range(M):
        if i==0 or j==0 or i==N-1 or j==M-1:
            if arr[i][j]=='.':
                est.append((i,j))

ax,ay=est[0][0],est[0][1]
bx,by=est[1][0],est[1][1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans=[]

def dfs(x,y,path):
    if x==bx and y==by:
        path+=[(x,y)]
        ans.append(path)
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0<=nx<N and 0<=ny<M:
            if v[nx][ny] != True and arr[nx][ny] == '.':
                v[nx][ny]=True
                dfs(nx,ny,path+[(x,y)])

v[ax][ay]=True # 시작노드 방문처리
dfs(ax,ay,[(ax,by)])


for i in range(N):
    for j in range(M):
        if arr[i][j]=='.' and (i,j) not in ans[0]:
            arr[i][j]='@'

for i in range(N):
    print(''.join(arr[i]))

'''



# 7562 나이트의 이동

# dfs
# ?? What PBL?  >>  시간 초과 issue

'''
def dfs(i,j,cnt):
    global ans

    #print(i,j)


    # 도착점 도착
    if lst[i][j]==2:
        ans=min(ans,cnt)
        # print('check')
        return
    
    di = [-1, 1, 2, 2, 1, -1, -2, -2]
    dj = [2, 2, 1, -1, -2, -2, -1, 1]

    for k in range(8):
        ni,nj=i+di[k],j+dj[k]
        
        # 체스판 out
        if 0<=ni<N and 0<=nj<N:
            if visited[ni][nj]!=1: # 방문하지 않았다면
                visited[ni][nj]=1 # 방췍
                dfs(ni,nj,cnt+1) 
                visited[ni][nj]=0


# main
N=int(input())
lst=[[0 for _ in range(N)] for _ in range(N)] # 체스판
visited=[[0 for _ in range(N)] for _ in range(N)] # 방문체크 배열

si,sj=map(int,input().split())
ei,ej=map(int,input().split())

lst[ei][ej]=2 # 도착점

ans=1e9
cnt=0 
dfs(si,sj,cnt)

print(ans)

'''



# bfs
# python3 말고 pypy 돌려야 시초 안뜸 
# What PBL ..?  방췍 리스트 이슈

'''
bfs를 사용해야 하는 이유

- 4방향 탐색이 아닌 8방향 탐색 -> 시간 복잡도 훨씬 큼

- bfs로 한번 이동한 좌표 -> 현좌표에서 한번 이동했을 때 갈 수 있는 최선의 좌표가 보장 됨

'''

'''
from collections import deque
import sys
input = sys.stdin.readline

# main
TC=int(input())

for _ in range(TC):
    
    N=int(input()) # 체스판 가로 길이
    si,sj=map(int,input().split()) # 시작점
    ei,ej=map(int,input().split()) # 목표점

    lst=[[0 for _ in range(N)] for _ in range(N)] # 체스판
    visited=[[0 for _ in range(N)] for _ in range(N)] # 방췍 배열
    
    q=deque()
    q.append((si,sj))
    visited[si][sj]=True # 시작점 방췍

    # bfs
    while q:
        i,j=q.popleft()

        # 나이트 이동방향
        di = [-1, 1, 2, 2, 1, -1, -2, -2]
        dj = [2, 2, 1, -1, -2, -2, -1, 1]

        for k in range(8):
            ni,nj=i+di[k],j+dj[k]

            if 0<=ni<N and 0<=nj<N:
                if visited[ni][nj]!=True:
                    q.append((ni,nj))
                    visited[ni][nj]=True
                    lst[ni][nj]=lst[i][j]+1

    # print(lst)
    print(lst[ei][ej])

'''


# BFS

# 개선
# 1. while문에서 목표점 도달 시 탈출  
# 2. 방문 체크 안사용해도 됨 -> BFS의 한번 이동은 최적해가 보장 되기 때문에 방문한 좌표에 대해서 더 이상 갱신이 일어나지 않음 -> 원본 테이블만 활용해서 사용하자

# Python3 통과

'''
from collections import deque
import sys
input = sys.stdin.readline


# bfs
def bfs():

    q=deque()
    q.append((si,sj))
    lst[si][sj]=1 # 시작점 방췍

    # bfs
    while q:
        i,j=q.popleft()

        if i==ei and j==ej:
            return lst[i][j]-1  # 처음 좌표(이동안했기 때문에 원래 0인데 방문처리 때문에 1로 시작함)를 1로 넣었으므로 이동횟수 1감소


        # 나이트 이동방향
        di = [-1, 1, 2, 2, 1, -1, -2, -2]
        dj = [2, 2, 1, -1, -2, -2, -1, 1]

        for k in range(8):
            ni,nj=i+di[k],j+dj[k]

            if 0<=ni<N and 0<=nj<N:
                if lst[ni][nj]==0:
                    q.append((ni,nj))
                    lst[ni][nj]=lst[i][j]+1

    return lst[ei][ej]


# main
TC=int(input())

for _ in range(TC):
    
    N=int(input()) # 체스판 가로 길이
    si,sj=map(int,input().split()) # 시작점
    ei,ej=map(int,input().split()) # 목표점
    lst=[[0 for _ in range(N)] for _ in range(N)] # 체스판
    ans=bfs()  # bfs 실행
    
    print(ans) 

'''





















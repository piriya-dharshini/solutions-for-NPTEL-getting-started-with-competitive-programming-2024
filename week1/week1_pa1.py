from copy import deepcopy
t=int(input())
for testcase in range(t):
    c=int(input())
    l=list(map(int,input().split()))
    p=l[0]
    q=l[1]
    #creating the snake body
    snake=[]
    for i in range(p):
      snake.append(list(map(str,input().split())))
    #moving the snake body
    snake1=deepcopy(snake)
    for moves in range(c):
      for j in range(p):
          for k in range(q):
              if (p-1,q-1)==(j,k):
                snake[0][0]=snake1[p-1][q-1]
              elif (j,q-1)==(j,k):
                snake[j+1][0]=snake1[j][k]
              else:
                snake[j][k+1]=snake1[j][k]
      snake1=deepcopy(snake)
    
    for m in range(p):
        for n in range(q):
            if n==q-1:
           	  print(snake[m][n])
            else:
              print(snake[m][n],end=' ')
       
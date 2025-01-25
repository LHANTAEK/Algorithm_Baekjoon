n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = blue = 0

def ckp(x, y, n):
   color = paper[x][y]
   for i in range(x, x + n):
       for j in range(y, y + n):
           if paper[i][j] != color:
               return False
   return True

def cut(x, y, n):
   global white, blue
   
   if ckp(x, y, n):
       if paper[x][y] == 0:
           white += 1
       else:
           blue += 1
       return
   
   n = n // 2
   cut(x, y, n)
   cut(x, y + n, n)
   cut(x + n, y, n)
   cut(x + n, y + n, n)

cut(0, 0, n)
print(white)
print(blue)
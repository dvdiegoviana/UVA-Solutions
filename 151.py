def funcao(n,m):
 c = []
 i = 0
 cont=m
 while(len(c)<n):
  i=i%n
  try:
   c.index(i)
  except:
   if(cont==m):
    c.append(i)
    cont=1
   else:
    cont=cont+1
  i=i+1
 return i;
 
 
while(1):
 inp=input()
 if(int(inp)==0):
  break;
 n=int(inp)
 t=1
 while(funcao(n,t)!=13):
  t=t+1
 print(t)
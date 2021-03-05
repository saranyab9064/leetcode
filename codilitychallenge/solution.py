def solution(n):
   res = []
   for i in range(1,24):
       if i%30 == 0:
           print('CodilityTestCoders')  
       elif i%6 == 0:
               print('CodilityTest')  
       elif i%15 == 0:
               print('TestCoders') 
       elif i%10 == 0:
               print('CodilityCoders')            
       elif i%2 == 0:
           res  = 'Codility'
           print(res)
       elif i%3 == 0:
           res = 'Test'
           print(res)
       elif i%5 ==0:
           res = 'Coders'
           print(res)
       else:
           print(i)
       

solution(10)

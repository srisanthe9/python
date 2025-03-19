l=[1,1,1,1,1]#created an empty list
for i in l:
    if l.count(i)>1:
        l.remove(i)
print(l)
#my i points to first 1 and my count is 5 
#now i am removing first 1
#now my list consists of 4 1's
#my for loop points to 2nd 1 in my list and when i remove '1' it removes 1st 1 in my list
#now my list constist of 3 1's
#my for loop points to 3rd element in my list and when i remove '1' it removes 1st 1 in my list
#now my loop consists 2 1's but my for is ended
#so i will get output two 1's 
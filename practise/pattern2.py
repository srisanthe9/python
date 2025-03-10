#Write a Python program to print the alphabet pattern 'A'.
#Expected Output:
"""
  ***   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *                                                                  
 *   *
      """
for i in range(1,8):
    if(i==1):
        print(' ***')
    if(i==4):
        print('*****')
    else:
        print('*   *')

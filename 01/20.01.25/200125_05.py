"""
for문을 이용해 *을 표시하라
    *
   **
  ***
 ****
*****
"""

for i in range(5):
    print(' '*(4-i), end = '')
    print('*'*(i+1))

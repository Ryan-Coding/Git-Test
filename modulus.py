mylist = [3, 8, 17, 14, 26, 31, 40, 12, 19]

EvenNO = [x for x in mylist if x%2==0]

OddNO = [x for x in mylist if x%2==1] 

print(f"this is the original list:    {mylist}")

print(f"this contains all the even NO from the main list:    {EvenNO}")

print(f"this contains all the odd NO from the main list:    {OddNO}")
N = int(input("Enter the number : "))
for i in range(1, N // 2 +2):
   for j in range(1, N +1):
       if j == i or j == N - i +1:
           print(j, end = "")
       else:
           print(" ", end = "")
   print()
a=input();l=len(a)
print(max([a[i:j+1]for i in range(l)for j in range(i,l)if list(a[i:j+1])==sorted(list(a[i:j+1]))],key=lambda x:len(x)))
a=input();l=[a[:i] for i in range(len(a),0,-1)]
print(*l[:len(a)-1],*reversed(l))
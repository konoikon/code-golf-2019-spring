# print(sum(c!=e for c,e in zip(str(bin(int(input())))[2:].zfill(31),str(bin(int(input())))[2:].zfill(31))))

with open('/Users/kon.oikon/Desktop/golf/code-golf-2019-spring/inputs/2.txt','r') as f:
    print(*[sum(c!=e for c,e in zip(str(bin(int(line.split()[0])))[2:].zfill(31),str(bin(int(line.split()[1])))[2:].zfill(31)))
          for line in f.readlines()])
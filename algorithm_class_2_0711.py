word = input()
croatias = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")     #변하지 않을 값이므로 튜플로 쓰는게 좋음

# ljc=aaa -> 5
# 00aaa -> len(word) : 5  # 모든 크로아티아 문자를 0으로 치환하고 문자 길이를 구하면 됨.

for croatia in croatias:
    word = word.replace(croatia, "0")  #변수지정을 해야 바뀜;

print(len(word))


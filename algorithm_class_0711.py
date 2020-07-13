
word = input().upper()  # 싹다 대문자로 바꿔줌


alphabets = {}

#알파벳을 key로 갖는 딕셔너리를 만들거임.
# ABCC
# alphabets = {}
# value를  sorting해서 값을 도출해내면 끝.


for letter in word:
    if letter in alphabets:  # 딕셔너리에 in하면 key값을 도출해내줌.
        alphabets[letter] += 1
    else:
        alphabets[letter] = 1  #이 부분 없으면 리스트에 아무것도 안담김.

print(alphabets)


alphabets = sorted(alphabets.items(), key=(lambda x: x[1]), reverse=True)   #내림차순으로 정렬

print(alphabets[0][0])

if len(word) > 1 and alphabets[0][1] == alphabets[1][1]:
    print("?")
else:
    print(alphabets[0][0])


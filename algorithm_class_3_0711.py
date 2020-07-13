count = int(input())

#aabb -> ["a", "b"]
def check_group(word):    # input = str,output = Boolean
    last_alphabet = ""
    alphabets =[]
    for letter in word:
        if letter == last_alphabet:
            continue
        else:
            if letter in alphabets:  # 문자가 이미 있는지 없는지 검사
                return False
            else:
                alphabets.append(letter)
                last_alphabet = letter

    return True #다 돌게되면 그룹단어가 맞는거라 True.

result = 0
for _ in range(count):   # for문에선 리스트에 해당하는 아이템값을 안쓰려면 _ (언더바) 처리를 해주면 됨
    word = input()
    if check_group(word):
        result += 1

print(result)
# 1. letter 연속적인가?  (aabb가 나올 때 연속적인지 보려면 직전 알파벳이 letter가 같은지 보면 됨.)
# 2. 이미 나왔던 단어인가?  (aabbaa가 나올 때
# 3. 연속을 깨뜨릴때, 이미 나왔던 알파벳인지 검사 -> False이면 그룹단어가 아님.



# <---------------------------------------->

# 제로 문제 : stack 과 관련있음 first-in, last-out
다시 한 번 봐보기:
# 4. 제로
class Stack:
    def __init__(self):
        self.__arr = []
        self.__top = 0

    def push(self, item):
        self.__arr.append(item)
        self.__top += 1

    def isEmpty(self):
        if self.__arr == []:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.__top -= 1
            item = self.__arr[self.__top]
            del(self.__arr[self.__top])

            return item

    def total_sum(self):
        sum = 0
        for num in self.__arr:
            sum += num
        return sum


count = int(input())
stack = Stack()

for _ in range(count):
    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.push(num)

print(stack.total_sum())
try:
    오류가 날 수 있는 부분~
except Exception as e:
    index_result = -1


find 와 달리 인덱스는 오류가능성이 있으므로 이렇게 처리를 해줄 수 있음

#django 에서 그나마 많이 쓰이는 문법

#split
    splitted_list = ex_str.split("?")
    print(splitted-list)
    >>> 다 자른 다음에 리스트 형태로 반환시켜줌


#join
    joined_str = "-".join(splitted_list)
    print(joined_str)

#replace (크롤링시 유용)
    replaced_str = ex_str.replace("Bumsu", "Piro")
    print(replaced_str)

    >>> 원하는 문자 형태로 만들어서 작업에 활용하는데에 유용(문자열 조작 함수 많이 알아둘 것!)

# strip (크롤링시 유용)
    text = "             data          "
    >>HTML 파싱하다보면 이런 공백 많음
    print(text.strip()) -> 안쪽의 공백이 사라지지 않음. -> 없애주려면 replace(" ", "")이렇게 치환하면 됨


# f string (3.6버전 부터 나왔음)
    장고 사용할 때 버전 확인 하기!

    print(f'{text}') >> f스트링 사용을 권장함 (explicit함.)
    문자열 포맷팅을 print 뿐만 아니라 변수 설정에도 이용할 수 있음.
    a = f'{text}'  이런식으로 함.


# list
    append, pop, remove :코딩도장으로 충분
    #extend
    list_1 = [1, 2, 3]
    list_2 = [4, 5]
    list1.extend(list_2)
    print(list_1) = [1,2,3,4,5]
    리스트를 연장시킬 수 있음. but 원본 리스트가 데이터가 변형 된다는 점 주의.

list1=[1,2,3]
list2=[4,5]
list3=list1.extend(list2)
print(list3) = none

>> why? extend 는 return 값이 없음. (메소드의 특성)

    람다? 때 활용 예정

# dictionary (엄청 많이 쓰임. 장고에서 템플릿 넘길때 딕셔너리 형식으로 넘김)

    ex_dic = {
        "name": "bumsu",
        "age": 25,
    }

    ex_dic["addres"] ="용산"
    print(ex_dic)

# 익명함수 lamda -> 함수인데 이름이 없음
# 함수 호출 방법 : 이름을 쓰고 인자를 준다.
lamda함수를 언제 쓰나? : 간단한 함수 사용시 쓰임.
or 인라인에서 사용할 때 (한 문장 내에서 함수 분리하긴 과하고, 안에서 쓰고싶기는 할 때)

print((lamda x, y: x+y)(1, 2))
(lamda x, y: x+y) >>이게 람다함수 선언
(1,2) >> 이게 함수 실행임.


print((lamda x, y: x+y))
>>> <function <lambda> at <~~~> 이렇게 뜨는데, 함수 자체를 출력해서 그럼. (함수를 실행한 것이 아님.)
>>> ex) print(sum)이거랑 같음.
>>> lambda 선언 이후 꼭 실행해야함

# map (lambda랑 만나면 좋은 시너지 발휘함)

#map -> 리스트를 받아서 func(item) 펑션처리 되어 결과 리스트를 반환함.
# map(function, list) : list 속 아이템을 하나하나 순환하면서 function 수행하여 리스트로 반환함.
numbers = [1,2,3,4,5]
map_2 = list(map(lambda number: number + 10, numbers))
>>map 을 list로 감싸준이유 : map은 오브젝트를 반환하기 때문. -> 리스트로 변환해야 실제로 사용할 수 있는 리스트가 됨.

# lambda랑 map 없이 구현해보기.
map_3 =[]
def sum10(number):
    return number + 10

for number in numbers:
    result = sum10(number)
    map_3.append(result)


 map_2랑 map_3는 똑같이 나옴. 엄청나게 줄을 줄일 수 있음


람다에서 if문쓸 때 논리연산자로 사용불가능한가요?

ex_lambda = (lambda x: x+10 if x>10 else x - 10)
print(ex_lambda(5))

# filter (map이랑 비슷함)  -> 불형값을 리턴하는것을 값으로 넣어야 함.
numbers = [1,2,3,4,5]
ex_filter_1 = list(filter(lambda x: x > 3, numbers))

def compare(x):
    return x > 3

ex_filter_2 =[]
for number in numbers:
    if compare(number):
        ex_filter_2.append(number)

print(ex_filter_2)

map은 10개의 인자가 있으면 무조건 결괏값도 10개임
filter는 조건에 따라 인자의 갯수를 줄일 수 있음. but 인자를 바꾸진 못함.



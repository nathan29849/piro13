# class Annie:
#     def __init__(self, health, mana, ability_power):
#         self.health = health
#         self.mana = mana
#         self.ability_power = ability_power
#
#     def tibbers(self):
#         print(f"티버: 피해량 {self.ability_power * 0.65 + 400}")
#
#
# health, mana, ability_power = map(float, input().split())
#
# x = Annie(health=health, mana=mana, ability_power=ability_power)
# x.tibbers()

# 35-6

# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#
#     @classmethod
#     def from_string(cls, time_string):
#         hour, minute, second = map(int, time_string.split(":"))
#         return cls(hour, minute, second)
#
#     @staticmethod
#     def is_time_valid(time_string):
#         hour, minute, second = map(int, time_string.split(":"))
#         return hour <= 24 and minute <= 59 and second <= 60
#
# time_string = input()
#
# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print('잘못된 시간 형식입니다.')

# 36-9

# class Animal:
#     def eat(self):
#         print('먹다')
#
#
# class Wing:
#     def flap(self):
#         print('파닥거리다')
#
# class Bird(Animal, Wing):
#     def fly(self):

#         print("날다")


# class NotPalindromeError(Exception):
#     def __init__(self):
#         super().__init__('회문이 아닙니다.')
#
# def palindrome(a):
#     if a == a[::-1]:
#         print(a)
#     else:
#         raise NotPalindromeError
#
# try:
#     word = input()
#     palindrome(word)
# except NotPalindromeError as e:
#     print(e)



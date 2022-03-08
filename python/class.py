# 파이썬 클래스
# self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스: 각각의 객체를 인스턴스화 할 때 저장된 공간.
# 클래스 변수: 직접 사용가능, 객체보다 먼저 생성된다.
# 동일한 클래스로 만든 객체끼리는 서로 영향을 미치지 않으며 고유한 성격을 가지고있다. 
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용.

# 예제1
# 선언 (PascalCase사용)
class UserInfo:
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name: ", self.name)

# 파이썬의 생성자(Constructor) 란 객체가 생성될 때 자동으로 호출되는 메서드를 말한다. 
# 파이썬에서 __init__메서드가 생성자 이다. 객체를 생성할때 생성자에 필요한 값을 같이 전달해줘야 한다. 

user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()
print(user2.name)
print(user2.__dict__) # 네임스페이스 출력
# 스페이스는 인스턴스가 가지고 있는 자신의 저장공간.

# 클래스를 생성해서 인스턴스화 시켜서 사용한다. 인스턴스화 된 변수들은 서로 독립적인 네임 스페이스를 둔다. 

# 예제2
# self의 이해 
# 클래스 메서드, 인스턴스 메서드
class SelfTest():
    def function1(): # 클래스 메서드
        print('function1 called')
    def function2(self): # 인스턴스 메서드
        print('function2 called')

self_test = SelfTest()
# self_test.function1() 오류
SelfTest.function1() # 클래스 변수는 직접 접근해야한다. 
self_test.function2()
SelfTest.function2(self_test)


# 예제3
# 클래스 변수, 인스턴스 변수
# 해당개념을 통해 중복코드를 줄일 수 있다. 
class WareHouse():
    # 클래스 변수(self 없음)
    stock_num = 0 # self가 없기 때문에 공동으로 공유한다. 여러 인스턴스에서
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
        # 창고가 하나 생길때 마다 전체 스탁넘을 1씩 추가해 준다.
    def __del__(self): # 인스턴스가 종료될 때 호출되는 함수
        WareHouse.stock_num -= 1

user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 출력해 보면 stock_num : 3 인걸 확인할 수 있음
# 클래스 네임스페이스, 클래스 변수는 공유된다 .

print(user1.name)
print(user1.stock_num) # 본인의 네임스페이스에 없으면 클래스 네임 스페이스에 가서 찾고 없으면 오류
print(user2.stock_num) # 3
print(user3.stock_num) # 3

del user1
print(user2.stock_num) # 2



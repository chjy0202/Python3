# 파이썬 클래스
# self, 클래스, 인스턴스 변수

# 선언 (PascalCase사용)

class UserInfo:
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("Name: ", self.name)

user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()
print(user2.name)
print(user2.__dict__) # 네임스페이스 출력
# 스페이스는 인스턴스가 가지고 있는 자신의 저장공간.

# 클래스를 생성해서 인스턴스화 시켜서 사용한다. 인스턴스화 된 변수들은 서로 독립적인 네임 스페이스를 둔다. 
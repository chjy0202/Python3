# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 상속이 필요한 이유 - 코드를 재사용 할 수 있고, 중복되는 코드를 줄일 수 있다. 
# 즉 코드의 생산성 및 유지보수. -> 이는 가독성과도 연관이 있음 

# 라면 -> 속성(종류, 회사, 맛, 면 종류 , 이름) : 부모

class Car():
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car class "show Method!"'

class BmwCar(Car): # Car class 를 상속받음
    """Sub Class"""
    def __init__(self, car_name, tp, color): # 부모한테 넘길 tp 와 color 까지 받는다.
        super().__init__(tp, color) # 부모에게 넘겨줌
        self.car_name = car_name

    def show_model(self):
        return "Your Car Name : %s" %self.car_name

class BenzCar(Car): # Car class 를 상속받음
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self):
        return "Your Car Name : %s" %self.car_name

    def show(self):
        print(super().show())
        return "Car Color: %s" %self.color


model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color) # red 부모클래스
print(model1.car_name) # 520d 자식클래스
print(model1.show())
print(model1.__dict__) # {'type': 'sedan', 'color': 'red', 'car_name': '520d'}

# Method Overriding (오버라이딩)
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show()) # Car Color: black
# 부모에 있는 메서드와 동일한 이름으로 메서드를 수정하여 생성하면 자식메서드가 먼저 호추룀. 
# 덮어쓰기 된다. 

# Parent Method Call
# super().show() 해주면 부모메서드도 함께 출력이 된다. 

# 상속의 뎁스가 깊을 때
# Inheritance Info
print(BmwCar.mro())

# 예제2
# 다중 상속

class X():
    pass
class Y():
    pass
class Z():
    pass

class A(X, Y):
    pass
class B(Y, Z):
    pass
class M(A, B, Z):
    pass

print(M.mro())
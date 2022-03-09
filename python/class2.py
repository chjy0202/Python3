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

    def Show(self):
        return 'Car class "show Method!"'

class BwmCar(Car): # Car class 를 상속받음
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
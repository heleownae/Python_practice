# 코드 작성
class Customer:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.points = 0

    def join_customer(self, name, email, points):
        self.name = name
        self.email = email
        self.points = points
        # print(f"이름: {name}, 이메일: {email}, 잔여 포인트: {points}")

    def add_points(self, amount):
        # before_add = self.points
        self.points += amount
        # print(f"기존 포인트: {before_add}, 추가 후 포인트: {self.points}")

    def reduce_points(self, amount):
        # before_reduce = self.points
        self.points -= amount
        if self.points < 0:
            self.points = 0
        # print(f"기존 포인트: {before_reduce}, 감소 후 포인트: {self.points}")


# 확인 코드
customer1 = Customer()
customer1.join_customer("Alice", "alice@example.com", 100)
customer1.add_points(50)
customer1.reduce_points(20)
customer1.reduce_points(150)  # 포인트 부족 상황 테스트
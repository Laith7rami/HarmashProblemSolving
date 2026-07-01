class Person:
    ID = 0

    def __init__(self, name, phone, gender):
        Person.ID += 1
        self.ID = Person.ID
        self.name = name
        self.Phone = phone
        self.gender = gender

    def print_info(self):
        print(f"{self.name}\n{self.gender}\n{self.Phone}")


class Employee(Person):
    def __init__(self, name, phone, gender, salary, work_time):
        super().__init__(name, phone, gender)
        self.salary = salary
        self.work_time = work_time


class Client(Person):
    def __init__(self, name, phone, gender, email):
        super().__init__(name, phone, gender)
        self.email = email


class Product:
    __ID = 0

    def __init__(self, name, price):
        Product.__ID += 1
        self.id = Product.__ID
        self.name = name
        self.price = price


class Order:
    __ID = 0

    def __init__(self, date, paid, person):
        Order.__ID += 1
        self.Id = Order.__ID
        self.date = date
        self.Is_paid = paid
        self.person = person
        self.products = []


class Company:
    person = []
    products = []
    order = []

    @staticmethod
    def add_product(name, price):
        Company.products.append(Product(name, price))

    @staticmethod
    def add_order(date, paid):
        preson = Person(input("name:"), input("phone :"), input("gender:"))
        Company.order.append(Order(date, paid, preson))

    @staticmethod
    def add_person(name, phone, gender):
        person = Person(name, phone, gender)
        Company.person.append(person)
        return person

    @staticmethod
    def remove_product(id):
        for i in Company.products:
            if i.id == id:
                Company.products.remove(i)
                print(f"remove {i.name}")
                return
        print("the product is not exist")

    @staticmethod
    def remove_person(id):
        for i in Company.person:
            if i.ID == id:
                Company.person.remove(i)
                print(f"remove {i.name}")
                return
        print("the person is not exist")

    @staticmethod
    def remove_order(id):
        for i in Company.person:
            if i.id == id:
                Company.order.remove(i)
                print(f"remove {i.Id}")
                return
        print("the Order is not exist")
    @staticmethod
    def print_info_person(id):
        for i in Company.person:
            if i.ID == id:
                print(f"{i.name}\n{i.gender}\n{i.Phone}")

                # التي يملكها email سيتم طباعة الخاصية Client تم إنشاؤه من الكلاس person إذا كان الكائن

                # داله الانستانس تتاكد له البراميتر الاول نسخه من البراميتر الثاني
              # isinstance(1,2)
                if isinstance(i, Client):
                    print("Email:", i.email)
                elif isinstance(i, Employee):
                    print("Salary:", i.salary)
                    print("Working time", i.work_time)
                return
        print("the person is not exist")
    @staticmethod
    def print_detail_prod(ID):
        for i in Company.products:
            if i.id == ID:
                print(f"{i.name}\n{i.price}")
                return
        print("the product is not exist")
    @staticmethod
    def print_detail_order(ID):
        for i in Company.order:
            if i.Id == ID:
                print(f"{i.person.name}\n{i.ispaid}\n{i.date}\n")
                total = 0
                for j in i.products:
                    total += j.price
                    print(f"{j.name}\n{j.price}\n total = {total}")
                return

    @staticmethod
    def print_person_order(ID):
        exist = False
        person = True
        for i in Company.person:
            if i.ID == ID:
                person = i
                exist = True

                break
        if not exist:
            print(" person not found")
            return
        print(" founds")




# n = Product("shoes",200)
# x = Product("shoes blue",250)
# y = Product("shoes red",300)
Company.add_product("shoes", 200)
Company.add_product("shoes blue", 250)
Company.add_product("shoes red", 300)
# print(Company.products)
Company.add_person("ahmed", 98384934, "male")
Company.add_person("ali", 98384934, "male")
Company.add_person("fatima", 98384934, "fmale")
# Company.remove_person(3)
#Company.print_info_person(3)
#Company.print_detail_prod(3)

Company.print_person_order(7)
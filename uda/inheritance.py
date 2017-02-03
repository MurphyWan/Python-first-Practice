class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("child constructor called")
        Parent.__init__(self,last_name, eye_color)
        self.number_of_toys = number_of_toys

#murphy_wan = Parent("Wan", "black")
#print(murphy_wan.last_name)

boyan_wan = Child("Wan", "black", 8)
print(boyan_wan.last_name)
print(boyan_wan.number_of_toys)

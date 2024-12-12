# class Rect:
#     def draw(self):
#         print("Drawing A Rectangle")

# class circle(Rect):
#     def draw(self):
#         print("Drawing a circle")
#         super().draw()

# c = circle()
# c.draw()

class Rect:
    def draw(self):
        print("Drawing A Rectangle")
        
class circle(Rect):
    def draw(self):
        print("Drawing a circle")
        super().draw()

c = circle()
c.draw()

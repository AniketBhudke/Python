from university import university
class college(university):
    def getclgdata(self):
        self.cname=input("Enter The Name Of tHe College:")
        self.cloc=input("Enter The Location Of your College:")
    def dispclgdata(self):
        print(f"The Name Of the college={self.cname}")
        print(f"The Location Of the College")

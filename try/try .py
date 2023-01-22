import termcolor 
import pyfiglet


class family:

    def __init__(self,n1,n2,n3) :
        
        self.first_name=n1
        self.midle_name=n2
        self.last_name=n3
        
    
    def all_name(self):


     return f"{self.first_name}{self.midle_name}{self.last_name}"


    def fantastic_name(self):
        
        return f"your first name is {self.first_name} , middle name is {self.midle_name} and your last name is {self.last_name}"


father=family("hassan","mohamed","Soffar")
son_1=family("mohamed","hassan","soffar")


x=pyfiglet.Figlet().renderText(father.last_name)
x=termcolor.colored(x,"red")
print(x)
print(termcolor.colored(father.fantastic_name(),"blue"))
print(termcolor.colored(son_1.fantastic_name(),"blue"))


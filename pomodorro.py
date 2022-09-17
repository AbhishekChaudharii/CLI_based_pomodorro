from datetime import datetime,timedelta
import time 
from termcolor import colored
from colorama import init
init(autoreset = True)


class pomodorro:
    def __init__(self):
       self.pomo_focus_min = [] # to store pomo time
       self.pomo_break_min = [] # to store total break time
        

    def main_menu(self):
        print(colored("\n \n \n \n 1. Pomodorro \n 2. Take a break \n 3. View Focus time \n 4. Exit Program \n \n \n \n","blue"))
        
#        print(colored('hello', 'red'), colored('world', 'green'))
        
        option = int(input("Choose option  "))
        if option == 1:
            self.setpomodorro()
        elif option == 2:
            self.breakpomo()
        elif option == 3:
            print(f"\n \n \n \n Total time you were focus was {sum(self.pomo_focus_min)} mins")
            print(f"You engaed your focus in the following blocks of time\n {self.pomo_focus_min} (in mins)")
            print(f"Total break time was {sum(self.pomo_break_min)} mins")
            print(f"You took breaks in the following blocks of time{self.pomo_break_min}\n \n \n \n (in mins)")
            self.main_menu()

        elif option == 4:
            print(colored("\n \n \n \n \n Thanks for using the program",'cyan'),colored(" \n Have a nice day! \n \n \n \n" , 'yellow'))
            exit()
        
            
            

    
    def countdown(self,t):
        
        """ Enter in mins"""
        t = t*60  # convert mins into secs
    
        while t:
            mins, secs = divmod(t, 60)
            #            (numerator and denominator)
            # returns quotient and remindar as tuples
            timer = '{:02d}:{:02d}'.format(mins, secs)


            print(timer, end="\r")  # print over the same line (end="\r")
            time.sleep(1) # delay of 1 sec
            t -= 1

    def setpomodorro(self):
       
        pomo_time = int(input("Set Pomodorro for how many minutes?   "))
        self.countdown(pomo_time)
        self.pomo_focus_min.append(pomo_time)
        self.main_menu()
        


        
    def breakpomo(self)    :
        break_time = int(input("Set break timer for how many minutes?  "))
        self.countdown(break_time)
        self.pomo_break_min.append(break_time)
        self.main_menu()
        
        
        
                
           
        
        
      
        

if __name__ ==  "__main__":
   
    pomodorro1 = pomodorro()
#    pomodorro1.setpomodorro()
    pomodorro1.main_menu()
#    time_min = int(input("Enter time in minutes for your pomodorro session :    "))
#    pomodorro1.countdown(time_min)



# Future scope:
# add pause feature , pause in between the countdown
    
    

    
        

        

        
        

        

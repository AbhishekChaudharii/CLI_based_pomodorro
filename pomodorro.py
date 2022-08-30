from datetime import datetime,timedelta
import time 
# import 
class pomodorro:
    def __init__(self):
        pass

    def setpomodorro(self):
        pomo = input("Set Pomodorro for how many minutes?   ")
        return pomo
    
    def now_and_now_time(self,flag=0):
        """if flag = 0 it will return datetime raw
        else it will return only time"""
        
        now = datetime.now()
        now_time = now.strftime("%H:%M:%S")

        if flag == 0:
            return now
        else:
            return now_time
    
    def timer(self):
        now = datetime.now()
        now_time = now.strftime("%H:%M:%S")
        return now


    # define the countdown func.
    def countdown(self,t):
        """ Enter in mins"""
    
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")  # print over the same line (end="\r")
            time.sleep(1) # delay of 1 sec
            t -= 1
        
        
        
        
        
        
        
                
             
             

         
         

        
        
        
      
        

if __name__ ==  "__main__":
   

    pomodorro1 = pomodorro()
    time_min = int(input("Enter time in minutes for your pomodorro session :    "))
    time_sec = time_min*60
    pomodorro1.countdown(time_sec)
    
    
    

    
        

        

        
        

        

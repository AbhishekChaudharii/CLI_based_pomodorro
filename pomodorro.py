from datetime import datetime,timedelta
#import time 
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


   
        
        

    def alert(self):
         pomo = self.setpomodorro()
         current_time = self.now_and_now_time()
         current_time_time = self.now_and_now_time(1)
         print(f"starting pomodorro at  {current_time_time} ")
         finish_time = current_time + timedelta(minutes=int(pomo))
         finish_time_time =  finish_time.strftime("%H:%M:%S")
         print(f"finishtime is {finish_time_time}")

         while current_time_time != finish_time_time:
#             
             delta = datetime.now() - current_time
#             print(delta.seconds)
             if delta.seconds >= 1:
                 current_time = datetime.now()
                 now_time = current_time.strftime("%H:%M:%S")
                 print(now_time)
                 # Update 't' variable to new time
                 current_time = datetime.now()



             if finish_time_time == self.now_and_now_time(1):
           
                 print("Done!!!!!!!!!!!!!!!!!!!!")
                 return input("Do you want to start the break? ")
             
    def break(self):
        print("Break will be 30% of the pomodorro time you set")
        
        
        
        
        
        
                
             
             

         
         

        
        
        
      
        

if __name__ ==  "__main__":
   

    pomodorro1 = pomodorro()
    pomodorro1.alert()
    
    
    
    

    
        

        

        
        

        

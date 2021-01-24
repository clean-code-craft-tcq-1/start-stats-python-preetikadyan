
def calculateStats(numbers):
  if (len(numbers) != 0): 
    return { "avg": sum(numbers)/len(numbers), "min": min(numbers), "max": max(numbers) } 
  else:
    return { "avg": 0, "min": 0, "max": 0 }
  
class StatsAlerter: 
    def  __init__(self,th,class_arr):
         self.th = th
         self.class_arr = class_arr
        
    def checkAndAlert(self,numbers):  
      if (max(numbers) > self.th): 
         self.class_arr[0].emailSent = True
         self.class_arr[1].ledGlows = True 
        
class EmailAlert:
    emailSent = False
    
class LEDAlert:
    ledGlows = False 
    
    

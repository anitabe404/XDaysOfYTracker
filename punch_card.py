class PunchCard():
    def __init__(self, size):
      self.slots = {}

      for key in range(1,size+1):
          self.slots[key] = False
    
    def punch(self, day):
        self.slots[day] = True
    
    def unpunch(self, day):
        self.slots[day] = False
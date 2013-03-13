import Leap, sys, math

class RPSListener(Leap.Listener): 
  past_hands = []
  count_down = 0
  
  def onInit(self, controller):
    #print "Initialized"
    return

  def onConnect(self, controller):
    #print "Connected"
    return

  def onDisconnect(self, controller):
    #print "Disconnected"
    return

  def onFrame(self, controller):
    result = do_one_player(self, controller)
    

  def count_fingers(self, controller):
    #Check to see if the Leap Motion senses a hand
    hands = controller.frame().hands()
    total = 0

    #if a hand is visible, grab the fingers on that hand
    if hands:
      if len(hands) >= 2:
        total += len(hands[1].fingers())
      total += len(hands[0].fingers())
      return total

  def average_num_fingers(self, controller):
    values = []
    for _ in range(1200):
      values.append(self.count_fingers(controller))

    temp = values[0]
    if values.count(temp) > 1000:
      return temp


def check_stable(hands_list):
  for h in hands_list:
    v = h.velocity()
    if v is None:
      return False
    if v.x > 100:
      return False
    if v.z > 100:
      return False
  return True

def play_alone(listen, controller):
    result = None
    while result == None:
      result = do_one_player(listen, controller)
    return result
    
def do_one_player(listen, controller):
  """Counts the number of times a player has pumped their hand.  After the third pump, records the number
     of fingers and turns that into a move"""
  frame = controller.frame()
  hands = frame.hands()
  if len(hands) != 1 or hands[0] is None:
      return
  hand = hands[0]
  if hand.velocity():
      if listen.count_down == 3:        
          listen.count_down = 0
          listen.past_hands = []
          return sign(hands[0], listen.average_num_fingers(controller))
      elif abs(hand.velocity().y) < 50:
          return None
      elif len(listen.past_hands) == 9:
          last_1 = sum(listen.past_hands[:3], 0) / 3
          last_2 = sum(listen.past_hands[3:6], 0) / 3
          last_3 = sum(listen.past_hands[6:], 0) / 3
          if last_1<-300 and last_3>300:
              listen.count_down += 1
              listen.past_hands = []
              return None
          if hand and listen.past_hands:
              shift_back(listen.past_hands)
              listen.past_hands[0] = hand.velocity().y
          return None
      else:
          if hand:
              listen.past_hands.append(hand.velocity().y)
          return None
  else:
      listen.past_hands = []
   
def shift_back(l):
    #shifts the elements in list l back by 1 index
    for i in range(len(l)-1)[::-1]:
        l[i+1] = l[i]
    
def sign(hand, num_fingers):
    fingers = hand.fingers()
    if num_fingers > 3:
        return 'paper'

    #depending on the orientation of the hand, sometimes the Leap only detects one finger, so this takes care of that case as well.
    if num_fingers > 1 or (num_fingers == 1 and fingers[0].length() > 50):
        return 'scissors'
    return 'rock'

import copy
def a(listt):
  littt[0] = 'b'
  print(littt)
def b(listt):
  littt =  copy.deepcopy(listt)
  littt[1] = 'b'
  print(littt)
def c(listt):
  listt[0] = 'b'
  print(listt)

littt = [0,1,2]
print(littt)
a(littt)
print(littt)
b(littt)
print(littt)
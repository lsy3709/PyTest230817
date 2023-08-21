

import sys
print(sys.getsizeof("a")) #<- 이건 a의 코드값을 출력한것

def test(**arg): #<- 여러개의 인수를 받을때, 키워드 인수를 받을 때 사용하는 표시
    x, y, z = arg    #3개받아서 각각 저장하고
    return x, y, z   #3개 리턴

print(test(f=3, s=2, r=6)) #<- 3개로 설정해서 무조건 인수가 3개여야함 **은 무조건 딕셔너리 형태로 값을 지정해줘야함





def b(*args):
    x, y, *z = args #z만 몇개들어올지 모르겠다는것    
    return x, y, z

print(b(1, 2, 3, 4, 5)) #3부터는 다 z임


# *과 **의 차이 :       1개는 매개변수가 몇개들어올지 모를때 씀,    
def function(*args):
  print(args)
function('asdf')
function('asdf',123,'asdfdfdsf')
# 결과
#('asdf',)
#('asdf', 123, 'asdfdfdsf')


#2개는  *과 같은기능에 추가로 딕셔너리 형태 매개변수를 받는다는것
def function(**kwargs):
  print(kwargs)
  
function(nn='asdf',aa=123)             
# 결과
#{'nn': 'asdf', 'aa': 123}
# function(123)
# 결과
# TypeError: function() takes 0 positional arguments but 1 was given         **로 만든 함순데 key값을 안줘서



# def test222(**arg): 
    # x, y, z* = arg          **로 선언한 함수에서는 이렇게 못쓰고
    # return x, y, z          고정된 개수의 인수만 사용해야 되는듯  <-x        이렇게 리턴값을 x,y,z  3개로 정했을때만 3개입력하는거지 여러개 지정 못하는게 아님
# print(test222(f=3, s=2,    r=6,q=1,w=1,e=1,d=2 ))   안됨



#둘다사용하려면
def function(*args,**kwargs):
  print(args)
  print(kwargs)

function(123,'asdf',22,424,535,646,464,    aa=1,bb='asdf',c='wer',b='werr')      # 앞쪽부분은 막추가해도 되는*     뒤쪽부분은 딕셔너리 형태로만 지정해야되는**              


# function(aa=1,bb='asdf','ASDF',1234)                순서맞춰야됨 def function(*args,**kwargs):      앞이 *  뒤가 **
# # 결과
# # SyntaxError: positional argument follows keyword argument
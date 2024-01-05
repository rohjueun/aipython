#1.1 split:문자열을 특정 구분자로 나누어 리스트로 반환하는 메소드
data = "John,30,Engineer\nAlice,25,Designer\nBob,22,Artist"
lines=data.split('\n')
print(lines)

for line in lines:
    fields = line.split(',')
    print("Name",fields[0],"Age",fields[1],"Occupation",fields[2])
    
#1.2join: 리스트의 각 요소를 문자열로 변환하고 주어진 구분자로 결합하여 
#하나의 문자열로 반환
words = ['Hello', 'world', 'this', 'is', 'a', 'test']
sentence = ' '.join(words)
print(sentence)

#Lab
#1. split the string
List = 'Geeks for Geeks'
new_List = List.split(" ")
print(new_List)

#2. Join the list of string
List =  ['Geeks', 'for', 'Geeks']
new_List = "-".join(List)
print(new_List)

#2.1 list comprehention 리트스를 생성하는 간결하고 직괁
squares = [x**2 for x in range(5)] 
print(squares)

#1. List Comporehension
List = [1,2,3,4,5]
new_List = [x**2 for x in List]
print(new_List)

#2. List Comprehension
List = ["Seoul", "New York", "London", "Shanghai", "Paris", "Tokyo"]
new_List = [x for x in List if x[0]=='S']
print(new_List)

#3.1 enumerate: 순회가능한 객체(예:리스트)를 인덱스와 함께 반환
fruits = ['apple', 'banana', 'cherry']
for i , fruit in enumerate(fruits):
    print(i,fruit)

#1. Enumerate
List = ['a','b','c']
for i,fruit in enumerate(List):
    print(f'fruit{i} name is {fruit} ')

#2. range를 사용한 코드
List = ['a','b','c']
for i in range(len(List)):
    print(f'fruit{i} name is {List[i]}')

#3.2 zip 
#2개 이상의 순회 가능한 객체를 병렬적으로 순회하면서 각 항목을 튜플로 묶어 반환
names = ['John', 'Jane', 'Doe']
ages = [25, 30, 35]

for name, age in zip(names,ages):
    print(f'{name} is {age} years old')


#1. zip
name = [ "M", "N", "S", "A" ]
roll_no = [ 4, 1, 3, 2 ]
result = set((zip(name,roll_no)))
print(result)

#2. zip & enumerate
names = ['M', 'R', 'C']
ages = [24, 50, 18]
for i ,j in enumerate(zip(names,ages)):
    print(i,j[0],j[1])

#4.1 lambda 
#lambda:익명함수를 정의할 때 사용
double = lambda x: x*2
print(double(5))

#4.2 map
#함수와 순회 가능한 객체를 받아,객체의 각 항목에 함수를 적용한 결과를 반환
numbers = [1,2,3,4]
squared = list(map(lambda x:x*2, numbers))
print(squared)

#1.map & lambda
num1 = [4,5,6]
num2 = [5,6,7]

List =list( map(lambda x,y:x+y,num1,num2))
print(List)

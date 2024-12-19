file = open('mi.txt')
print(file.read())
file.close()

print('------------------')
file = open('mi.txt','r')
print(file.read())
file.close()

print('------------------')
file = open('mi.txt','w')
file.write('I read in class 10')
file.close()

print('------------------')
file = open('mi.txt','a')
file.write('\n I used to read in class 9')
file.close()

file = open('mi.txt','r')
count=0

content=file.read()
lines=content.split('\n')

for i in lines:
    if i:
      count=count+1

print("total=" ,count)

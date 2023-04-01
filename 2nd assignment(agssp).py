def new(numbers):
    total=0
    for num in numbers:
        total+= num**2
    return total
numbers=[1,2,3,4,5,6,7]

d=new(numbers)
print(d)
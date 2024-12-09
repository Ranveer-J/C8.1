my_tuple = ()
print(my_tuple)

my_tuple = (1,2,3)
print(my_tuple)

my_tuple = (1, "hello" , 2, 3)
print(my_tuple)

my_tuple = ("cat" , [1,4,16] , (1,2,3))
print(my_tuple)

my_tuple = ("p","e","r","m","i","t")
print(my_tuple[0])
print(my_tuple[5])

n_tuple = ("turtle", (4,8,22) , ["tom" , "henry"])
print(n_tuple[0][4])
print(n_tuple[0][2])

print("Spliced :", n_tuple[0:8])

for letter in my_tuple:
    print("Hello", letter)


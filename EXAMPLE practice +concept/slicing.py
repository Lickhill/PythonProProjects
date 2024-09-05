arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(arr[2:8])  # this is called slicing
# this cuts the array or even for tuppel from index 2 to 8 and not taking 8

print(arr[4:])  # print from 4th index to ending

print(
    arr[:6]
)  # from index 0 to index 6 and not including 6th index element just like how substring comcept works

print(
    arr[1 : len(arr) : 2]
)  # from index >= 1 till last element with the intercal of 2 live leaving 1 and printing the other

print(arr[::2])  # print all the elememtns with the intercval of 2

print(arr[::-1])  # print the array or tupple in reverse

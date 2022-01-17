def largest(array,l):
  
    max = array[0]
    for i in range(1, l):
        if array[i] > max:
            max = array[i]
    return max
  
# int main()
array = [904, 324, 4500, 90, 900]
l=len(array)
largest= largest(array,l)
print ("Largest element in given array is",largest)
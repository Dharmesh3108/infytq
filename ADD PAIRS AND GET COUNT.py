def find_pairs_of_numbers(num_list,n):
  count=0
  for i in range(len(num_list)):
      for j in range(i+1,len(num_list)):
        if(num_list[i]+num_list[j]==n):
          count=count+1
  print(count)        
  

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))

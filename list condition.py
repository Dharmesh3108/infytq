
list_of_airlines=["AI","EM","BA"]
print("List of airlines:",list_of_airlines)

sample_list=["Mark",5,"Jack",9, "Chan",5]
print("Sample List:",sample_list)

print("Number of elements in the list:",len(sample_list))

print("Element at 2nd index position:", sample_list[2])


sample_list[2]="James"


print("Element at 2nd index position after random write:",sample_list[2])



sample_list.append("James")
print("After adding element to list:",sample_list)


new_list=["Henry","Tim"]
sample_list+=new_list

print("After combining two lists - 1st way:",sample_list)

sample_list=sample_list+new_list
.
print("After combining two lists - 2nd way:",sample_list)

print(sample_list[10])

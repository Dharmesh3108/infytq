def encode(message):
    count=1
    res=''
    for i in range(len(message)-2):
      
      if message[i]==message[i+1]:
        count+=1
      else:
        res+=str(count)+message[i]
        count=1    
    temp=message[-2:]
    if (temp[0]==temp[1]):
        count+=1
        res+=str(count)+temp[0]
    else:
        res+=str(count)+temp[0]
        res+=str(count)+temp[1]
    print(res)    
  

encoded_message=encode("ABBBBCCCCCCCCAB")def encode(message):
    count=1
    res=''
    for i in range(len(message)-2):
      
      if message[i]==message[i+1]:
        count+=1
      else:
        res+=str(count)+message[i]
        count=1    
    temp=message[-2:]
    if (temp[0]==temp[1]):
        count+=1
        res+=str(count)+temp[0]
    else:
        res+=str(count)+temp[0]
        res+=str(count)+temp[1]
    print(res)    
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)


print(encoded_message)


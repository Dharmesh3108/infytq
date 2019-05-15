def find_common_characters(msg1,msg2):
    res=""
    for i in range(len(msg1)):
      for j in range(len(msg2)):
        if((msg1[i]==msg2[j]) and (msg1[i]!=" ")):
          res+=(msg1[i])
        
    
    
    re=[]
    for i in res:
      if i not in re:
        re.append(i)
        
    restr=''
    for i in re:
      restr+=i
    return restr 
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)

# reverse the string
s = "this is string example"
#print(s[::-1])
print(s[:-23 : -1])

#interchange charactor
str="this is my string example"
w=str.split(' ')
print(w[0][0:2][::-1]+w[0][2:4][::-1],w[1][0:2][::-1],w[2][0:2][::-1],w[3][0:5][::-1],w[3][0:7][::-1])


#reverse string without interchanging word
r="this is string example"
s=r.split(' ')
print(s[0][::-1],s[1][::-1],s[2][::-1],s[3][::-1])

# split the string
a="*"
st= "this is string example"
p=st.split(" ")
print(p)
print(a.join(p))

#ste="this is string example"
#print(list(ste))

# replace the word
word = "this is string example"
print(word.replace(" is ", " was "))





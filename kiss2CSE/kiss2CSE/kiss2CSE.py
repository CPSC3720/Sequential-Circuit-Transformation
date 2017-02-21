#Currently what i Think needs to happen is...
# we take a kiss2 file, which is formatted as follows ( i think, please correct me if i am misunderstanding )
# .i i  
# .o o 
# .p p 
# .s s 
# iiii stateQ stateQ+ oooo
# ....
# ....
# .... 
# iiii stateQ stateQ+ oooo

#where 'i' is the size of inputs (that is a input will be i digits long), note that i is the index 4
#where 'o' is the size of outputs (output will be o digits long), note that o is the index 8
#where 'p' is the size of the list of transitions that will be described
#where 's' is the number of states that will be described  ////"This is what i think atleast"////



#Lets try opening a .kiss2 file with python first.
filename = '..\..\MCNC\Sequential\Kiss2\ex1.kiss2' 
fin=open(filename,'r') # 'r' means we are openiong the file for reading versus 'w' for writing

i = fin.readline() #this is some garbage?

i= fin.readline()
val_i =''.join(n for n in i if n.isdigit())
print(val_i)


o = fin.readline()
val_o =''.join(n for n in o if n.isdigit())
print(val_o)

p = fin.readline()
val_p =''.join(n for n in p if n.isdigit())
print(val_p)

s = fin.readline()
val_s =''.join(n for n in s if n.isdigit())
print(val_s)

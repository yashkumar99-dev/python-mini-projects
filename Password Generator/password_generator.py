#import the required function from modules!
from random import sample
from string import ascii_lowercase,ascii_uppercase,digits,punctuation

#input the length of password
N=int(input('\nEnter the length of password: '))                      

#define collection
all = ascii_lowercase + ascii_uppercase + digits + punctuation

#use random 
password = sample (all, N)

#print the password
print("Password: ",*password, sep="")
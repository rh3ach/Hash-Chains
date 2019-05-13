import hashlib;
import passlib.hash;
import sys;
import time
start = time.time()
A=123
print "-----------------------------------------------------"
print "     ZKP implementation for account balance check "
print "-----------------------------------------------------"
print "Hello Alice!"
print "How much will you spend today?"
P = input("Enter amount in BTC: ")
print "-----------------------------------------------------"

seed=b"12345667"

proof = hashlib.md5(seed)
encrypted_bal = hashlib.md5(seed)
x=A-P

for i in range(1,1+x):
	proof = hashlib.md5(proof.digest())

for i in range(1,A+1):
	encrypted_bal = hashlib.md5(encrypted_bal.digest())

verfied_bal=proof

for i in range(0,P):
	verfied_bal = hashlib.md5(verfied_bal.digest())



print "Alice's Balance:\t\t",A
print "Balance to prove:\t\t",P

print "-----------------------------------------------------"


print "Proof:\t\t",proof.hexdigest()
print "Encr Balance:\t",encrypted_bal.hexdigest()
print "Verified Balance:\t",verfied_bal.hexdigest()
print "-----------------------------------------------------"
if (encrypted_bal.hexdigest()==verfied_bal.hexdigest()):
	print "Transaction is valid"
else:
	print "Insufficient funds"
end = time.time()
print "-----------------------------------------------------"
print "Your code took",end - start,"seconds to run"

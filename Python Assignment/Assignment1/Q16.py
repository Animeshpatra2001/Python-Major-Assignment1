'''16. Import relevant Python modules and print the values of e^π and π^e^e. Then, if e^π > π^e, print ”ok”.
Otherwise print ”ok anyway”'''

import math

print(math.e ** math.pi)
print(math.pi ** math.e)

print("OK") if math.e ** math.pi > math.pi ** math.e else print("OK anyway") 

#It will print OK
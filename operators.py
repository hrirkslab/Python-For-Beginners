#Div and modulo operator
a = 5%2 # reminder
b = 15//2 #only diviisible answer
print(a)
print(b)

c = divmod(7,3)
print(c)

print(abs(-6))

#custom absolute value
def abs_custom(val):
    if(val<0):
        return -val
    return val

print(abs_custom(8))

#rounding
print(round(69.420))

#conversion
num1 = int("67")
num2 = float("679.6")
print(num1+num2)

#power
print(num2 ** num1)
print(pow(num2,num1))

compl_num = complex()

pasa_boka = True
gore_boka = True

if pasa_boka | gore_boka: 
    print("Atleast, Ek jana Boka")

if pasa_boka & gore_boka: 
    print("Duitai Boka")


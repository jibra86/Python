####
##Setting up a Program to Compute the Regular Pay and the Over Time Pay of a Worker Using if and elif
####

h = input("Enter hours: ")
r = input("Enter rate per hours: ")

fh = float(h)
fr = float(r)

def computepay(hours, rate):
    if hours > 40:
        regPay = fh * fr
        otp = (fh - 40) * (fr * 0.5)
        pay = regPay + otp
        return pay
    elif hours < 40:
        pay = fh * fr
        return pay

xp = computepay(fh, fr)
print("pay:", xp)

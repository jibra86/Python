hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")

fhours = float(hours)
frate = float(rate)

if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 0.5)
    pay = reg + otp
    print(pay)
elif fhours < 40:
    pay = fhours * frate
    print(pay)

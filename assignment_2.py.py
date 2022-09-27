T = int (input("Enter a temperature: "))
if (T > 0) and (T <= 30):
    print(T, "is a low temperature so alarm switched off.")
elif (T >= 35):
    print(T, "is a high temperature so alarm switched on.")
else:
    print(T, "is a normal temperature")
H =int (input("Enter a humidity:"))
if(H > 0) and (H <= 30):
    print(H, "is a low humidity so alarm switched off.")
elif (H >= 35):
    print(H, "is a high humidity so alarm switched on.")
else:
    print(H, "is a normal humidity")

# dictionaries one of the data structures like list in python where we can strore data 
months = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(months["Feb"])    #if i give wrong name in it , it will shoe error
print(months.get("Mar"))
print(months.get("mar"))    #if i give wring name in it , it won't show error, instead of that it will show none
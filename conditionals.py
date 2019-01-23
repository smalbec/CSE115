#    a and b is true if both a is true and b is true. Otherwise, it is false.
#     a or b is true if either a is true or b is true. Otherwise, it is false.
#
#     if morning and workday:
#         wakeup()
#
#     elif is when you need another conditional inside an if statement



def higher_lower(x):
    if x<24:
        return("higher")
    elif x>24:
        return("lower")
    else:
        return("correct u dumb")


print(higher_lower(24))


def categorize(x):
    if x<20:
        return("low")
    elif x>=20 and x<36:
        return("medium")
    else:
        return("high")

#or the more optimal one

def categorize2(x):
    if x<15:
        return("low")
    elif 15<=x<=24:
        return("medium")
    else:
        return("high")

print(categorize2(60))

def categorizelen(x):
    if len(x)<5:
        return("short")
    elif 5<=len(x)<=14:
        return("medium")
    else:
        return("long")

def compute_xp(x,y):
    if y==False:
        return(92884)
    else:
        return(92884 + x)

def replacement(x):
    x = x.replace("a", "j")
    return(x)

print(replacement("alalala"))
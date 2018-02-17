a = 7
b = 10
c = 8

#if a < b and a < c:
#   print "a is smaller"
#   print "inside if"
#print "outside if"


#if a < b and a < c:
#   print "a is smaller"
#   print "inside if"
#else:
#    print "a is not smaller"
#    print "inside else"
#print "outside if"
"""
if a < b and a< c:
    print "a is smaller"
elif b<c:
    print "b is smaller"
else:
    print "c is smaller"
    """


if a < b:
    print "first condition satisfied"
    if a < c:
        print "second condition satisfied"
        print "a is smaller"
    else:
        print "a is neither greater nor smaller"
else:
    print "a is greater"




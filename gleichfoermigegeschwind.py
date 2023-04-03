
#static velocity(no acceleration) s1 = v * t + s0


#1 Formula

def strecke(v,t,s0):
    
    s1 = (v * t) + s0
    return s1

def time(v,s1,s0):
    t = (s1-s0) / v
    return t

def velocity(s1,t,s0):
    v = (s1 - s0) / t
    return v

print(strecke(100,2,0))
print(time(100,200,0))
print(velocity(200,2,0))


#2  Cars ex: Car A ----><---- Car B

#when do they meet? we need Time
#t = x
#v1 * x = s1
#v2 * x = s2
#distance d = s1 + s2

def whenzusammenstoss(v1,v2,d):
    #v1 * x + v2 * x = d
    #x(v1+v2) = d
    x = d/(v1+v2)
    return x

#where do they meet? we need S

def wherezusammenstoss(v1,v2,d):
    p = d - (v1 * d/(v1+v2))
    p2 = (v1 * d/(v1+v2))
    return p,p2

print(whenzusammenstoss(80, 40, 160))
print(wherezusammenstoss(80, 40, 160))
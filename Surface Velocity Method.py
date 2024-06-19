i=0
a=0
c=0
h=0
wli=[]
hli=[]
al=[]

print('---------------------------------------------------')
print('Measurement of Discharge by Surface Velocity Method')
print('---------------------------------------------------')
n=int(input('Enter the Number of Intervals of Stream:'))
v=float(input('Enter the Surface Velocity of Stream in ft/sec:'))
cf=float(input('Enter the Conversion factor for Surface Velocity:'))
v=v*cf
r=int(input('Enter "1" for Constant Interval or "2" for Varaible Interval of Stream:'))
print()
if r==1:
    w=float(input('Enter the width of Interval in ft:'))
    print()
    while i<=n:
        c=h
        h=float(input('Enter the Depth of Stream at Node {} in ft:'.format(i)))
        i=i+1
        a=a+(h+c)*w/2
        q=a*v
elif r==2:
    while i<n:
        w=float(input('Enter the width of Interval between Node {} and Node {} in ft:'.format(i,i+1)))
        wli.append(w)
        i=i+1
    print()    
    i=0    
    while i<=n:
        h=float(input('Enter the Depth of Stream at Node {} in ft:'.format(i)))
        hli.append(h)
        i=i+1    
    for x in range(0,len(wli)):
        a=(hli[x]+hli[x+1])*wli[x]/2
        al.append(a)
    a=sum(al)
    q=a*v 
else:
    print('Invalid Input')
    print()
    q=0
print('---------------------------------------------------------------------')    
print('Discharge of Stream by Surface velocity Method is',round(q,2),'Cusecs')
print('---------------------------------------------------------------------')

    

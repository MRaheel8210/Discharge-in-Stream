i=0
c=0
h=0
wli=[]
hli=[]
al=[]
vl=[]
vll=[]
ql=[]

print('--------------------------------------------')
print('Measurement of Discharge by 0.6 depth Method')
print('--------------------------------------------')
n=int(input('Enter the Number of Intervals of Stream:'))
print()
while i<=n:
    v=float(input('Enter the 0.6 Depth Velocity at Node {} in ft/sec:'.format(i)))
    vl.append(v)
    i=i+1
i=0
for i in range(0,(len(vl)-1)):
    v=(vl[i]+vl[i+1])/2
    vll.append(v)
print()
r=int(input('Enter "1" for Constant Interval or "2" for Varaible Interval of Stream:'))
print()
i=0
if r==1:
    w=float(input('Enter the width of Interval in ft:'))
    print()
    while i<=n:
        c=h
        h=float(input('Enter the Depth of Stream at Node {} in ft:'.format(i)))
        i=i+1
        a=(h+c)*w/2
        al.append(a)
    i=0    
    for i in range(0,len(al)-1):
        ql.append(vll[i]*al[i+1])
    q=sum(ql)
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
    i=0    
    for i in range(0,len(wli)):
        a=(hli[i]+hli[i+1])*wli[i]/2
        al.append(a)
    i=0    
    for i in range(0,len(al)):
        ql.append(vll[i]*al[i])
    q=sum(ql)
else:
    print('Invalid Input')
    print()
    q=0  
print('-------------------------------------------------------------------')    
print('Discharge of Stream by 0.6 Depth Method is',round(q,2),'Cusecs')
print('-------------------------------------------------------------------')

    

i=0
c=0
h=0
wli=[]
hli=[]
al=[]
vl=[]
vll=[]
vlll=[]
ql=[]
print('----------------------------------------------------')
print('Measurement of Discharge by 0.2 and 0.8 depth Method')
print('----------------------------------------------------')
n=int(input('Enter the Number of Intervals of Stream:'))
print()
while i<=n:
    v=float(input('Enter the 0.2 Depth Velocity at Node {}:'.format(i)))
    vlll.append(v)
    i=i+1
print()
i=0
while i<=n:
    v=float(input('Enter the 0.8 Depth Velocity at Node {}:'.format(i)))
    vll.append(v)
    i=i+1
print()
i=0
for i in range(0,(len(vll)-1)):
    v=(vll[i]+vll[i+1]+vlll[i]+vlll[i+1])/4
    vl.append(v)
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
        ql.append(vl[i]*al[i+1])
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
    print()
    i=0    
    for i in range(0,len(al)):
        ql.append(vl[i]*al[i])
    q=sum(ql)
    print()
else:
    print('Invalid Input')
    print()
    q=0  
print('-----------------------------------------------------------------------')    
print('Discharge of Stream by 0.2 and 0.8 Depth Method is',round(q,2),'Cusecs')
print('-----------------------------------------------------------------------')

    

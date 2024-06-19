i=0
a=0
c=0
h=0
wli=[]
hli=[]
al=[]
vl=[]
vll=[]
vlll=[]
ql=[]

print('-------------------------')
print('Measurement of Discharge')
print('-------------------------')
wh=int(input('Enter "1" surface velocity Method or "2" for 0.6 depth method or "3" for 0.2 & 0.8 depth method:'))
if wh==1:
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

elif wh==2:
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

elif wh==3:
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
    
else:
    print('Invalid Choice')
    

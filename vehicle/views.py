from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        weight=request.POST['weight']
        va=[]
        vb=[]
        vc=[]
        a=250
        b=250
        c=250
        packages= weight.split(',')
        packages=list(map(int, packages))
        for i in range(0,len(packages)):
            if packages[i]>5 and sum(va)+packages[i]<250:
                va.append(packages[i])
            elif packages[i]<50 and sum(vb)+packages[i]<250:
                vb.append(packages[i])
            elif sum(vc)+packages[i]<250:
                vc.append(packages[i])


            if sum(vb)<=100:
                for i in range(0,len(vb)):
                    if vb[i]>5 and sum(va)+vb[i]<250:
                        va.append(vb[i])
                    elif sum(vc)+vb[i]<250:
                        vc.append(vb[i])

            if sum(vb)<=100:
                vb=[]
            
            print("Vehicle A:",va)
            print("Vehicle B:",vb)
            print("Vehicle C:",vc)
        return render(request,"index.html",{"vehicleA":va,"vehicleB":vb,"vehicleC":vc})
    else:
        return render(request,"index.html")


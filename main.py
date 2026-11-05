box(texture = "https://i.postimg.cc/nLqyvRt6/geulim3.png&quot;, size = vec(100,100,0.1))
box(size = vec(100,10,10), texture = "https://i.postimg.cc/kgmz7NS0/geulim4.jpg&quot;, pos=vec(0,-44,4))
sphere( pos=vec(0,-41,10), texture = "https://i.postimg.cc/NFC79cCt/geulim2.jpg&quot;)
trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1)
top = cylinder(size = vec(0.1,1,1),pos = vec(0,0.5,0), axis = vec(0,1,0))

cup = compound([oddring,top])

color=[]

while True : 
    rate(100)
    k = keysdown()
    if ' ' in k : 
        for i in color :
            cup.color= vec(i/255,0,0)

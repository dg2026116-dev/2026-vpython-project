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


 trishape = shapes.triangle(xscale=1.4, yscale=5)
circpath = paths.circle(scale=5)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(1,0,5))
top = cylinder(size = vec(0.7,5,5),pos = vec(1,1.5,5), axis = vec(0,1,0))

trishape = shapes.triangle(xscale=1.4, yscale=5)
circpath = paths.circle(scale=5)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(21,0,5))
top = cylinder(size = vec(0.7,5,5),pos = vec(21,1.5,5), axis = vec(0,1,0))

trishape = shapes.triangle(xscale=1.4, yscale=5)
circpath = paths.circle(scale=5)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(-20,0,5))
top = cylinder(size = vec(0.7,5,5),pos = vec(-20,1.5,5), axis = vec(0,1,0))




box(texture = "https://i.postimg.cc/nLqyvRt6/geulim3.png&quot;, size = vec(50,50,10),pos=vec()
box(size = vec(50,1.8,14), texture = "https://i.postimg.cc/kgmz7NS0/geulim4.jpg&quot;, pos=vec(0,-10,5))
sphere( pos=vec(0,-41,20), texture = "https://i.postimg.cc/NFC79cCt/geulim2.jpg&quot; )




trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(5,0,0))
top = cylinder(size = vec(0.1,1,1),pos = vec(5,0.4,0), axis = vec(0,1,0))

trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(0,0,0))
top = cylinder(size = vec(0.1,1,1),pos = vec(0,0.4,0), axis = vec(0,1,0))

trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(-5,0,0))
top = cylinder(size = vec(0.1,1,1),pos = vec(-5,0.4,0), axis = vec(0,1,0))
colors = [color.red, color.blue, color.green]

colors = [color.red, color.blue, color.green]
cnt = 0
while True : 
    rate(100)
    k = keysdown()
    if ' ' in k:
        sleep(0.095)
        for c in trishape :
            trishape.color = colors[cnt%3]
        for c in circpath :
            circpath.color = colors[cnt%3]       
        for c in oddring :
            oddring.color = colors[cnt%3]        
        for c in top :
            top.color = colors[cnt%3]
        cnt +=1


trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1,pos = vec(5,0,0))
top = cylinder(size = vec(0.1,1,1),pos = vec(5,0.4,0), axis = vec(0,1,0))

cup1 = compound([oddring,top])



trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1)
top = cylinder(size = vec(0.1,1,1),pos = vec(0,0.5,0), axis = vec(0,1,0))

cup2 = compound([oddring,top])


trishape = shapes.triangle(xscale=0.2, yscale=1)
circpath = paths.circle(scale=1)
oddring = extrusion(shape=trishape, path=circpath,opacity = 1, pos = vec(-5,0,0))
top = cylinder(size = vec(0.1,1,1),pos = vec(-5,0.4,0), axis = vec(0,1,0))

cup3 = compound([oddring,top])

cups = [cup1, cup2, cup3]
colors = [color.red, color.yellow]
cnt = 0
while True : 
    rate(10)
    for c in cups : 
        rate(10)
        cnt += 1
        c.color = colors[cnt%2]
        

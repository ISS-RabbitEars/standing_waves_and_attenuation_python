import math
import matplotlib.pyplot as plt
from matplotlib import animation

fig, a=plt.subplots()

N=1000
s=2*math.pi
x=[]
y=[]
frps=30
sec=10
sec2=5
f=frps*sec
f2=frps*sec2
dt=2*s/f

def setplot(sx,sy):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-sx,sx])
	plt.ylim([-sy,sy])
	ax.set_facecolor('xkcd:black')

for i in range(N):
	x.append(-s+i*2*s/N)
	y.append(math.sin(x[i]))

def run(frame):
	if (frame<=f2):
		plt.clf()
		plt.plot(x,y,color='r')
		plt.title(r'Sine Wave:' '\n' r'$f(x)=\sin(x)$')
		setplot(s,2)
	if (frame>f2 and frame<=f+f2):
		plt.clf()
		for i in range(N):
			y[i]=math.sin(x[i]-(frame-f2)*dt)
		plt.plot(x,y,color='r')
		plt.title(r'Traveling Sine Wave:' '\n' r' $f(x,t)=\sin(x-t)$')
		setplot(s,2)
	if (frame>f+f2 and frame<=2*f+f2):
		plt.clf()
		for i in range(N):
			y[i]=math.sin(x[i]-(frame-(f+f2))*dt)+math.sin(x[i]+(frame-(f+f2))*dt)
		plt.plot(x,y,color='r')
		plt.title(r'Standing Wave:' '\n' r'$f(x,t)=\sin(x-t)+\sin(x+t)$')
		setplot(s,3)
	if (frame>2*f+f2 and frame<=3*f+f2):
		plt.clf()
		for i in range(N):
			y[i]=math.exp(-x[i]**2)*(math.sin(x[i]-(frame-(2*f+f2))*dt)+math.sin(x[i]+(frame-(2*f+f2))*dt))
		plt.plot(x,y,color='r')
		plt.title(r'Spatially Attenuated Standing Wave:' '\n' r'$f(x,t)=e^{-x^2}\left[\sin(x-t)+\sin(x+t)\right]$')
		setplot(s,2)		
	if (frame>3*f+f2 and frame<=4*f):
		plt.clf()
		for i in range(N):
			y[i]=math.exp(-(x[i]**2)-(frame-(3*f+f2))*dt)*(math.sin(x[i]-(frame-(3*f+f2))*dt)+math.sin(x[i]+(frame-(3*f+f2))*dt))
		plt.plot(x,y,color='r')
		plt.title(r'Spatially and Temporally Attenuated Standing Wave:' '\n' r'$f(x,t)=e^{-x^{2}-t}\left[\sin(x-t)+\sin(x+t)\right]$')
		setplot(s,2)

ani=animation.FuncAnimation(fig,run,interval=1,frames=4*f)
writervideo = animation.FFMpegWriter(fps=frps)
ani.save('waves.mp4', writer=writervideo)
plt.show()

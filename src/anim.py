import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import writers

plt.close('all')

plt.style.use("seaborn")

fig = plt.figure(figsize=[16/1.3,9/1.3])

axCercleUni = plt.subplot2grid((3,3), (2,2))
axCos = plt.subplot2grid((3,3), (0,2), rowspan = 2)
axSin = plt.subplot2grid((3,3), (2,0), colspan = 2)

theta = np.linspace(0,2*np.pi,500)

axCercleUni.plot(np.cos(theta), np.sin(theta))
axCercleUni.axis("equal")
axCercleUni.set_xlim([-2,2])

barre, = axCercleUni.plot([0,1], [0,0])

ligneCos, = axCos.plot(np.cos(theta), theta)
axCos.set_xlim([-2,2])
axCos.set_ylim([0,2*np.pi])

ligneSin, = axSin.plot(theta, np.sin(theta))
axSin.set_xlim([0,2*np.pi])

def animate(iter):
    barre.set_data([0,np.cos(theta[iter])], [0,np.sin(theta[iter])])
    ligneCos.set_data(np.cos(theta[:iter]), theta[:iter])
    ligneSin.set_data(theta[:iter], np.sin(theta[:iter]))
    return [barre, ligneCos, ligneSin]

ani = FuncAnimation(
    fig,
    animate,
    frames=500,
    blit=True,
    interval=1000/60,
    repeat=True)

## Uniquement si vous avez installer ffmpeg
# Writer = writers['ffmpeg']
# writer = Writer(
#     fps=24,
#     metadata=dict(artist="Thibaut Kovaltchouk", title = "TutoAnimationPlt"),
#     bitrate=8000)
#
# ani.save("TutoAnimationPlt.mp4", writer=writer)

plt.show()
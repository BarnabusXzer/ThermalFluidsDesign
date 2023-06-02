import numpy as np
import matplotlib.pyplot as plt

tmw060_headloss = [23,21.5,20,19,17.75,16.25,15,13.5,12.25,11,9.25,8,6.5,5,3.25,1.75,0]
tmw120_headloss = [33.5,32.25,31,29.5,28,26.25,24.5,23,21,19,17,15,12.75,10.25,8,5.75,3.25,0.5]

def plot_pump_curve(pump_head_loss:list[int],plot_color:str):
    # FIND EQUATION FOR PUMP CURVE
    flow_rates = np.linspace(0, (len(pump_head_loss)-1)*2, len(pump_head_loss))
    pump_curve = np.poly1d(np.polyfit(x=flow_rates,y=pump_head_loss,deg=2))

    # PLOT PUMP CURVE
    plt.plot(flow_rates,pump_curve(flow_rates),color=plot_color)
    # PLOT MANUFACTURE DATA
    plt.scatter(flow_rates,pump_head_loss,color=plot_color)

plot_pump_curve(tmw060_headloss,'blue')
plot_pump_curve(tmw120_headloss,'orange')

# MAKE THE PLOT LOOK NICE
plt.title("Pump Model vs Manufacture Data")
plt.legend(['TACO-0014','TACO-0014 Manufacture Data','TACO-0013','TACO-0013 Manufacture Data'])
plt.xlabel("Flow Rate - GPM")
plt.ylabel("Head Loss - feet")
plt.margins(x=0,y=0)
plt.grid(which="major")
plt.yticks(ticks=
np.linspace(0,36,19))
plt.xticks(ticks=np.linspace(0,34,18))
# SAVE FIGURE
plt.savefig("pump_curve.png")
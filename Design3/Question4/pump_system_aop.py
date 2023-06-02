import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

taco0014_headloss = [23,21.5,20,19,17.75,16.25,15,13.5,12.25,11,9.25,8,6.5,5,3.25,1.75,0]
taco0013_headloss = [33.5,32.25,31,29.5,28,26.25,24.5,23,21,19,17,15,12.75,10.25,8,5.75,3.25,0.5]

for i in range(len(taco0014_headloss)):
    taco0014_headloss

def plot_pump_curve(pump_head_loss:list[int],plot_color:str):
    # FIND EQUATION FOR PUMP CURVE
    flow_rates = np.linspace(0, (len(pump_head_loss)-1)*2, len(pump_head_loss))
    pump_curve = np.poly1d(np.polyfit(x=flow_rates,y=pump_head_loss,deg=2))

    # PLOT PUMP CURVE
    plt.plot(flow_rates,pump_curve(flow_rates),color=plot_color,zorder=3)

def plot_system_curve(pump_head_loss:list[int],total_head_loss:int,flow_rate:int,plot_color:str):
    # DETERMINE K VALUE FOR SYSTEM CURVE
    k = total_head_loss / (flow_rate**2)
    flow_rates = np.linspace(0, (len(pump_head_loss)-1)*2, len(pump_head_loss))

    # FIND EQUATION FOR SYSTEM CURVE
    system_head_loss = []
    for i in range(len(pump_head_loss)):
        head = k*(flow_rates[i]**2)
        system_head_loss.append(head)
    system_curve = np.poly1d(np.polyfit(x=flow_rates,y=system_head_loss,deg=2))
    # PLOT SYSTEM CURVE
    plt.plot(flow_rates,system_curve(flow_rates),color=plot_color,zorder=4)

def plot_aop(pump_head_loss:list[int],total_head_loss:int,flow_rate:int,plot_color:str='k'):
    # DETERMINE K VALUE FOR SYSTEM CURVE
    k = total_head_loss / (flow_rate**2)
    flow_rates = np.linspace(0, (len(pump_head_loss)-1)*2, len(pump_head_loss))

    # FIND EQUATION FOR SYSTEM CURVE
    system_head_loss = []
    for i in range(len(pump_head_loss)):
        head = k*(flow_rates[i]**2)
        system_head_loss.append(head)
    system_curve = np.poly1d(np.polyfit(x=flow_rates,y=system_head_loss,deg=2))
    
    # FIND EQUATION FOR PUMP CURVE
    pump_curve = np.poly1d(np.polyfit(x=flow_rates,y=pump_head_loss,deg=2))

    # FIND INTERSECTION OF PUMP AND SYSTEM TO FIND AOP
    def find_intersection(func1,func2,x0:int=0):
        return fsolve(lambda x: func1(x)-func2(x),x0)
    x_intersect = find_intersection(system_curve,pump_curve)

    # PLOT AOP
    plt.scatter(x_intersect,system_curve(x_intersect),color=plot_color,zorder=10)

def main():

    # PLOT ALL PUMP, SYSTEM, AND AOP POINTS
    plot_system_curve(taco0014_headloss,29.41353581,9,'r')
    plot_pump_curve(taco0014_headloss,'b')
    plot_aop(taco0014_headloss,29.41353581,9,)
    for i in range(len(taco0014_headloss)):
        taco0014_headloss[i] = taco0014_headloss[i] * 2
    plot_pump_curve(taco0014_headloss,'g')
    plot_aop(taco0014_headloss,29.41353581,9)

    plot_system_curve(taco0013_headloss,29.52601516,18,'y')
    plot_pump_curve(taco0013_headloss,'c')
    plot_aop(taco0013_headloss,29.52601516,18)
    for i in range(len(taco0013_headloss)):
        taco0013_headloss[i] = taco0013_headloss[i] * 2
    plot_pump_curve(taco0013_headloss,'m')
    plot_aop(taco0013_headloss,29.52601516,18)

    # PLOT DESIGN POINTS
    plt.scatter(9,29.41353581,zorder=10,color='b')
    plt.scatter(18,29.52601516,zorder=10,color='g')

    # MAKE THE PLOT LOOK NICE
    plt.title("Pump Analysis")
    plt.legend(['TACO-0014 System Curve','Single TACO-0014','_aop','Two TACO-0014 in Series','_aop','TACO-0013 System Curve','Single TACO-0013','_aop','Two TACO-0013 in Series','_aop','TACO-0013 Design Point','TACO-0014 Design Point'])
    plt.xlabel("Flow Rate - GPM")
    plt.ylabel("Head Loss - feet")
    plt.margins(x=0,y=0)
    plt.grid(which="major")
    plt.yticks(ticks=np.linspace(0,68,18))
    plt.ylim(0,68)
    plt.xticks(ticks=np.linspace(0,36,19))
    # SAVE FIGURE
    plt.savefig("pump_analysis.png")

main()
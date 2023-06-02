import matplotlib.pyplot as plt
import numpy as np

def calc_heat_exchanger_head_loss(flow_rate:int,correction_factor:int=1):
    head_loss = (0.0066*(flow_rate**2)-0.12*flow_rate+5.6053) * correction_factor
    return head_loss

pump_head_loss = [31.5,30.8,30,29,28.5,27.5,26.8,25.8,25,24,23,22,21,20.1,19,18.1,17,16.1,15,14,12.9,11.9,10.8,9.5,8.4,7.2,6,5,3.8,2,0.8,0]

def plot_system_and_pump_curve(pump_head_loss:list[int],total_head_loss:int,flow_rate:int):

    # FIND EQUATION FOR PUMP CURVE
    flow_rates = np.linspace(0,len(pump_head_loss)-1,len(pump_head_loss))
    pump_curve = np.poly1d(np.polyfit(x=flow_rates,y=pump_head_loss,deg=3))

    # CALCULATE THE K VALUE FO RTHE SYSTEM CURVE
    k = total_head_loss/(flow_rate**2)

    # CALCULATE HEADLOSS FOR AND EQUATION FOR SYSTEM CURVE
    system_head_loss = []
    for i in range(len(pump_head_loss)):
        aop = k*(flow_rates[i]**2)
        system_head_loss.append(aop)
    
    # PLOT PUMP CURVE
    plt.plot(flow_rates,pump_curve(flow_rates))
    # PLOT SYSTEM CURVE
    plt.plot(flow_rates,system_head_loss)
    # PLOT AOP FOR 18-GPM
    plt.scatter(x=flow_rate,y=total_head_loss,color="orange")

    # MAKE THE PLOT LOOK NICE
    plt.title("Pump and System Curve")    
    plt.legend(['Pump','System'])
    plt.xlabel("Flow Rate - GPM")
    plt.ylabel("Head Loss - feet")
    plt.margins(x=0,y=0)
    plt.grid(which="major")
    plt.yticks(ticks=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42])
    plt.xticks(ticks=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32])

    # SAVE FIGURE    
    plt.savefig("pump_curve.png")

calc_heat_exchanger_head_loss(18,1.21)
plot_system_and_pump_curve(pump_head_loss=pump_head_loss,total_head_loss=14.1961,flow_rate=18)
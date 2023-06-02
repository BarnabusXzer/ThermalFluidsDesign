import matplotlib.pyplot as plt
from numpy import linspace, poly1d, polyfit
from scipy.optimize import fsolve

def calc_pump_curve(head_loss:list[float],flow_rates:list[float]):
    # FIND EQUATION FOR PUMP CURVE
    pump_curve = poly1d(polyfit(x=flow_rates,y=head_loss,deg=2))
    return pump_curve

def calc_system_curve(flow_rates:list[float],total_head_loss:float,flow_rate:float):

    # FIND EQUATION FOR SYSTEM CURVE
    k = total_head_loss / (flow_rate**2)
    system_head_loss = []
    for i in range(len(flow_rates)):
        head = k*((flow_rates[i])**2)
        system_head_loss.append(head)
    system_curve = poly1d(polyfit(x=flow_rates,y=system_head_loss,deg=2))
    return system_curve 

def calc_aop(pump_curve,system_curve):
    # FIND INTERSECTION OF PUMP AND SYSTEM TO FIND AOP
    def find_intersection(func1,func2,x0:int=0):
        return fsolve(lambda x: func1(x)-func2(x),x0)
    x_intersect = find_intersection(pump_curve,system_curve)
    return x_intersect

def plot(head_loss:list[float],pump_curve,system_curve,aop:float,design_point:tuple=(0,0),title:str='',file:str='simulation.png'):
    plt.plot(head_loss,system_curve(head_loss),zorder=4,color='b') # PLOT SYSTEM CURVE
    plt.plot(head_loss,pump_curve(head_loss),zorder=3,color='g') # PLOT PUMP CURVE
    plt.scatter(aop,system_curve(aop),zorder=5,color='r') # PLOT AOP
    plt.scatter(design_point[0],design_point[1],zorder=5,color='k')# PLOT DESIGN POINT

    # MAKE THE PLOT LOOK NICE
    plt.title(title)
    plt.legend(['System Curve','Pump Curve','Actual Opperating Point','Design Point'],loc="upper right")
    plt.xlabel('Flow Rate - GPM')
    plt.ylabel('Headloss - ft')
    plt.margins(x=0,y=0)
    plt.grid(which="major")
    x_intercept = 0
    plt.ylim(bottom=0,top=pump_curve(0)+4)
    while pump_curve(x_intercept) > 0:
        x_intercept = x_intercept +  1
    plt.xlim(left=0,right=x_intercept+4)

    # SAVE FIGURE
    plt.savefig(file)

def plot_simulation(head_loss:list[float],design_point,title:str='',file:str='simulation.png'):
    flow_rates = linspace(0, (len(head_loss)-1)*2, len(head_loss))
    pump_curve = calc_pump_curve(head_loss,flow_rates)
    system_curve = calc_system_curve(flow_rates,design_point[1],design_point[0])
    aop = calc_aop(pump_curve,system_curve)
    plot(head_loss,pump_curve,system_curve,aop,design_point,title,file)
    plt.clf()
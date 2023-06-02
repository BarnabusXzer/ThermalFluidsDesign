import numpy as np
import matplotlib.pyplot as plt

# MANUFACTURE DATA AT 80F
manufacture_flow_rates=[15,22,30]
manufacture_headloss=[2.5,7.15,13.4]
flow_rates = np.linspace(start=14,stop=32,num=29)

# ESTIMATED/CALCULATED K VALUE
k = 80.445720612
estimated_curve_headloss = []

for i in flow_rates:
    y = k*((i*0.133681/0.020)**2/(2*(32.2*3600)))
    estimated_curve_headloss.append(y)

# PLOT THE DATA
plt.plot(flow_rates,estimated_curve_headloss)
plt.scatter(x=manufacture_flow_rates,y=manufacture_headloss,color="orange")

# MAKE THE PLOTS LOOK NICE
plt.title("Estimated Curve vs Manufacture Data")
plt.legend(['Estimated - TMW120',"Manufacture"])
plt.xlabel("Flow Rate - GPM")
plt.ylabel("Head Loss - feet")
plt.margins(x=0,y=0)
plt.grid(which="major")
plt.yticks(ticks=[0,2,4,6,8,10,12,14,16])
plt.xticks(ticks=[14,16,18,20,22,24,26,28,30,32])

plt.savefig("TMW120 Estimated Curve vs Manufacture Data.png")


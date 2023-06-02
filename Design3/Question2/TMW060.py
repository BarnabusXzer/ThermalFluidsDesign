import numpy as np
import matplotlib.pyplot as plt

# MANUFACTURE DATA AT 80F
manufacture_flow_rates=[7.5,11.25,15]
manufacture_headloss=[2.3,6.5,12.2]
flow_rates = np.linspace(start=6,stop=16,num=11)

# ESTIMATED/CALCULATED K VALUE
k = 293.737585354
estimated_curve_headloss = []

for i in flow_rates:
    y = k*((i*0.133681/0.020)**2/(2*(32.2*3600)))
    estimated_curve_headloss.append(y)

# PLOT THE DATA
plt.plot(flow_rates,estimated_curve_headloss)
plt.scatter(x=manufacture_flow_rates,y=manufacture_headloss,color="orange")

# MAKE THE PLOTS LOOK NICE
plt.title("Estimated Curve vs Manufacture Data")
plt.legend(['Estimated - TMW060',"Manufacture"])
plt.xlabel("Flow Rate - GPM")
plt.ylabel("Head Loss - feet")
plt.margins(x=0,y=0)
plt.grid(which="major")
plt.yticks(ticks=[0,2,4,6,8,10,12,14,16,18,20])
plt.xticks(ticks=[6,8,10,12,14,16])

plt.savefig("TMW060 Estimated Curve vs Manufacture Data.png")

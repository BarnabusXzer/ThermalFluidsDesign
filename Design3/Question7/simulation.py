import numpy as np
from simulation_pump_curve import plot_simulation

def calc_headloss(diameter:float,flow_rate:float,length:float,heat_pump:bool=False,heat_pump_loss:float=0,heat_exchanger:bool=False,etc_loss:float=0,elbows:int=0,tstraight:int=0,tbranch:int=0):

    k_tstraight = 0.34
    k_tbranch = 1.01
    k_elbow = 0.50
    g = 32.2*3600 # ft/min^2

    # FUNCTION TO CALCULATE MAJOR LOSS USING PIPE DIAMETER, FLOW RATE, LENGTH OF PIPE, AND VELOCITY OF FLUID
    def calc_major_loss(diameter:float,flow_rate:float,length:float,velocity:float):
        
        # FUNCTION TO FIND REYNOLDS NUMBER FOR 15% PROPYLENE-GLYCOL (Kinematic-Viscosity = 0.1365/60)
        def calc_reynolds_number(diameter:float,velocity:float):
            reynolds_number = velocity * diameter / (0.1365/60)
            return reynolds_number
        
        # FUNCTION TO FIND FRICTION FACTOR FOR 2" SDR11 PIPING
        def calc_friction_factor(diameter:float,velocity:float):
            relative_roughness = ((np.pi/4)*diameter**2) * 0.00328084
            reynolds_number = calc_reynolds_number(diameter,velocity)
            friction_factor = 0.25/(np.log((relative_roughness/(3.7*diameter))+(5.74/(reynolds_number**2)))**2)
            return friction_factor
        
        friction_factor = calc_friction_factor(diameter,velocity)
        headloss = friction_factor * (length/diameter) * (velocity**2 / (2*g))
        return headloss

    def calc_minor_loss(velocity:float,elbows:int,tstraight:int,tbranch:int):
        h1 = elbows * k_elbow * velocity**2 / (2*g)
        h2 = tstraight * k_tstraight * velocity**2 / (2*g)
        h3 = tbranch * k_tbranch * velocity**2 / (2*g)
        headloss = h1 + h2 + h3
        return headloss
    
    def calc_heat_exchanger_loss(flow_rate):
        headloss = 0.0066*flow_rate**2 - 0.12*flow_rate + 5.6053
        return headloss

    velocity = (flow_rate*0.133681)/((np.pi/4)*(diameter**2))
    major_loss = calc_major_loss(diameter,flow_rate,length,velocity)
    minor_loss = calc_minor_loss(velocity,elbows,tstraight,tbranch)

    if heat_exchanger == True and heat_pump ==True:
        equipment_loss = calc_heat_exchanger_loss(flow_rate) + heat_pump_loss
    elif heat_exchanger == False and heat_pump == True:
         equipment_loss = heat_pump_loss
    elif heat_exchanger == True and heat_pump == False:
         equipment_loss = calc_heat_exchanger_loss(flow_rate)

    headloss = major_loss + minor_loss + equipment_loss + etc_loss
    return headloss

def calc_simulation_headloss(situation:int=0):
    diameter = 0.1598
    tmw120_loss = 5.02272 # FOUND ON SUBMITAL SHEETS
    tmw060_loss = 4.58496 # FOUND ON SUBMITAL SHEETS

    if situation == 0: # SITUATION 0 INDICATES BOTH HEAT PUMPS IN OPERATION
        etc_loss2 = 1.3938638 # ETC HEADLOSS IS THE HEADLOSS FROM THE CHECK VALVE AND REDUCERS
        etc_loss3 = 1.971228839 # ETC HEADLOSS IS THE HEADLOSS FROM THE CHECK VALVE, EXPANDERS, AND REDUCERS
        h1 = calc_headloss(diameter,27,410.13,False,0,True,0,9,1,1) # H1 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 27 GPM
        h2 = calc_headloss(diameter,18,12,True,tmw120_loss,False,etc_loss2,9,0,1) # H2 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 18 GPM
        h3 = calc_headloss(diameter,9,31.44,True,tmw060_loss,False,etc_loss3,17,1,0) # H3 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 9 GPM
        headloss = (h1 + h2 + h3) * 1.15 # TOTAL HEADLOSS WITH A 15% FACTOR OF SAFETY
        return headloss
    elif situation == 1: # SITUATION 1 INDICATES ONLY THE TMW060 HEAT PUMPS IS IN OPERATION
        etc_loss2 = 1.3938638 # ETC HEADLOSS IS THE HEADLOSS FROM THE CHECK VALVE, EXPANDERS, AND REDUCERS
        h1 = calc_headloss(diameter,9,410.13,False,0,True,0,9,1,1) # H1 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 27 GPM
        h2 = calc_headloss(diameter,9,31.44,True,tmw060_loss,False,etc_loss2,17,1,0) # H3 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 9 GPM
        headloss = (h1 + h2) * 1.15 # TOTAL HEADLOSS WITH A 15% FACTOR OF SAFETY
        return headloss
    elif situation == 2: # SITUATION 2 INDICATES ONLY THE TMW120 HEAT PUMPS IS IN OPERATION
        etc_loss2 = 1.971228839 # ETC HEADLOSS IS THE HEADLOSS FROM THE CHECK VALVE, EXPANDERS, AND REDUCERS
        h1 = calc_headloss(diameter,18,410.13,False,0,True,0,9,1,1) # H1 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 27 GPM
        h2 = calc_headloss(diameter,18,12,True,tmw120_loss,False,etc_loss2,9,0,1) # H2 IS THE HEADLOSS FROM ALL PIPING/EQUIPMENT THAT OPPERATES AT 18 GPM
        headloss = (h1 + h2 ) * 1.15 # TOTAL HEADLOSS WITH A 15% FACTOR OF SAFETY
        return headloss
    else:
        print('no')

def main():
    situation0_headloss = (calc_simulation_headloss(0)) # HEADLOSS FOR SITUATION 0 RETURNED 25.93365260965075 ft
    situation1_headloss = (calc_simulation_headloss(1)) # HEADLOSS FOR SITUATION 1 RETURNED 13.105649389716984 ft
    situation2_headloss = (calc_simulation_headloss(2)) # HEADLOSS FOR SITUATION 2 RETURNED 15.844505127782224 ft

    head_loss_TACO0014 = [23,21.5,20,19,17.75,16.25,15,13.5,12.25,11,9.25,8,6.5,5,3.25,1.75,0]
    for i in range(len(head_loss_TACO0014)):
        head_loss_TACO0014[i] = head_loss_TACO0014[i] * 2
    head_loss_TACO0013 = [33.5,32.25,31,29.5,28,26.25,24.5,23,21,19,17,15,12.75,10.25,8,5.75,3.25,0.5]
    for i in range(len(head_loss_TACO0013)):
        head_loss_TACO0013[i] = head_loss_TACO0013[i] * 2
    plot_simulation(head_loss_TACO0014,(situation1_headloss,9),'Pump Analysis for only TMW060 Opperating','TMW060 Only Pump Curve.png')
    plot_simulation(head_loss_TACO0013,(situation2_headloss,18),'Pump Analysis for only TMW120 Opperating','TMW120 Only Pump Curve.png')

main()


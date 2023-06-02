# Pumping and Piping Design Project

## 1. Executive Summary

This report will outline the design of the source side pumping system for a golf course cooling system. It was overdesigned to ensure proper operation after repairs will operate adequately.

The following sections will detail how headloss is found for the heat pumps and the error corrlated with those calculation, The pumping system design, how the headloss was calculated and how the pumps were selcted, comparing the calculated pump curve to the manufacture data, a system P&ID and headloss summary, a method to automate headloss calculations, and operating power consumption.    

## 2. Calculate and Analyze Heat Pump Headloss

Question 2 requires the designer to determine the headloss of the Climate Master Tranquility TMW060 and TMW120 heat pumps, and then calculate the K values for each heat pump. The first step to finding the headloss of a heat pump is calculating the refrigerant correction factor. For this paper, the heat pumps operate with 15% Propylene-Glycol by weight and have an average entering fluid temperature of 80F. Using this information and the data provided in Fig.1 it is possible to find the proper correction factor.  
The next step is calculating the headloss at the designs specified flow and temperature using the manufacture data. Given the manfufacture data for the Climate Master TMW Tranquility series the designer need interpolate the data once to find the headloss at the correct flowrate, then they needed to interpolate again to find the headloss at the correct temperature. Lastly, the calculated headloss must be multiplied by the refrigerant correction factor that was found above.  
The problem statement also required the designer to find the K value associated with each heat pump. The K value is proportional to the headloss multiplied by two time the acceleration due to gravity and divided by the velocity of the fluid squared.  
All of the calculations described above are shown below. The calculations for the TMW060 Fig.2, Fig.3, and Fig.4. The calculations for the TMW060 Fig.5, Fig.6, and Fig.7.
Lastly, it is important for designers to analyze the accuracy of their models. Using the K value calculated the designer developed a model for a headloss as a function of flowrate and compared the results to the values given in the manufactures data. Using a python script the comparisons were plotted and can be observed in Fig.8 and Fig.9 for the TMW060 and TMW120 respectively.  
An accurate K value is important because for each percent error from the manufacture value, directly correlates to error for teh heat pump headloss. 

<figure><center><img src='Question2\Refrigerant Correction Values.jpg'alt='Refrigerant Correction Values'align='center'></center>
<figcaption align='center'><b>Fig.1 - Refrigerant Correction Values</b></figcaption></figure>

<figure><center><img src='Question2\TWM060 Manufacture Data.jpg'alt='TWM060 Manufacture Data'align='center'></center>
<figcaption align='center'><b>Fig.2 - TWM060 Manufacture Data</b></figcaption></figure>

<figure><center><img src='Question2\Calculate Headloss of TMW060.jpg'alt='Calculate Headloss of TMW060'align='center'></center>
<figcaption align='center'><b>Fig.3 - Calculate Headloss of TMW060</b></figcaption></figure>

<figure><center><img src='Question2\Calculate K Value for TMW060.jpg'alt='Calculate K Value for TMW060'align='center'></center>
<figcaption align='center'><b>Fig.4 - Calculate K Value for TMW060</b></figcaption></figure>

<figure><center><img src='Question2\TWM120 Manufacture Data.jpg'alt='TWM120 Manufacture Data'align='center'></center>
<figcaption align='center'><b>Fig.5 - TWM120 Manufacture Data</b></figcaption></figure>

<figure><center><img src='Question2\Calculate Headloss of TMW120.jpg'alt='Calculate Headloss of TMW120'align='center'></center>
<figcaption align='center'><b>Fig.6 - Calculate Headloss of TMW120</b></figcaption></figure>

<figure><center><img src='Question2\Calculate K Value for TMW120.jpg'alt='Calculate K Value for TMW120'align='center'></center>
<figcaption align='center'><b>Fig.7 - Calculate K Value for TMW120</b></figcaption></figure>

<figure><center><img src='Question2\TMW060 Estimated Curve vs Manufacture Data.png'alt='TMW060 Estimated Curve vs Manufacture Data'align='center'></center>
<figcaption align='center'><b>Fig.8 - TMW060 Estimated Curve vs Manufacture Data</b></figcaption></figure>

<figure><center><img src='Question2\TMW120 Estimated Curve vs Manufacture Data.png'alt='TMW120 Estimated Curve vs Manufacture Data'align='center'></center>
<figcaption align='center'><b>Fig.9 - TMW120 Estimated Curve vs Manufacture Data</b></figcaption></figure>

## 3. System Design

The designer was tasked to design a piping system. Given the location and manufacturer data for the two heat pumps the design in Fig.10 was developed.  

<figure><center><img src='Question3\Piping Design.jpg'alt='Piping Design'align='center'></center>
<figcaption align='center'><b>Fig.10 - Piping Design</b></figcaption></figure>

## 4. Calculate System Headloss and Pump Selection

Question 4 asked the designed to size and choose a pump/pumps that would be suitable for the system. In order to size a pump, the headloss of the system and loop must be determined. The approach used in this report to calculate the headloss was to find the headloss of the straight piping (majorloss), then calculate the headloss of the fittings (minorloss), find calculate the headloss of the check valves, reducers, and expanders in the system, and then find the headloss of all equipment in the system.  

**Calculate Straight Piping Headloss**

To calculate the majorloss the fluid velocity, pipe length, pipe diameter, and acceleration due to gravity. Given dimensions of the piping the Fig.11 and the fluid properties, it is possible to calculate all of these values. First the friction factor must be found. Using the method demonstrated in Fig.12. After determining the friction factor all the needed parameters have been found and the corresponding headloss was calculated. This method must be used to solve headloss at each flow rate individually. The calculation for the system’s total major loss can be found in Fig.11 through Fig.18.  

<figure><center><img src='Question4\SDR11 Pipe Dimensions.jpg'alt='SDR11 Pipe Dimensions'align='center'></center>
<figcaption align='center'><b>Fig.11 -SDR11 Pipe Dimensions</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Friction Factor at 9 GPM.jpg'alt='Calculate Friction Factor at 9 GPM'align='center'></center>
<figcaption align='center'><b>Fig.12 - Calculate Friction Factor at 9 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Piping at 9 GPM.jpg'alt='Calculate Headloss of Piping at 9 GPM'align='center'></center>
<figcaption align='center'><b>Fig.13 - Calculate Headloss of Piping at 9 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Friction Factor at 18 GPM.jpg'alt='Calculate Friction Factor at 18 GPM'align='center'></center>
<figcaption align='center'><b>Fig.14 - Calculate Friction Factor at 18 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Piping at 18 GPM.jpg'alt='Calculate Headloss of Piping at 18 GPM'align='center'></center>
<figcaption align='center'><b>Fig.15 - Calculate Headloss of Piping at 18 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Friction Factor at 27 GPM.jpg'alt='Calculate Friction Factor at 27 GPM'align='center'></center>
<figcaption align='center'><b>Fig.16 - Calculate Friction Factor at 27 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Piping at 27 GPM.jpg'alt='Calculate Headloss of Piping at 27 GPM'align='center'></center>
<figcaption align='center'><b>Fig.17 - Calculate Headloss of Piping at 27 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Outdoor Piping.jpg'alt='Calculate Headloss of Outdoor Piping'align='center'></center>
<figcaption align='center'><b>Fig.18 - Calculate Headloss of Outdoor Piping</b></figcaption></figure>

**Calculate Fitting Headloss**

Next, the minorloss needs to be found. To find minorloss these parameters must be know: the K value corresponding to pipe diameter and fitting type, fluid velocity, and acceleration due to gravity. The K values can be found from literature and are presented in Fig.19. The approach to calculate minornloss at each individual flow rate in demonstrated in Fig.20 and then repeated in Fig.20 through Fig.23.  

<figure><center><img src='Question4\SDR11 Fitting K Values.jpg'alt='SDR11 Fitting K Values'align='center'></center>
<figcaption align='center'><b>Fig.19 - SDR11 Fitting K Values</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Fittings at 9 GPM.jpg'alt='Calculate Headloss of Fittings at 9 GPM'align='center'></center>
<figcaption align='center'><b>Fig.20 - Calculate Headloss of Fittings at 9 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Fittings at 18 GPM.jpg'alt='Calculate Headloss of Fittings at 18 GPM'align='center'></center>
<figcaption align='center'><b>Fig.21 - Calculate Headloss of Fittings at 18 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Fittings at 27 GPM.jpg'alt='Calculate Headloss of Fittings at 27 GPM'align='center'></center>
<figcaption align='center'><b>Fig.22 - Calculate Headloss of Fittings at 27 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Headloss of Outdoor Fittings.jpg'alt='Calculate Headloss of Outdoor Fittings'align='center'></center>
<figcaption align='center'><b>Fig.23 - Calculate Headloss of Outdoor Fittings</b></figcaption></figure>

**Calculate Headloss of Check Valves, Reducers, and Expanders**

While check valves, reducers, and expanders are technically fittings, for the purpose of this report it made more sense to calculate them apart from minorloss. Literature states that the K value for a check value is 100 times greater than the friction factor, however this left many question. Therefor, the designer decided to source their own check valves. Quickly upon searching, it became clear that there are almost no check valves that are the same 2” diameter as the piping and have a low enough cracking pressure to be a viable option. Because of this the designer chose two check different check valves, one ½” valve that will be installed inline with 9 GPM flow, and one 1” valve that will be installed inline with the 18 GPM flow. The dimensions for the selected check valves are presented in Fig.25. Once the check valves were selected the headloss was found using the chart in Fig.26.

<figure><center><img src='Question4\Check Valve Dimensions.jpg'alt='Check Valve Dimensions'align='center'></center>
<figcaption align='center'><b>Fig.25 - Check Valve Dimensions</b></figcaption></figure>

<figure><center><img src='Question4\Determine Check Valve Headloss.jpg'alt='Determine Check Valve Headloss'align='center'></center>
<figcaption align='center'><b>Fig.26 - Determine Check Valve Headloss</b></figcaption></figure>

As reducers and expanders fittings, the K value corresponding to pipe diameter and fitting type, fluid velocity, and acceleration due to gravity. The K values can be found from literature and are presented in Fig.27. The approach to calculate headloss from reducers and expander is demonstrated in Fig.28 and then repeated in Fig.28 through Fig.31.  

<figure><center><img src='Question4\SDR11 Reducer and Expander K Values.jpg'alt='SDR11 Reducer and Expander K Values'align='center'></center>
<figcaption align='center'><b>Fig.27 - SDR11 Reducer and Expander K Values</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Reducer Headloss at 9 GPM.jpg'alt='Calculate Reducer Headloss at 9 GPM'align='center'></center>
<figcaption align='center'><b>Fig.28 - Calculate Reducer Headloss at 9 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Reducer Headloss at 18 GPM.jpg'alt='Calculate Reducer Headloss at 18 GPM'align='center'></center>
<figcaption align='center'><b>Fig.29 - Calculate Reducer Headloss at 18 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Expander Headloss at 9 GPM.jpg'alt='Calculate Expander Headloss at 9 GPM'align='center'></center>
<figcaption align='center'><b>Fig.30 - Calculate Expander Headloss at 9 GPM</b></figcaption></figure>

<figure><center><img src='Question4\Calculate Expander Headloss at 18 GPM.jpg'alt='Calculate Expander Headloss at 18 GPM'align='center'></center>
<figcaption align='center'><b>Fig.31 - Calculate Expander Headloss at 18 GPM.jpg</b></figcaption></figure>

**Calculate Headloss of Equipment**

Lastly the headloss from equipment such as the head pumps and heat exchangers need to be accounted for. The headloss for the heat pumps has been calculated above. The headloss for the heat exchangers can be calculated using the relationship provided by the literature. This calculation is presented in Fig.32.  

<figure><center><img src='Question4\Calculate Headloss of Heat Exchangers.jpg'alt='Calculate Headloss of Heat Exchangers'align='center'></center>
<figcaption align='center'><b>Fig.32 - Calculate Headloss of Heat Exchangers</b></figcaption></figure>

**Pump Selection/Analysis**

The total system head can now be calculated by adding everything together and it is possible to size a pump. Fig.33 show the design point for pumps in series and single pump at 9 GPM and 18 GPM. The horizontal red line represents the design point for single pumps, and the horizontal blue line represents the design point for two pumps in series.  
The figure clearly shows that using a single pump to accommodate for the headloss at the design flowrate will not be enough. However, in series each pump will only be accountable for half of the head. The figure shows that there are many pump combinations that exceed the requirements. Using Fig.33, 2 TACO-0014 circulator pumps in series were selected to pump fluid through the TMW060 loop, and 2 TACO-0013 circulator pumps in series were selected to pump fluid through the TMW120 loop.  

<figure><center><img src='Question4\Pump Requirements in Series.jpg'alt='Pump Requirements in Series'align='center'></center>
<figcaption align='center'><b>Fig.33 - Pump Requirements in Series</b></figcaption></figure>

Using a python script, pump curves for a single TACO-0013, 2 TACO-0013 pumps in series, a singleTACO-0014, and 2 TACO-0014 in series were plotted. The required design points were also plotted as well as the actual operating point and system curves . By comparing the actual operating point headloss to the design point headloss it was confirmed that the pumps in series will work well.

<figure><center><img src='Question4\Pump Analysis.png'alt='Pump Analysis'align='center'></center>
<figcaption align='center'><b>Fig.34 - Pump Analysis</b></figcaption></figure>

## 5. Plotting Pump Curves

Similar to question 2, it is important for designers to validate their models against the manufacture data. A comparison between the plotted/calculated pump curve and the manufacture data is found in Fig.35

<figure><center><img src='Question5\Pump Model vs Manufacture Data.png'alt='Pump Model vs Manufacture Data'align='center'></center>
<figcaption align='center'><b>Fig.35 - Pump Model vs Manufacture Data</b></figcaption></figure>

## 6. P&ID and Headloss Summary

Below is a P&ID clarifying any design configurations. The headloss totals and the number of fittings for each loop are displayed in Fig.36 through Fig.39.

<figure><center><img src='Question6\P&ID.jpg'alt='P&ID'align='center'></center>
<figcaption align='center'><b>Fig.36 - P&ID</b></figcaption></figure>

<figure><center><img src='Question6\Headloss for Componenets Operating at 9 GPM.jpg'alt='Headloss for Componenets Operating at 9 GPM'align='center'></center>
<figcaption align='center'><b>Fig.37 - Headloss for Componenets Operating at 9 GPM</b></figcaption></figure>

<figure><center><img src='Question6\Headloss for Componenets Operating at 18 GPM.jpg'alt='Headloss for Componenets Operating at 18 GPM'align='center'></center>
<figcaption align='center'><b>Fig.38 - Headloss for Componenets Operating at 18 GPM</b></figcaption></figure>

<figure><center><img src='Question6\Headloss for Componenets Operating at 27 GPM.jpg'alt='Headloss for Componenets Operating at 27 GPM'align='center'></center>
<figcaption align='center'><b>Fig.39 - Headloss for Componenets Operating at 27 GPM</b></figcaption></figure>

## 7. Automating Headloss Calculations

Question 7 asked the designer to automate the work that was done in question 4. This was accomplished using the two python scripts that are displayed below. Headloss calculations have been reduced to one function, `headloss(diameter:float,flow_rate:float,length:float,heat_pump:bool=False,heat_pump_loss:float=0,heat_exchanger:bool=False,etc_loss:float=0,elbows:int=0,tstraight:int=0,tbranch:int=0)`. `diameter` is the diameter of the pipe, `flow_rate` is the flow rate of that section of piping, `length` is the length of straight pipe, `heat_pump` is a Boolean that determines if there is heat pump in that section of piping, `heat_pump_loss` is the headloss that was calculated elsewhere, `heat_exchanger` is a Boolean that determines if there is a heat exchanger in the loop, `etc_loss` accounts for any loss besides major, minor, or equipment loss (ie. Check valves, reducers and expanders), `elbows` is the number of elbows in the loop, `tstraight` is the number of Tee-Straight fittings in the loop, and `tbranch` is the number of Tee-Branch fittings in the loop.

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

Fig.40 shows the design point when only the TMW060 is operating. It is clear that the actual operating point has enough headloss to pump the needed headloss at the design point. The same conclusion can be made when only the TMW120 is operating. This can be concluded based on Fig.41.

<figure><center><img src='Question7\TMW060 Only Pump Curve.png'alt='TMW060 Only Pump Curve'align='center'></center>
<figcaption align='center'><b>Fig.40 - TMW060 Only Pump Curve</b></figcaption></figure>

<figure><center><img src='Question7\TMW120 Only Pump Curve.png'alt='TMW120 Only Pump Curve'align='center'></center>
<figcaption align='center'><b>Fig.41 - TMW120 Only Pump Curve</b></figcaption></figure>

## 8. Power Consumption Analysis

Question 8 required the calculation of system power consumption in different situations. The first thing that needs to be found is the power/electrical data for the heat pump and two pumps’ models. This data is shown in Fig.42, Fig.43, and Fig.44.  
To find the power the voltage and current need to be multiplied, this is done for the pumps and heat pump. Then the power of both pumps and the heat pump are added together to find the power per hour. Then the power per hour is multiplied by the operating time to find how much power is consumed for the time operated. The total system power is calculated by adding the power consumption rate of both loop and multiplying it by the operating time.  
Fig.45, Fig.46, and Fig.47 shows the calculations to find the power consumption of just the TMW060 operating for 800 hours, TMW120 operating for 1100 hours, and both heat pumps for 500 hours respectively.

<figure><center><img src='Question8\Heat Pumps Electrical Data.jpg'alt='Heat Exchanger Pumps Data'align='center'></center>
<figcaption align='center'><b>Fig.42 - Heat Pumps Electrical Data</b></figcaption></figure>

<figure><center><img src='Question8\TACO0014 Power Data.jpg'alt='TACO-0014 Power Data'align='center'></center>
<figcaption align='center'><b>Fig.43 - TACO-0014 Power Data</b></figcaption></figure>

<figure><center><img src='Question8\TACO0013 Power Data.jpg'alt='TACO-0013 Power Data'align='center'></center>
<figcaption align='center'><b>Fig.44 - TACO-0013 Power Data</b></figcaption></figure>

<figure><center><img src='Question8\TMW060 Only System Power.jpg'alt='TMW060 Only System Power'align='center'></center>
<figcaption align='center'><b>Fig.45 - TMW060 Only System Power Consumption</b></figcaption></figure>

<figure><center><img src='Question8\TMW120 Only System Power.jpg'alt='TMW120 Only System Power'align='center'></center>
<figcaption align='center'><b>Fig.46 - TMW120 Only System Power Consumption</b></figcaption></figure>

<figure><center><img src='Question8\System Power Usage.jpg'alt='System Power Usage'align='center'></center>
<figcaption align='center'><b>Fig.47 - System Power Consumption</b></figcaption></figure>
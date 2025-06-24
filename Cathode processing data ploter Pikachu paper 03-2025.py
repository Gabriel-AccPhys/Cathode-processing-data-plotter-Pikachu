#-----------------------------------------03/27/2025------------------------------
# importing modules
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import datetime

#-----------------------------------------Reading files and creating dataframes------------------------------
# For the file names, if there is many, maybe is better to rename them lie 1_V, 1_C, 1_D, 2_V, 2_C, 2_D, etc and make a for cycle

# Read the file name
print ("Give me the file number (In CSV format) ")
file_name = 'E:/Gabriel/Python/500kV_vac_test_2/Lognumber 4274608.csv'
# file_name = input()

# making data frame from csv file df and parse the dates
df = pd.read_csv(file_name , header = 0, names = ['time', 'Unix time', 'IGLGL01HVPSkVolts_ave', 'IGLGL01Preset_Volt', 'IGLGL01HVIREAD', 'IGLGL01UpRamp_Rate', 'VIPGT04cur', 'IFYGT00PICOdataRead', 'IDRGTS1RAD04'], parse_dates = ['time']) 
df = df.sort_values(by = ["time"], ascending = True)

# Print the data frame content
#print('Data frame content:')
#display(df)
#print()

# Drop duplicates
df = df.drop_duplicates(subset=['time'])
#print('Data frame content WITHOUT DUPLICATES:')
#display(df)
#print()

# Calculate step size for the elapsed time column 
Step_size = (df['time'].iloc[1] - df['time'].iloc[0]).total_seconds()
print('Step size is:', Step_size)
print('iloc 0 is:', df['time'].iloc[0])
print('iloc 1 is:', df['time'].iloc[1])
    
# Dropping the rows from dataframe when HV_On is 0, that means PS is OFF 
df.drop(df[df.IGLGL01Preset_Volt == 0].index, inplace = True)
        
# Add column with cumulative hrs to dataframe
df['Cumulative time [hrs]'] = (np.arange(0, 0+len(df)*Step_size, Step_size))/3600

#Asks the user for an input to select the x axis by cumulative time or by timestamp
print ("Plot by duration (d) or time (t)?")
if input() == 'd':
    x_axis = 'Cumulative time [hrs]'
else: x_axis = 'time'

# making data frame from csv file Current
#current = pd.read_csv(file_name + '_Current.csv', header = 0, names = ['time', 'gun current'])

#-----------------------------------------Plotting controls------------------------------
def plotter(file_name,x_1,y_1,y_2,y_3):
    #Define the size of the plot
    plt.rcParams["figure.figsize"] = [20.5, 17]
    plt.rcParams.update({'font.size': 20})

    fig, ax1 = plt.subplots()
    
    ax1.set_xlabel('Cummulative time [hours]')
    ax1.set_ylabel('Power supply voltage [kV]')
    ax1.plot(x_1,y_1,"ob", label = 'Voltage') #plots voltage
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    ax2.set_ylabel('Radiation monitor [cpm]')  # we already handled the x-label with ax1
    ax2.plot(x_1,y_2,"og", label = 'Radiation') #plots decarad
    ax2.tick_params(axis='y')

    # Create a third y-axis for Vacuum
    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(("outward", 120))  # Offset the third axis
    ax3.plot(x_1, y_3*(1/1E-3), 'o', color = 'orange', label='Pressure') # y_3 is in mili Amps
    ax3.set_ylabel('Ion pump pressure [mTorr]')
    ax3.tick_params(axis='y')
    plt.ylim(0, 0.12) # controls y-axis limit
    
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    #Plot title is created with file name
    plt.title('file name: ' + file_name) 

    #plt.ylim(0, 7) # controls y-axis limit
    #plt.grid(True) # controls Grid
  
    # Save the plot to file with the file_name variable as file name lol 
    plt.savefig(file_name + '.png') #save plot to png file
    
    # Show the plot
    leg = ax1.legend(loc = 'upper right') 
    leg = ax2.legend(loc = 'lower right')
    leg = ax3.legend(loc = 'upper left')
    plt.show() 
    
# Call the plotter sub function before changing files for troubleshooting
plotter(file_name, df[x_axis], df['IGLGL01HVPSkVolts_ave'], df['IDRGTS1RAD04'], df['VIPGT04cur'])

print('Done!')
#-----------------------------------------Data displays for troubleshooting------------------------------
# displays data for troubleshoot
#print('voltage data', voltage)
#print('decarad data', decarad)
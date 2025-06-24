# Cathode-processing-data-plotter-Pikachu
Cathode processing data plotter Pikachu
This script processes time-series data from a high-voltage power
supply test log, extracting voltage, radiation, and pressure readings
for diagnostic visualization. The data are imported from a CSV file
with timestamps, sorted, and cleaned to remove duplicates and idle-
state entries (i.e., when the preset voltage is zero). A cumulative time
column in hours is calculated based on the time resolution of the ac-
quisition. The user can choose between plotting against cumulative
time or absolute timestamp. The resulting figure uses three y-axes
to simultaneously display, power supply voltage (IGLGL01HVPSk-
Volts_ave), radiation monitor count rate (IDRGTS1RAD04), and ion
pump current (VIPGT04cur) converted to pressure in mTorr. The
figure is saved as a PNG file using the input filename and displayed
with labeled axes, legends, and a title derived from the file path.

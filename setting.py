# I2C address of the LSM6DSOX (0x6A if SA0 pin is low, otherwise 0x6B)
LSM6DSOX_ADDR = 0x6A

# Important LSM6DSOX registers
CTRL1_XL = 0x10       # Accelerometer configuration (ODR, range, etc.)
CTRL2_G = 0x11        # Gyroscope configuration (ODR, range, etc.)
CTRL3_C = 0x12        # General configuration (BDU, auto-increment...)
OUTX_L_G = 0x22       # Start of gyroscope data registers (6 bytes)
OUTX_L_XL = 0x28      # Start of accelerometer data registers (6 bytes)
# Time Delay
t = 1
# SCALE FACTOR
# - For other ranges (±4g, ±8g, ±16g or ±500/1000/2000 dps), the scale factor changes (see LSM6DSOX datasheet)
#   Accelerometer scale factors (LSB/g):
#     ±2g  : 0.000061 g/LSB
#     ±4g  : 0.000122 g/LSB
#     ±8g  : 0.000244 g/LSB
#     ±16g :   (0.000488 g/LSB
g = 0.000061
#   Gyroscope scale factors (LSB/dps):
#     ±250 dps  : 0.00875 dps/LSB
#     ±500 dps  : 0.0175 dps/LSB
#     ±1000 dps : 0.035 dps/LSB
#     ±2000 dps : 0.07 dps/LSB
dps = 0.00875
# =====================
# Additional notes:
#
# - To get acceleration in g, multiply the raw value by 0.000061 (for ±2g)
#   Example: x_g = x_a * 0.000061
#
# - To get angular velocity in dps (degrees/second), multiply the raw value by 0.00875 (for ±250 dps)
#   Example: x_dps = x_g * 0.00875
#
# - Raw values range from -32768 to +32767 (int16)
#   This corresponds to the full sensor range.
#
# - Raw values are in LSB (Least Significant Bit). To get a physical unit (g or dps), you must apply the scale factor.
#
# - Two's complement allows correct interpretation of negative values sent by the sensor.
#
# - To read the gyroscope, you must read from register OUTX_L_G (0x22)
#   (already done in the read_gyro() function)
#
# - For more details, see the official LSM6DSOX datasheet:
#   https://www.st.com/resource/en/datasheet/lsm6dsox.pdf
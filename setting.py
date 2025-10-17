# I2C address of the LSM6DSOX (0x6A if SA0 pin is low, otherwise 0x6B)
LSM6DSOX_ADDR = 0x6A
#frequency settings for accelerometer
FQ_POWER_DOWN = 0x00   #capteur désactivé
FQ12_5HZ      = 0x10
FQ26HZ        = 0x20
FQ52HZ        = 0x30
FQ104HZ       = 0x40
FQ208HZ       = 0x50
FQ416HZ       = 0x60
FQ833HZ       = 0x70
FQ1660HZ      = 0x80  # 1.66 kHz
FQ3330HZ      = 0x90  # 3.33 kHz
FQ6660HZ      = 0xA0  # 6.66 kHz
#Accelerometer full-scale selection
FS_2G  = 0x00
FS_16G = 0x04
FS_4G  = 0x08
FS_8G  = 0x0C

#Gyroscope Frequencies
FQ_G_POWER_DOWN = 0x00
FQ_G_12_5HZ     = 0x10
FQ_G_26HZ       = 0x20
FQ_G_52HZ       = 0x30
FQ_G_104HZ      = 0x40
FQ_G_208HZ      = 0x50
FQ_G_416HZ      = 0x60
FQ_G_833HZ      = 0x70
FQ_G_1660HZ     = 0x80
FQ_G_3330HZ     = 0x90
FQ_G_6660HZ     = 0xA0

# Gyroscope Full Scale
FS_G_125DPS   = 0x02
FS_G_245DPS   = 0x00
FS_G_500DPS   = 0x04
FS_G_1000DPS  = 0x08
FS_G_2000DPS  = 0x0C

# CTRL3_C_Register Bits
#define CTRL3_C_SW_RESET      0x80  // Bit 7: Software Reset
#define CTRL3_C_BOOT          0x40  // Bit 6: Reboot memory content
#define CTRL3_C_H_LACTIVE     0x20  // Bit 5: Interrupt active level
#define CTRL3_C_PP_OD         0x10  // Bit 4: Push-pull/open-drain
#define CTRL3_C_ODR           0x08  // Bit 3: Output Data Rate
#define CTRL3_C_ODR_G         0x04  // Bit 2: Gyroscope Output Data Rate
#define CTRL3_C_ODR_XL        0x02  // Bit 1: Accelerometer Output Data Rate
#define CTRL3_C_ODR_TEMP      0x01  // Bit 0: Temperature Output Data Rate


# Time delay for each data read (in seconds)
time_delay = 1
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
import smbus2
import time
from setting import *

# =====================
# LSM6DSOX  Driver for Raspberry Pi
# =====================
# This script reads acceleration (X, Y, Z) and gyroscope (X, Y, Z) values from the LSM6DSOX sensor
# connected to the standard I2C pins of the Raspberry Pi (SDA: GPIO 2, SCL: GPIO 3).
#
# The sensor communicates via the I2C bus. We use the smbus2 library here.
#
# The values read are raw (signed 16-bit integers). To get acceleration in g or angular velocity in dps,
# you must apply a scale factor (see notes at the end).

# I2C address of the LSM6DSOX (0x6A if SA0 pin is low, otherwise 0x6B)

class Driver:
    def __init__(self, bus=1, adresse=LSM6DSOX_ADDR):
        # Open the I2C bus (bus=1 for Raspberry Pi)
        self.bus = smbus2.SMBus(bus)
        self.adresse = adresse
        self.init_lsm6dsox()

    def init_lsm6dsox(self):
        # Initialize the sensor:
        # - Accelerometer at 104 Hz, ±2g range (0x40)
        #   (ODR_XL = 104 Hz, FS_XL = ±2g)
        self.bus.write_byte_data(self.adresse, CTRL1_XL, 0x42)
        # - Gyroscope at 104 Hz, ±250 dps range (0x40)
        #   (ODR_G = 104 Hz, FS_G = ±250 dps)
        self.bus.write_byte_data(self.adresse, CTRL2_G, 0x40)
        # - Enable BDU (Block Data Update) and auto-increment (0x44)
        self.bus.write_byte_data(self.adresse, CTRL3_C, 0x44)
        time.sleep(0.1)  # Small delay for settings to take effect

    def read_accel(self):
        # Read 6 bytes from OUTX_L_XL: X_L, X_H, Y_L, Y_H, Z_L, Z_H
        data = self.bus.read_i2c_block_data(self.adresse, OUTX_L_XL, 6)
        # Combine bytes and convert to signed integer (two's complement)
        x = self._twos_complement(data[1] << 8 | data[0], 16)
        y = self._twos_complement(data[3] << 8 | data[2], 16)
        z = self._twos_complement(data[5] << 8 | data[4], 16)
        return x, y, z

    def read_gyro(self):
        # Read 6 bytes from OUTX_L_G: X_L, X_H, Y_L, Y_H, Z_L, Z_H
        data = self.bus.read_i2c_block_data(self.adresse, OUTX_L_G, 6)
        # Combine bytes and convert to signed integer (two's complement)
        x = self._twos_complement(data[1] << 8 | data[0], 16)
        y = self._twos_complement(data[3] << 8 | data[2], 16)
        z = self._twos_complement(data[5] << 8 | data[4], 16)
        return x, y, z

    def _twos_complement(self, val, bits):
        # Convert an unsigned integer to signed (two's complement)
        # Example: 0xFFFE (65534) on 16 bits => -2
        if val & (1 << (bits - 1)):
            val -= 1 << bits
        return val


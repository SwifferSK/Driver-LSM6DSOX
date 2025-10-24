# Driver-LSM6DSOX
LSM6DSOX - Datasheet de STM Electronics

Voici les informations que l'on peut tirer d'après le [PDF officiel de STM Electronics](https://www.st.com/resource/en/datasheet/lsm6dsox.pdf)

1. __Qu'est-ce que le composant LSM6DSOX ?__

" The LSM6DSOX is a 6-axis IMU (inertial measurement unit) system-in-package
featuring a 3-axis digital accelerometer and a 3-axis digital gyroscope, boosting
performance at 0.55 mA in high-performance mode and enabling always-on lowpower features for an optimal motion experience for the consumer.

The LSM6DSOX supports the main OS requirements, offering real, virtual, and batch sensors with 9 KB for
dynamic data batching. [...] The LSM6DSOX has a full-scale __acceleration range of ±2/±4/±8/±16 g and an angular rate range of
±125/±250/±500/±1000/±2000 dps__ "

" The LSM6DSOX works as a combo accelerometer-gyroscope sensor, generating acceleration and angular rate
output data. It is also possible to connect an external sensor (magnetometer) by using the sensor hub feature
(mode 2). These data can be used as the input of up to 16 programs in the embedded finite state machine
All 16 finite state machines are independent: each one has its dedicated memory area and it is independently
executed. An interrupt is generated when the end state is reached or when some specific command is performed."

![Figure 1: State machine in the LSM6DSOX](images/fsm.png)

1. __Description des PIN__

![Figure 2: Pin connections](images/PIN_connection.png)

![Figure 3: Pin description](images/PIN_description.png)

2. __Protocole de communication I²C__

"The registers embedded inside the LSM6DSOX may be accessed through both the I²C and SPI serial interfaces.
The latter may be software configured to operate either in 3-wire or 4-wire interface mode. The device is
compatible with SPI modes 0 and 3.
The serial interfaces are mapped onto the same pins. To select/exploit the I²C interface, the CS line must be tied
high (that is, connected to VDDIO)."

![Figure 4: I²C/I3C coexistence in LSM6DSOX](images/I2C_Schemas.png)

"If the LSM6DSOX is configured in mode 2, a master I²C line is available. The master serial interface is mapped to
the following dedicated pins."

![Figure 5: Master I²C pin details](images/PIN_I2C.png)

Librairie trouvée : SINBUS

Données tirées d'après [la datasheet de STM Electronics](https://www.st.com/resource/en/datasheet/lsm6dsox.pdf)


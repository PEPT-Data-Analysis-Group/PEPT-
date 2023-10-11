# Data Analysis
# 1. Optimazation.
The 'Optimazation' data collected from the HR++ camera is going to be used for obtaining the f(opt) factor used in a convertion of .lm to .a files (readable onces)
This is done by, first plotting the 3D standard deviation as a function of f (i.e from 30% to 85%) then taking the minimum f value from the plot.
This f(opt) will then be ran through the PEPT algorithm to obtain .a files.
# 2. Calibration.
a. Rotation speed: you will set the power (product of V and I applied to the motor) by changing V. This will result in a rotation rate presumably linear in proportion to the power. Which depends on the load of the motor (the cylinder plus the fluid). So, you need to calibrate "what V gives the rotation RPM?". This is done with a tracer particle fixed to the inner (rotating) cylinder, and rotational speed measured (using PEPT) for different V. Then a linear response can be fitted to generate a calibration curve for the motor. Then you can set a rotation speed by using the appropriate V.

b. Position (and coordinate system): The motion is fundamentally in cylindrical coordinates, but PEPT gives you the trajectory in Cartesian coordinates. Thus, you need to convert from Cartesian to cylindrical. To do this you will need to know the centre of rotation. So, you will need to measure (using PEPT) the position of the device. You don't need the exact centre... you can use the rotation measurements above as the trajectory will be a circle centred on the origin, then you can fit the circular trajectory to the geometry and determine the axis centre. You will also need to determine which of (x, y, z) is the vertical direction, and in what sense.  Then you know the centre of rotation and the directions of the principle coordinate system unit vectors. Note this will change every time the system is moved - i.e. if the fluid is emptied and replaced with a different fluid this is a consideration. 


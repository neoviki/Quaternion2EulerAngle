'''
    Quaternion To Euler Angle Converter

    Authoe: Vignesh Natarajan
'''
import math
def Quaternion2EulerAngles(w, x, y, z):
    PIby2 = (math.pi / 2)

    # roll : rotation in x axis
    roll_x = float(2 * (w * x + y * z))
    roll_y = float(1 - 2 * (x * x + y * y))
    roll = math.atan2(roll_x, roll_y);

    # pitch : rotation in y axis
    pitch_var = float(2 * (w * y - z * x))
    if (abs(pitch_var) >= 1):
	#In the event of out of range -> use 90 degrees
        pitch = math.copysign(PIby2, pitch_var);
    else:
        pitch = math.asin(pitch_var);

    # yaw : rotation in z-axis
    yaw_x = 2 * (w * z + x * y);
    yaw_y = 1 - 2 * (y * y + z * z);
    yaw = math.atan2(yaw_x, yaw_y);

    print("roll     ( radians )  : "+str(roll))
    print("pitch    ( radians )  : "+str(pitch))
    print("yaw      ( radians )  : "+str(yaw))

    roll  = math.degrees(roll)
    pitch = math.degrees(pitch)
    yaw   = math.degrees(yaw)

    print("roll     ( degrees )  : "+str(roll))
    print("pitch    ( degrees )  : "+str(pitch))
    print("yaw      ( degrees )  : "+str(yaw))

    return roll, pitch, yaw
Quaternion2EulerAngles(0.9995431, 0.0174506, 0.0174506, 0.0174506)

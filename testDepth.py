from rc import RCLib
import time
import imu as imu

rc = RCLib()

rc.setmode('ALT_HOLD')

rc.arm()

#print(rc.getDeg())

#time.sleep(5)

rc.throttle('time', 2.5, -0.25)

rc.setmode('ALT_HOLD')

rc.yaw('time', 10, 0)


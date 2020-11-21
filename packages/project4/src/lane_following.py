class lanefollowing:
    def __init__(self):
        self.previous_error_d = 0
        self.set_point_d = 1
        self.kp_d=1
        self.kd_d=1
        self.dt=0.1
    
#self.previous_error_phi = 0
#self.set_point_phi = 0
#self.kp_phi = 1
#self.kd_phi = 1

    def pd_controller_d(self,measured_value):
        print ("set point pre")
        print(self.previous_error_d)
        self.error = self.set_point_d - measured_value 
        self.derivative = (self.error - self.previous_error_d)/self.dt
        self.previous_error_d = self.error
        print ("set point")
        print(self.previous_error_d)

        return self.kp_d*self.error + self.kd_d*self.derivative

test=lanefollowing()
while True:
    x=test.pd_controller_d(1.3)
    t=test.pd_controller_d(2)
    print(x) 
    print(t)

import math

u=int(input("Enter initial velocity in m/s: "))
angle=int(input("Enter launch angle in degrees: "))
g = 9.81

try:
    if u<=0:
        raise ValueError("Initial velocity must be greater than 0.")  
    elif angle<0 or angle>90:
        raise ValueError("Launch angle must be between 0 and 90 degrees.") 
    else:
        theta=math.radians(angle) # Convert angle to radians
        ux=u*math.cos(theta)
        uy=u*math.sin(theta)
        time_of_flight=(2*uy)/g
        max_height=(math.pow(uy,2))/2*g
        horizontal_range=ux*time_of_flight
        impact_velocity=math.sqrt(math.pow(ux,2)+math.pow(uy,2))
        max_range=math.pow(u,2)/g
        efficiency=(horizontal_range/max_range)*100

        print(f"Horizontal component of initial velocity: {ux:.2f} m/s")
        print(f"Vertical component of initial velocity: {uy:.2f} m/s")
        print(f"Time of flight: {time_of_flight:.2f} seconds")
        print(f"Maximum height reached: {max_height:.2f} meters")
        print(f"Horizontal range: {horizontal_range:.2f} meters")
        print(f"Impact velocity: {impact_velocity:.2f} m/s")
        print(f"Maximum range: {max_range:.2f} meters")
        print(f"Range Efficiency: {efficiency:.2f}%")

except ValueError as e:
    print("Error:", e) 


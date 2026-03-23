def speed_of_sound(temp_celsius):
    if temp_celsius < -50 or temp_celsius > 100:
        print("Earth temps only")

    speed = 331.4 + (0.6 * temp_celsius)
    return speed

temp_c = 20
speed_at_20 = speed_of_sound(temp_c)
print(f"{temp_c:.2f} m/s")
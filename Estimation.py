def estimate_traffic_delay(num_cars, avg_speed, distance):
    delay_time = (distance / avg_speed) * (1 + (num_cars / 50)**2)
    return delay_time

# Example usage:
num_cars = 30
avg_speed = 50
distance = 200
delay = estimate_traffic_delay(num_cars, avg_speed, distance)
print("Estimated traffic delay:", delay)

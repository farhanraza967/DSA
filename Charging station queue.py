class Queue:
    def __init__(self):
        self.values = []

    def enqueue(self, x):
        print("A vehicle has arrived and is added to the waiting queue:", x)
        self.values.append(x)

    def dequeue(self):
        if len(self.values) == 0:
            print("There are no more vehicles waiting. The queue is empty.")
            return None
        front = self.values[0]
        print("The next vehicle in the queue is now being sent for charging:", front)
        self.values = self.values[1:]
        return front

class Vehicle:
    def __init__(self, veh_id, owner, battery_level, charge_time):
        self.veh_id = veh_id
        self.owner = owner
        self.battery_level = battery_level
        self.charge_time = charge_time

    def __str__(self):
        return self.veh_id + " - " + self.owner + " (" + str(self.battery_level) + "%, " + str(self.charge_time) + " min)"

q = Queue()

print("Charging Station System Started...\n")

v1 = Vehicle("EV-101", "Ali", 25, 45)
v2 = Vehicle("EV-102", "Sara", 40, 30)
v3 = Vehicle("EV-103", "Ahmed", 15, 60)

print("Adding vehicles to the charging queue...\n")
q.enqueue(v1)
q.enqueue(v2)
q.enqueue(v3)

print("\nCurrent vehicles waiting:")
for v in q.values:
    print(" ->", v)

print("\nStarting charging process...\n")
while True:
    next_vehicle = q.dequeue()
    if next_vehicle is None:
        print("All vehicles have been processed. Charging station is now clear.")
        break

    print("Charging vehicle", next_vehicle.veh_id, "owned by", next_vehicle.owner)
    print("Estimated charging time:", next_vehicle.charge_time, "minutes.")
    print("Battery level before charging:", next_vehicle.battery_level, "%\n")

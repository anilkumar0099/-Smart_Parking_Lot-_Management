from datetime import datetime

class CarNode:
    def __init__(self, plate, owner):
        self.plate = plate
        self.owner = owner
        self.entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.next = None


class ParkingLot:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.size = 0

    def park_car(self, plate, owner):
        if self.size >= self.capacity:
            print("❌ Parking lot is FULL! Car cannot be parked.")
            return

        new_car = CarNode(plate, owner)
        if not self.head:
            self.head = new_car
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_car

        self.size += 1
        print(f"✅ Car parked: {plate} ({owner}) at {new_car.entry_time}")

    def exit_car(self, plate):
        if not self.head:
            print("❌ No cars in the parking lot.")
            return

        if self.head.plate == plate:
            print(f"🚗 Car exited: {self.head.plate} ({self.head.owner})")
            self.head = self.head.next
            self.size -= 1
            return

        prev = self.head
        current = self.head.next
        while current:
            if current.plate == plate:
                print(f"🚗 Car exited: {current.plate} ({current.owner})")
                prev.next = current.next
                self.size -= 1
                return
            prev, current = current, current.next

        print(f"❌ Car with plate {plate} not found.")

    def show_parked_cars(self):
        if not self.head:
            print("🅿️ Parking lot is empty.")
            return

        print(f"\n🅿️ Currently Parked Cars ({self.size}/{self.capacity}):")
        current = self.head
        while current:
            print(f"- {current.plate} | Owner: {current.owner} | Entry: {current.entry_time}")
            current = current.next
        print()


# Example Usage
if __name__ == "__main__":
    lot = ParkingLot(capacity=3)

    lot.park_car("TS01AB1234", "ANIL")
    lot.park_car("TS02CD5678", "BHARATH")
    lot.park_car("TS03EF9999", "CHARAN")
    lot.park_car("TS04GH0001", "DAVID")  # Overflow

    lot.show_parked_cars()

    lot.exit_car("TS02CD5678")
    lot.exit_car("TS05XY1111")  # Not found

    lot.show_parked_cars()


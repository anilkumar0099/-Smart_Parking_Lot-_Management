# 🅿️ Smart Parking Lot Management

A Python project to simulate a **smart parking lot system** with entry/exit tracking, using **linked lists** to store active cars.  
It demonstrates **dynamic memory allocation** for parking slots and **overflow handling** when the lot is full.

---

## 🚀 Features
- ✅ Park a car (with plate number, owner name, entry time)  
- ✅ Remove a car when it exits  
- ✅ Display all currently parked cars  
- ✅ Handle **overflow** when the parking lot is full  
- ✅ Linked list used for active parked cars (self-referential structure)  

---

## 🛠️ Tech Requirements
- **Linked List** → Each car is a node (`plate, owner, entry_time`).  
- **Dynamic Memory Allocation** → New nodes created for each parked car.  
- **Overflow Handling** → Reject cars if the lot is full.  
- **Entry/Exit Tracking** → Add/remove cars as they enter/exit.  


---

## 📖 How It Works
1. **Park Car** → Adds a new node (car) if space available.  
2. **Exit Car** → Removes the node if the car is found in the lot.  
3. **Show Cars** → Displays all active parked cars.  
4. **Overflow Check** → If lot is full, new cars are rejected.  

##Output Example

✅ Car parked: TS01AB1234 (ANIL) at 2025-08-22 17:50:33
✅ Car parked: TS02CD5678 (BHARATH) at 2025-08-22 17:50:33
✅ Car parked: TS03EF9999 (CHARAN) at 2025-08-22 17:50:33
❌ Parking lot is FULL! Car cannot be parked.

🅿️ Currently Parked Cars (3/3):
- TS01AB1234 | Owner: ANIL | Entry: 2025-08-22 17:50:33
- TS02CD5678 | Owner: BHARATH | Entry: 2025-08-22 17:50:33
- TS03EF9999 | Owner: CHARAN | Entry: 2025-08-22 17:50:33

🚗 Car exited: TS02CD5678 (Bob)
❌ Car with plate TS05XY1111 not found.

🅿️ Currently Parked Cars (2/3):
- TS01AB1234 | Owner: ANIL | Entry: 2025-08-22 17:50:33
- TS03EF9999 | Owner: BHARATH | Entry: 2025-08-22 17:50:33



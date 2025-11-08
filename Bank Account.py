class Customer:
    def __init__(self, name, nic, acc_no, balance):
        self.name = name
        self.nic = nic
        self.acc_no = acc_no
        self.balance = balance

    def disp(self):
        print("Name: " + self.name + ", NIC: " + self.nic + ", Account: " + self.acc_no + ", Balance: Rs." + str(self.balance))

    def upt_bal(self, new_balance):
        self.balance = new_balance
        print("Updated balance for " + self.name + ": Rs." + str(self.balance))

cust1 = Customer("Ali Khan", "42101-1234567-1", "ACC1001", 55000)
cust2 = Customer("Sara Ahmed", "42202-7654321-9", "ACC1002", 90000)
cust3 = Customer("Bilal Raza", "42301-9876543-5", "ACC1003", 35000)

customers = [cust1, cust2, cust3]

print("\n--- Customer Accounts Created ---")
cust1.disp()
cust2.disp()
cust3.disp()

cust1.upt_bal(60000)

for i in range(len(customers)):
    min_pos = i
    for j in range(i + 1, len(customers)):
        if customers[j].name < customers[min_pos].name:
            min_pos = j
    temp = customers[i]
    customers[i] = customers[min_pos]
    customers[min_pos] = temp

print("\n--- Sorted by Name (Selection Sort) ---")
for c in customers:
    c.disp()

for i in range(len(customers)):
    max_pos = i
    for j in range(i + 1, len(customers)):
        if customers[j].balance > customers[max_pos].balance:
            max_pos = j
    temp = customers[i]
    customers[i] = customers[max_pos]
    customers[max_pos] = temp

print("\n--- Sorted by Balance (Selection Sort) ---")
for c in customers:
    c.disp()

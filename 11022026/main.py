class Customer:
    count = 0

    def __init__(self, name, num_of_purchases):
        self.name = name
        self.num_of_purchases = num_of_purchases
        Customer.count += 1

    @classmethod
    def add_count(cls):
        return f"{Customer.count}"
    
customer1 = Customer("testing testing", 2131)
print(customer1)
print(Customer.count)
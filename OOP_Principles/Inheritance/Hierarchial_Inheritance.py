class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions
    
    def manage_users(self):
        print(f"{self.username} managing users with {self.permissions}")

class Customer(User):
    def __init__(self, username, email, cart_id):
        super().__init__(username, email)
        self.cart_id = cart_id
    
    def view_cart(self):
        print(f"{self.username} viewing cart {self.cart_id}")

admin = Admin("admin1", "admin@shop.com", ["read", "write"])
customer = Customer("user123", "user@shop.com", "CART_456")
admin.login()      # admin1 logged in (inherited)
admin.manage_users()  # admin1 managing users with ['read', 'write']
customer.view_cart()  # user123 viewing cart CART_456

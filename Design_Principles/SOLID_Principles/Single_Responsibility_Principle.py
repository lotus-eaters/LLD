# A class should have only one reason to change" which means every class should have a single responsibility or single job or single purpose.

# Class for baking bread
class BreadBaker:
    def bakeBread(self):
        print("Baking high-quality bread...")

# Class for managing inventory
class InventoryManager:
    def manageInventory(self):
        print("Managing inventory...")

# Class for ordering supplies
class SupplyOrder:
    def orderSupplies(self):
        print("Ordering supplies...")

# Class for serving customers
class CustomerService:
    def serveCustomer(self):
        print("Serving customers...")

# Class for cleaning the bakery
class BakeryCleaner:
    def cleanBakery(self):
        print("Cleaning the bakery...")

def main():
    baker = BreadBaker()
    inventoryManager = InventoryManager()
    supplyOrder = SupplyOrder()
    customerService = CustomerService()
    cleaner = BakeryCleaner()

    # Each class focuses on its specific responsibility
    baker.bakeBread()
    inventoryManager.manageInventory()
    supplyOrder.orderSupplies()
    customerService.serveCustomer()
    cleaner.cleanBakery()

if __name__ == "__main__":
    main()

# BreadBaker Class: Responsible solely for baking bread. This class focuses on ensuring the quality and standards of the bread without being burdened by other tasks.
# InventoryManager Class: Handles inventory management, ensuring that the bakery has the right ingredients and supplies available.
# SupplyOrder Class: Manages ordering supplies, ensuring that the bakery is stocked with necessary items.
# CustomerService Class: Takes care of serving customers, providing a focused approach to customer interactions.
# BakeryCleaner Class: Responsible for cleaning the bakery, ensuring a hygienic environment.
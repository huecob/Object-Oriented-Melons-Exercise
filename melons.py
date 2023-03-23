"""Classes for melon orders."""

class AbstractMelonOrder:

    def __init__(self,species,qty):
        """ Initializing the attributes of the melon order"""
        self.species = species
        self.qty = qty
        self.shipped = False

    def __repr__(self):
        """prints neatly :)"""
        return f"<Melon: {self.species}, Qty: {self.qty}>"
    
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        
        if self.species == "Christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10 and self.order_type == "international":
            total += 3
        
        return total
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
    
        super().__init__(species, qty)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        
        self.country_code = country_code
 
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
        
class GovernmentMelonOrder(AbstractMelonOrder):
    """Initializes terrible people buying melons"""

    tax = 0
    passed_inspection = False

    def marked_inspection(passed):
        if passed == True:
            passed_inspection = True

order0 = GovernmentMelonOrder("Watermelon", 10)
order1 = InternationalMelonOrder("Watermelon",10,"AUS")
order2 = InternationalMelonOrder("Christmas", 11, "USA")
order3 = InternationalMelonOrder("Christmas", 9, "USA")


order1.get_total()
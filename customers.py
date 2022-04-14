"""Customers at Hackbright.


This provides a Customer class, helper methods to get all customers, find a
customer by email_id.

It reads customer data in from a text file customer.txt.
"""


class Customer:
    """Ubermelon customer."""

    def __init__(
        self,
        first_name,
        last_name,
        email_id,
        password,
    ):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email_id}, {self.password}>"
        )

def read_customer_types_from_file(filepath):
    """ Read customer data and populate dictionary of customers. 
       Dictionary will be {email_id: Customer object}
    """

    customer = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email_id,
                password
            ) = line.strip().split("|")

            customer[email_id] = Customer(first_name, last_name, email_id, password, )

    return customer

def get_by_email(email_id):
    """Return a customer, given his/her EMAILID."""

    # This relies on access to the global dictionary customer

    return customer[email_id]

customer = read_customer_types_from_file("customers.txt")
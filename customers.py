"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
             first_name,
             last_name,
             email,
             password,
             ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {first_name} {last_name}, {email}, {password}>".format(first_name=self.first_name,
                        last_name=self.last_name,
                        email=self.email,
                        password=self.password)


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customer info.

    Dictionary will be {email: Customer object}
    """

    customer_info = {}

    for line in open(filepath):
        (first_name,
         last_name,
         email ,
         password) = line.strip().split("|")

        customer_info[email] = Customer(first_name,
                                      last_name,
                                      email,
                                      password)

    return customer_info

def get_by_email(email):
    """Return a customer, given their email address."""

    return customer_info[email]

customer_info = read_customers_from_file("customers.txt")
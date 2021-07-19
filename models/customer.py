class Customer():
    """Customer class def
    """
    def __init__(self, id, name, address, email="", password=""):
        self.id = id
        self.full_name = name
        self.address = address
        self.email = email
        self.password = password
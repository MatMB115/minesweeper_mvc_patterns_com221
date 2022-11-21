class Cell:
    """Сell is the class from which the field is built.

       State attribute can be:
           -opened
           -closed
           -flagged
           -questioned """

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.state = "closed"
        self.mined = False
        self.int_state = 9  # Blank
        self.counter = 0

    sequence = ["closed", "flagged", "questioned"]
    int_sequence = [9, 10, 11]

    def open(self):
        """When cell is not disable(flagged) we can open it."""
        if (self.state != "flagged" and
                self.state != "opened" and
                self.state != "disable"):
            self.state = "opened"
            self.int_state = 0

    def next_mark(self):
        """Change cell state when right click made."""
        # if cell is not already opened.
        if self.state != "opened" and self.state != "disable":
            _index = self.sequence.index(self.state)
            self.state = self.sequence[(_index + 1) % len(self.sequence)]
            self.int_state = self.int_sequence[(_index + 1) % len(self.sequence)]

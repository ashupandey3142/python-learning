# classmethod is used when a method needs access to the class itself, often for operations involving class-level variables.
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('/'))
        return cls(year, month, day)

    def display_date(self):
        print(f"{self.year}-{self.month:02d}-{self.day:02d}")


# Using the class method to create instances
date_string_1 = "2023/12/15"
date_string_2 = "2022/05/28"

date1 = Date.from_string(date_string_1)
date2 = Date.from_string(date_string_2)

# Displaying the dates
date1.display_date()
date2.display_date()

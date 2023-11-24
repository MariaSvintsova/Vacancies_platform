class Handle_job():

    def __init__(self, title: str, city: str, salary_to: int, salary_from: int, short_description: str) -> None:

        self.title = title
        self.city = city
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.short_description = short_description

    def is_valid(self, title: str, link: str, salary_to: int, salary_from: int, short_description: str):
        if not title or not link or not salary_to or not salary_from or not short_description:
            raise ValueError('All atributes must be provided')


    def __str__(self):
        return f"Job title: {self.title}\nLink: {self.city}\nsalary_to: {self.salary_to}\nsalary_from: {self.salary_from}\nDescription: {self.short_description}"


    def __eq__(self, other):
        if not isinstance(other, Handle_job):
            return False
        if self.salary_to is None or other.salary_to is None:
            return self.salary_from == other.salary_from
        return self.salary_to == other.salary_to


    def __gt__(self, other):
        if not isinstance(other, Handle_job):
            return False
        if self.salary_to is None or other.salary_to is None:
            return self.salary_from > other.salary_from
        return self.salary_to > other.salary_to


    def __lt__(self, other):
        if not isinstance(other, Handle_job):
            return False
        if self.salary_to is None or other.salary_to is None:
            return self.salary_from < other.salary_from
        return self.salary_to < other.salary_to


    # def __cmp__(self, other):
    #     if isinstance(other, MyClass):
    #         return cmp(self.value, other.value)
    #     return cmp(id(self), id(other))


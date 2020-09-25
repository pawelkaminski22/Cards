from faker import Faker
cards = []


class BaseContact:
    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self._label_length = len(name) + len(last_name)

    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = len(value)

    def contact(self):
        return print(f'Wybieram numer: {self.phone} i dzwonie do {self.name} {self.last_name}')


class BusinessContact(BaseContact):
    def __init__(self, name, last_name, phone, email, position, company, work_phone):
        super().__init__(name, last_name, phone, email)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        return print(f'Wybieram numer: {self.work_phone} i dzwonie do {self.name} {self.last_name}')


if __name__ == '__main__':
    fake = Faker()

    def create_contacts(card_type, quantity):
        if card_type == 'base':
            for i in range(quantity):
                friend = BaseContact(fake.first_name(), fake.last_name(), fake.random_int(), fake.email())
                cards.append({'name': friend.name, 'last name': friend.last_name, 'phone': friend.phone, 'email': friend.email})
                print(friend.label_length)
                friend.contact()

        elif card_type == 'business':
            for i in range(quantity):
                friend = BusinessContact(fake.first_name(), fake.last_name(), fake.random_int(), fake.email(),
                                         fake.job(), fake.company(), fake.random_int())
                cards.append({'name': friend.name, 'last name': friend.last_name, 'phone': friend.phone, 'email': friend.email,
                              'position': friend.position, 'company': friend.company, 'work phone': friend.work_phone})
                print(friend.label_length)
                friend.contact()


    s_cards = sorted(cards, key=lambda k: k['name'])

    create_contacts('business', 2)
    print(cards)




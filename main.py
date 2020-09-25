from faker import Faker

cards = []


class BaseContact:
    def __init__(self, name, last_name, telephone, email):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.telephone = telephone
        self._name_len = len(name) + len(last_name)

    @property
    def name_len(self):
        return self._name_len

    @name_len.setter
    def name_len(self, value):
        self._name_len = len(value)

    def __str__(self):
        return f'{self.name} {self.last_name} with email: {self.email}'

    def contact(self):
        return print(f'Kontaktuje sie z: {self.name} {self.last_name} pracuje jako {self.position} i posiada maila {self.email}')


if __name__ == '__main__':
    fake = Faker()
    friend = Card(fake.first_name(), fake.last_name(), fake.job(), fake.email())

    for i in range(3):
        friend = Card(fake.first_name(), fake.last_name(), fake.job(), fake.email())
        cards.append({'name': friend.name, 'last name': friend.last_name, 'email': friend.email})
        print(friend.name_len)
        print(friend.contact())

    s_cards = sorted(cards, key=lambda k: k['email'])

    #print(cards)
    #print(s_cards)
    print(friend)




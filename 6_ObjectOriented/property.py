# wird eher selten benötigt

# Property: quasi Getter/Setter  -> dadurch kann weiterhin per User.name auf die Variable zugegriffen werden
# _var - private

class User:
    def __init__(self, name, user_id):
        self._name = name  # private attribut
        self._user_id = user_id # private attribut

    def __str__(self):
        return '{}, {}'.format(self._name, self._user_id)

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

u1 = User('Hans', 123)
print(u1)
u1.name = 'Franz'
print(u1)
print(u1.name)


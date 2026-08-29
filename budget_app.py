class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': float(amount), 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False

        self.ledger.append({'amount': -float(amount), 'description': description})
        return True

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        category.deposit(amount, f'Transfer from {self.name}')
        self.withdraw(amount, f'Transfer to {category.name}')
        return True

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        output = f'{self.name[:30]:*^30}\n'
        for item in self.ledger:
            description = item['description'][:23]
            amount = f"{item['amount']:.2f}"
            if len(amount) > 7:
                amount = f"{item['amount']:.1f}"
                if len(amount) > 7:
                    amount = f"{item['amount']:.0f}"
                    if len(amount) > 7:
                        amount = amount[:7]
            output += f"{description:<23}{amount:>7}\n"
        output += f'Total: {self.get_balance():.2f}'
        return output


def create_spend_chart(categories):
    total_spent = 0
    for category in categories:
        for item in category.ledger:
            if item['amount'] < 0:
                total_spent += -item['amount']

    percentages = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']

        if total_spent == 0:
            percent = 0
        else:
            percent = int(spent / total_spent * 100)
            percent = (percent // 10) * 10
        percentages.append(percent)

    output = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        output += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                output += " o "
            else:
                output += "   "
        output += " \n"

    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)

    for i in range(max_len):
        output += "     "
        for category in categories:
            if i < len(category.name):
                output += f"{category.name[i]}  "
            else:
                output += "   "
        if i < max_len - 1:
            output += "\n"

    return output
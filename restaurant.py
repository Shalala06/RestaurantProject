class Table:

    def __init__(self, num_of_people):
        self.num_of_people = num_of_people
        self.bill = {"item": [], "price": [], "quantity": []}

    def order(self, item, price, quantity=1):
        for i in range(len(self.bill["item"])):
            if self.bill["item"][i] == item and self.bill["price"][i] == price:
                self.bill["quantity"][i] += quantity
                break
        else:
            self.bill["item"].append(item)
            self.bill["price"].append(price)
            self.bill["quantity"].append(quantity)

    def remove(self, item, price, quantity=1):
        for i in range(len(self.bill["item"])):
            if self.bill["item"][i] == item and self.bill["price"][i] == price:
                self.bill["quantity"][i] -= quantity

    def get_subtotal(self):
        sub_total = 0
        for i in range(len(self.bill["item"])):
            item_total = (self.bill["quantity"][i])*(self.bill["price"][i])
            sub_total =sub_total+item_total
        return sub_total
    def get_total(self,service_charge_percentage = 0.1):
        sub_total_pound = "£" + str(format(self.get_subtotal(),".2f"))
        service_charge = format((float(self.get_subtotal())*service_charge_percentage),".2f")
        service_charge_pound = "£" + str(service_charge)
        total = format((self.get_subtotal() + float(service_charge)),".2f")
        total_pound = "£" + str(total)
        get_total_dic = {"Sub Total": sub_total_pound, "Service Charge": service_charge_pound, "Total": total_pound}

        return get_total_dic

    def split_bill(self):
        split_total = float(format((self.get_subtotal())/self.num_of_people,".2f")) # still need to add round.

        return split_total

        print(self.bill)

#  update_price(self, percent_change, is_increased) 
# - updates the product's price. If is_increased is True, the price should
#  increase by the percent_change provided. If False, the price should decrease
#  by the percent_change provided.
def update_price(self,percent_change,is_increased):
    if is_increased == True:
        self.price += percent_change
    else:
        self.price -= percent_change
    return self
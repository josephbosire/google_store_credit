__author__ = 'josephbosire'
"""
The trick with contest question is that the complement price might be equal to the partner price so
that means in a sorted list the next number in the least would be same and that is the price to pick.
Also in this combination problem you needed to sort the list first then just subtract the credit from the current item price
and search if that complimentary price is there
"""
def load_data_set():
    data_Set = {}
    with open("answers.out", "wb") as answer_file:
        with open("A-large-practice.in", "rb") as input_file:
            number_of_cases = input_file.readline()
            data = input_file.readlines()
            count = 1
            for credit_index in range(0, len(data), 3):
              credit = int(data[credit_index])
              num_of_items = data[credit_index+1].rstrip()
              item_prices = [int(d) for d in data[credit_index+2].rstrip().split(" ")]
              lower, upper = get_max_combination(item_prices, credit)
              answer_file.write("Case #{}: {} {}\n".format(count, lower, upper))
              count += 1

def get_max_combination(item_prices, credit):
    sorted_item_prices = sorted(item_prices)
    for item_price in sorted_item_prices:
        complement_price = credit - item_price
        if complement_price in sorted_item_prices:
            ind1 = item_prices.index(item_price)+1
            ind2 = item_prices.index(complement_price)+1
            if complement_price == item_price:
                ind2 += 1
            print item_price, complement_price
            return min(ind1, ind2), max(ind1, ind2)


print load_data_set()
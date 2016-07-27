# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    total_value = 0.
    # Сначала ложим по максимуму тот товар который дороже,
    # потом дешевле и дешевле ...
    dictionary = {}
    for i in range(0, len(values)):
        dictionary[i+1] = {'frac': values[i] / weights[i], 'value': values[i], 'weights': weights[i]}

    while capacity > 0:
        if bool(dictionary):
            max_frac_item_key = max(dictionary, key=lambda k: dictionary[k]['frac'])
            max_frac_object = dictionary[max_frac_item_key]

            space_left = capacity - max_frac_object['weights']

            if space_left >= 0:
                capacity = space_left # reduce capacity by best item amount
                total_value += max_frac_object['value'] # increase total value
                dictionary.pop(max_frac_item_key) # remove this item from tmp dict
                continue
            if space_left < 0: # amount of items to big to fit into bag
                # Here we just take item amount that left (it is actually capacity itself)
                # and multiply by proper value
                total_value += capacity * max_frac_object['frac']
                capacity = 0 # There is no capacity left at all!
                dictionary.pop(max_frac_item_key) # remove this item from tmp dict
        else:
            break
    return total_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    # Check for validity
    max_limit = 2*10**6
    all_valid = True
    if (n >= 1) and (n <= 10**3):
        if (capacity >= 0) and (capacity <= max_limit):
            for i in range(0, n):
                if (values[i] >= 0) and (values[i] <= max_limit) and (weights[i] >= 1) and (weights[i] <= max_limit):
                    all_valid = True
                else:
                    all_valid = False
                    break

            if all_valid == True:
                opt_value = get_optimal_value(capacity, weights, values)
                print("{:.10f}".format(opt_value))

# Test
# for n in range(1, 10):
#     print('--- New bag ---')
#     print('bag total items', n)
#     for c in range(0, 5):
#         print('bag weight', c)
#         capacity = c
#         values = [1]*n
#         weights = [c]*n
#         print('values',values)
#         print('weights',weights)
#
#         # Check for validity
#         max_limit = 2*10**6
#         all_valid = True
#         if (n >= 1) and (n <= 10**3):
#             if (capacity >= 0) and (capacity <= max_limit):
#                 for i in range(0, n):
#                     # NOTE change v to v >= 0
#                     if (values[i] >= 1) and (values[i] <= max_limit) and (weights[i] >= 1) and (weights[i] <= max_limit):
#                         all_valid = True
#                     else:
#                         all_valid = False
#                         break
#
#                 if all_valid == True:
#                     opt_value = get_optimal_value(capacity, weights, values)
#                     print("{:.10f}".format(opt_value))

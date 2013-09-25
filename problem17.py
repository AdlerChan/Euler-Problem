def return_num_words(n):
    dic_ten = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5,\
               '8': 5, '9': 4}
    dic_twenty = {'10': 3, '11': 6, '12': 6, '13': 8, '14': 8, '15': 7,\
                  '16': 7, '17': 9, '18': 8, '19': 8}
    dic_decade = {'2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6,\
                  '9': 6}
    dic_hundred = {'100': 7, 'and': 3, '1000': 11}

    if 1 <= n < 10:
        return dic_ten[str(n)]
    elif 10 <= n < 20:
        return dic_twenty[str(n)]
    else:
        if 2 == len(str(n)):
            if 0 == n % 10:
                return dic_decade[str(n / 10)]
            else:
                return dic_decade[str(n / 10)] + dic_ten[str(n % 10)]
        elif 3 == len(str(n)):
            if 0 == n % 100:
                return dic_ten[str(n / 100)] + dic_hundred['100']
            else:
                if 1 <= (n % 100) < 10:
                    return dic_ten[str(n / 100)] + dic_hundred['100'] +\
                           dic_hundred['and'] + dic_ten[str(n % 100)]
                elif 10 <= (n % 100) < 20:
                    return dic_ten[str(n / 100)] + dic_hundred['100'] +\
                           dic_hundred['and'] + dic_twenty[str(n % 100)]
                else:
                    return dic_ten[str(n / 100)] + dic_hundred['100'] +\
                         dic_hundred['and'] + dic_decade[str((n % 100) / 10)]\
                         + dic_ten[str((n % 100) % 10)]
        else:
            return dic_hundred['1000']

if __name__ == "__main__":
    print sum(map(lambda x: return_num_words(x), range(1, 1001)))

# FOR LOOPS
# for loops can iterate over data within lists
titans = ['ryu', 'crystal', 'titan', 'ken', 'philip']

# for titan in titans:
#     print(titan)

for titan in titans[1:4]:
    print(titan)

for titan in titans:
    if titan == "ken":
        print(f"{titan} - is a gypsy")
        break
    else:
        print(titan)

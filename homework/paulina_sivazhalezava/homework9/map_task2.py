temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31,
                33, 31, 30, 32, 30, 28, 24, 23]

hot_days_summer = list(filter(lambda temperature: temperature > 28, temperatures))

print(hot_days_summer)
print(min(hot_days_summer), max(hot_days_summer), round(sum(hot_days_summer)/len(hot_days_summer)))

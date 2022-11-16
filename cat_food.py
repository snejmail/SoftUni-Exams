cats_count = int(input())
group1_cats_count = 0
group2_cats_count = 0
group3_cats_count = 0
total_food = 0

for cat in range(cats_count):
    food_grams = float(input())
    total_food += food_grams

    if 100 <= food_grams < 200:
        group1_cats_count += 1
    elif 200 <= food_grams < 300:
        group2_cats_count += 1
    elif 300 <= food_grams < 400:
        group3_cats_count += 1

total_food_price = (total_food/1000) * 12.45
print(f"Group 1: {group1_cats_count} cats.")
print(f"Group 2: {group2_cats_count} cats.")
print(f"Group 3: {group3_cats_count} cats.")
print(f"Price for food per day: {total_food_price:.2f} lv.")



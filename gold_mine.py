locations_count = int(input())
total_gold_produced = 0

for location in range(locations_count):
    expected_gold_production_per_day = float(input())
    digging_days_count = int(input())

    for day in range(digging_days_count):
        daily_gold_production = float(input())
        total_gold_produced += daily_gold_production
        average_gold_production = total_gold_produced / digging_days_count
        diff = abs(expected_gold_production_per_day-average_gold_production)

    if average_gold_production >= expected_gold_production_per_day:
        print(f"Good job! Average gold per day: {average_gold_production:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")

    total_gold_produced = 0


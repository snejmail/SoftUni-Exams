from math import ceil, floor

paint_box_count = int(input())
wallpaper_rolls_count = int(input())
gloves_pair_price = float(input())
brush_price = float(input())

paint_box_price = 21.50
wallpaper_rolls_price = 5.20
gloves_pairs_count = ceil(wallpaper_rolls_count * 0.35)
brush_count = floor(paint_box_count * 0.48)

total_price = gloves_pair_price * gloves_pairs_count + brush_price * brush_count + paint_box_price * paint_box_count + wallpaper_rolls_price * wallpaper_rolls_count
delivery_price = total_price * (1/15)
print(f"This delivery will cost {delivery_price:.2f} lv.")
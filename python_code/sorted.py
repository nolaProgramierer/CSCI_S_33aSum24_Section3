# sorted(iterable, key=None, reverse=False)

nums = (43, 2, 99, 33, -4, 20)

composers = ["Beethoven", "Ravel", "Brahms", "Debussy", "Mahler", "Bruckner", "Mozart", "Bach", "Stravinsky"]

cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

# Sort these numbers
sorted_nums = sorted(nums)
print(f"1) {sorted_nums}")

print()
# Sort in reverse
rev_sorted_nums = sorted(nums, reverse=True)
print(f"2) {rev_sorted_nums}")

print()
# Sort with key function
sorted_by_word_length = sorted(composers, key=len, reverse=True)
print(f"3) {sorted_by_word_length}")

print()
# Sort with custom key function
sorted_cars = sorted(cars, key=lambda car: car['price'])
print(f"4) {sorted_cars}")


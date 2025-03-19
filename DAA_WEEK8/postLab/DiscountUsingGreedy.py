def max_discount(purchases, points):
    items = list(zip(purchases, points))

    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_discount = 0
    available_points = sum(points)

    for price, point_value in items:
        if available_points >= point_value:
            total_discount += price
            available_points -= point_value
        else:
            break

    return total_discount



purchases = [10, 20, 30]
points = [5, 8, 12]
print("Maximum Discount:", max_discount(purchases, points))

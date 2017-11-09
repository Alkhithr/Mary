import math

# 1. How many seconds are there in 42 minutes 42 seconds?

total_seconds = (42 * 60) + 42
print('1. There are {} seconds in 42 minutes and 42 seconds.'.format(total_seconds))

# 2. How many miles are there in 10 kilometres? Hint: there are 1.61 kilometres in a mile.

miles = 10 / 1.61
print('2. There are {} miles in 10 kilometers.'.format(miles))

# 3. If you run a 10 kilometre race in 42 minutes 42 seconds, what is your average
# pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

miles_per_second = miles / total_seconds
miles_per_minute = miles / total_seconds / 60
miles_per_hour = miles / total_seconds / 60 / 60
print('3. miles_per_second = {}, miles_per_minute = {}, miles_per_hour = {}'.format(miles_per_second, miles_per_minute, miles_per_hour))

# 4. We’ve seen that n = 42 is legal. What about 42 = n?

print('4. 42 = n will produce SyntaxError: can\'t assign to literal')

# 5. How about x = y = 1?

x = y = 1
print('5. x = y = 1 works: x = {}, y = {}'.format(x, y))

# 6. In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?

print('6. This line ends happily with a semi-colon;');

# 7. What if you put a period at the end of a statement?

print('7. Unless it\'s a = 2. one will get a syntax error')

# 8. In math notation you can multiply x and y like this: xy. What happens if you try that in Python?

x = 5
y = 6
print('8. Python will think xy is a variable and will throw NameError: name \'xy\' is not defined')

# 9. The volume of a sphere with radius r is 4/3πr3. What is the volume of a sphere with radius 5?

sphere_volume = 4/3 * math.pi * math.pow(5, 3)
print('9. the volume of a sphere with radius 5 is {}'.format(sphere_volume))


# 10. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy. What
# is the total wholesale cost for 60 copies?
book_price = 24.95 * 40 / 100
shipping_first = 3
shipping_rest = 0.75
total_wholesale_cost = (book_price + shipping_first) + (book_price + shipping_rest) * 59

print('10. The total wholesale cost for 60 copies is ${}'.format(total_wholesale_cost))

# 11. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then
# 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get
# home for breakfast?

start_time = '6:52:0'
mpm_easy = '0:8:15'
mpm_fast = '0:7:12'


def get_seconds(hms):
    hours, minutes, seconds = hms.split(':')
    total_seconds = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)
    return total_seconds


total_seconds = get_seconds(start_time) + (get_seconds(mpm_easy) * 2) + get_seconds(mpm_fast)
return_time = (total_seconds // 3600)
return_minutes = (total_seconds - (return_time * 3600)) // 60
return_seconds = (total_seconds - (return_time * 3600) - return_minutes * 60)
print('11. You\'ll get home from breakfast at {}:{}:{}'.format(return_time, return_minutes, return_seconds))

course = "Brandon's Course for Beginners"
print(course)

triple_test = '''
Hi man,

Welcome to the course

Thank you
'''

print(triple_test)

# Specific Characters
print(course[0])

# Negative will start from the end
print(course[-1])

# Return through a designated amount of characters
print(course[0:3])
print(course[1:])
print(course[:5])

# Copy strings
another = course[:]

name = 'Jennifer'
print(name[1:-1])

# formatted strings
first = 'John'
last = 'Smith'

# John [Smith] is a coder
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

print(len(course))
print(course.upper())
print(course.lower())

# METHODS are case sensitive
print(course.find('o'))

print(course.replace('Beginners', 'Absolute Beginners'))

print('Course' in course)
print('course' in course)
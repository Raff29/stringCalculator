from stringCalculator import Add

# Test with integers separated by a comma
test = Add("1,2,5")
print('\nAdd("1,2,5"): returns {} {}\n'.format(test, type(test)))

# Test with a new line input format
test = Add("1\n,2,3")
print('Add("1\\n,2,3"): returns {} {}'.format(test, type(test)))

test = Add("1,\n2,4")
print('Add("1,\\n2,4"): returns {} {}\n'.format(test, type(test)))

# Test with multiple custom delimiters
test = Add("//;\n1;3;4")
print('Add("//;\\n1;3;4"): returns {} {}'.format(test, type(test)))

test = Add("//$\n1$2$3")
print('Add("//$\\n1$2$3"): returns {} {}'.format(test, type(test)))

test = Add("//@\n2@3@8")
print('Add("//@\\n2@3@8"): returns {} {}\n'.format(test, type(test)))

# Test with negative integers
try:
    test = Add("1,-3,-4")
    print('Add("1,-3,-4"): returns {} {}'.format(test, type(test)))
except ValueError as e:
    print('Add("1,-3,-4"): returns {}\n'.format(e))

# Test with integers larger than 1001
test = Add("2,1001")
print('Add("2,1001"): returns {} {}\n'.format(test, type(test)))

test = Add("2,1001, 9999")
print('Add("2,1001, 9999"): returns {} {}\n'.format(test, type(test)))

# Test delimiters of arbitrary length
test = Add("//***\n1***2***3")
print('Add("//***\\n1***2***3"): returns {} {}\n'.format(test, type(test)))

test = Add("//@@@\n1@@@2@@@3")
print('Add("//@@@\\n1@@@2@@@3"): returns {} {}\n'.format(test, type(test)))

# Test with multiple delimiters
test = Add("//$,@\n1$2@3")
print('Add("//$,@\\n1$2@3"): returns {} {}\n'.format(test, type(test)))

test = Add("//@,?,?\n5@5?20?1")
print('Add("//@,?,?\\n5@5?20?1"): returns {} {}\n'.format(test, type(test)))

# Test with multiple delimiters of arbitrary length
test = Add("//$$,@@@,bbb\n1@@@2bbb3$$4")
print('Add("//$$,@@@,bbb\\n1@@@2bbb3$$4"): returns {} {}\n'.format(test, type(test)))

test = Add("//$$,@@@,bbb,???\n5???2bbb1$$9@@@2")
print('Add("///$$,@@@,bbb,???\\n5???2bbb1$$9@@@2"): returns {} {}\n'.format(test, type(test)))
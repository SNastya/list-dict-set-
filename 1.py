power_2_numbers = [ 2**i for i in range(1,8)]
print(power_2_numbers)

generated_set = {1 if i%5==0 else i for i in range(8,51)} #множества не могут содержать повторяющихся элементов, поэтому единица только одна
print((generated_set))

new_set = (generated_set.symmetric_difference(power_2_numbers))
print(new_set)

new_set = new_set & {i for i in range(34,121)}
print(new_set)

unicode_values = {i: chr(i) for i in new_set}
print(unicode_values)

    
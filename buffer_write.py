contact_15_in_bytes = bytes('15,New5,new5@new.com.br\n', 'latin_1')

# file = open('data/contact_test_2.csv')

with open('data/contact_test_2.csv', encoding='latin_1', mode='a+') as file_1:
    file_1.buffer.write(contact_15_in_bytes)

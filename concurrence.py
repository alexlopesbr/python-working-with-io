contact_15 = '15,New5,new5@new.com.br\n'
contact_16 = '16,New6,new6@new.com.br\n'

with open('data/contact_test_2.csv', encoding='latin_1', mode='a+') as file_1:
    file_1.write(contact_15)

with open('data/contact_test_2.csv', encoding='latin_1', mode='a+') as file_2:
    file_2.write(contact_16)

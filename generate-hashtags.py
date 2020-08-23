'''
This script will generate a randomized list of hashtags from three separate groups (large, medium, small) as defined in the text files indicated below. 

To use: python3 random-hashtag-group.py <NUMBER OF RESULTS>

Eric Fuerstenberg
8/22/2020
'''

import random
import sys
import yagmail

def process_file(file):
    with open(file, "r") as file:
        newlist = ''
        for i in file:
            newlist += i
        #print(newlist)
        split_list = newlist.split()
        #print(split_list)
    return split_list
        
def generate_list(large, medium, small):
    full_list = []

    l_list = random.sample(large, 5)
    m_list = random.sample(medium, 10)
    s_list = random.sample(small, 15)

    for i in l_list:
        full_list.append(i)
    for i in m_list:
        full_list.append(i)
    for i in s_list:
        full_list.append(i)

    hashtags = ' '.join(full_list)
    return hashtags


def send_mail(message):
    with yagmail.SMTP(sender_email) as yag:
        yag.send(receiver_email, 'Hashtag Shuffler for this week', message)


if __name__ == '__main__':
    
    files = ["input/large.txt", "input/medium.txt", "input/small.txt"]
    sender_email = "automation.ericfuerstenberg@gmail.com"  # Enter your address
    receiver_email = "ericfuerstenberg@gmail.com"  # Enter receiver address
    message = ''

    count = int(sys.argv[1])

    print('Processing files..')
    large = process_file(files[0])
    medium = process_file(files[1])
    small = process_file(files[2])

    for i in range(count):
        output = generate_list(large, medium, small)
        message += output + '\n' + '\n'
    
    print('Sending email..')
    send_mail(message)

    print('Sent!')
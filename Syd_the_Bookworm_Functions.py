# This imports some extra code, making it available to use later
from random import choice
import string

# This section includes variables that define a collection of input and output things our chatbot can say and respond to
greetings_in = ['Hello', 'Hi', 'Hey', 'Hola', 'Welcome', 'Bonjour', 'Greetings', 'What\'s up?']
greetings_out = ['Hello I\'m Syd the Bookworm, how can I help you?', \
                 'Hey I\'m Syd the Bookworm, what book could I suggest to you?', \
                 'Hello I\'m Syd the Bookworm, what do you feel like reading today?', \
                 'Hey I\'m Syd the Bookworm, it\'s a beautiful day to open up a book!'] 

user_in = ['I\'m not sure', \
           'I don\'t know', \
           'Not sure', \
           'I would like to read a new book', \
           'Book suggestions please', \
           'I feel like reading about a specific author',\
           'Could you find me an author to check out?']
user_out = ['Of course! What genre do you feel like reading?', \
            'Okay sounds good! What genre do you feel like reading?', \
            'Let me help you out! What genre do you feel like reading?',\
            'Would you like me to suggest an author?', \
            'I could suggest an author.']
            
reaction = ['Cool', 'Thank you', 'Thanks', 'Awesome!', 'Woah', 'Wow', 'Okay', 'Nice']
response = ['No problem, can I help you with anything else? :)']

yes_input = ['Yeah', 'Yes', 'Yes please', 'Yeah actually', 'Okay', 'Yup', 'Ya', 'Please', 'Actually yeah']
no_input = ['No', 'Nah', 'No thanks I\'m good', 'No thanks', 'I\'m fine', 'Naw', 'Nope']

unknown = ['Huh?', 'Sorry I don\'t think I understand.', 'Can you try again?', 'Sorry what?']

goodbye_msg = ['Okay, hate to see you go!']



# This section includes the different genre libraries and books included in them as well as a list of authors
Horror_library = ['The Institute by Stephen King',\
                  'The Woman in Black by Susan Hill',\
                  'The Shining by Stephen King',\
                  'The Luminous Dead by Caitlin Starling',\
                  'The Tenth Girl by Sara Faring']
Fiction_library = ['A Thousand Splendid Suns by Khaled Hosseini',\
                   'Daisy Jones and The Six by Taylor Jenkins Reid',\
                   'Kindred by Octavia Butler',\
                   'The Kite Runner by Khaled Hosseini',\
                   'All the Light We Cannot See by Anthony Doerr']
Dystopian_library = ['Fahrenheit 451 by Ray Bradbury',\
                     'The Road by Cormac McCarthy',\
                     'Future Home of the Living God by Louise Erdrich',\
                     'Parable of the Sower by Octavia Butler',\
                     'The Stand by Stephen King']
Comedy_library = ['Dear Girls: Intimate Tales, Untold Secrets & Advice for Living Your Best Life by Ali Wong',\
                  'Born a Crime by Trevor Noah',\
                  'It\'s Not You It\'s Him: An absolutely hilarious and feel good romantic comedy by Sophie Ranald',\
                  'Stay Sexy and Don\'t Get Murdered by Georgia Hardstark and Karen Kilgariff',\
                  'Wishful Drinking by Carrie Fisher and Joshua Ravetch']            
Feminism_library = ['Fifty Million Rising: The New Generation of Working Women Transforming the Muslim World by Saadia Zahidi',\
                    'Bad Feminist: Essays by Roxane Gay',\
                    'We Should All Be Feminists by Chimamanda Ngozi Adichie',\
                    'Men Explain Things to Me by Rebecca Solnit',\
                    'The Beauty Myth by Naomi Wolf']

Authors = ['Octavia Butler',\
           'Albert Camus',\
           'Ocean Vuong',\
           'Khaled Hosseini',\
           'Stephen King',\
           'Jane Austen',\
           'Ernest Hemingway',\
           'J.K. Rowling',\
           'George Orwell',\
           'Paulo Coehlo',\
           'Toni Morrison',\
           'Kim Fu',\
           'Akwaeke Emezi',\
           'Elizabeth Acevedo',\
           'Zadie Smith',\
           'F. Scott Fitzgerald',\
           'Carson McCullers',\
           'Percival Everett',\
           'Lynda Barry',\
           'Alice Munro']



# Code from the A3 Chatbot

# Determines if the input from the user is a question
def is_question(input_string): 
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output


# Prepares the text
def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list


# Removes punctuation of input text
def remove_punctuation(input_string):
    out_string = ''
    
    for item in input_string:
        if item not in string.punctuation:
            out_string += item
  
    return out_string


# Selector
def selector(input_list, check_list, return_list):
    output = None
    
    for item in range(len(input_list)):
        if input_list[item] in check_list:
            output = random.choice(return_list)
            break 
        
    return output 


# Ends the chat
def end_chat(input_list):
    if 'quit' in input_list:
        output = True
    else:
        output = False
    return output



# Function for the chatbot 

# Returns a random book based on the specified genre
def choose_book(input_string):
    """Identifies if the input from the user asked a specific genre and returns a book associated with that genre"""
        
    suggested_phrase = 'I suggest you read this: '
       
    if 'horror' in input_string:
        return suggested_phrase + random.choice(Horror_library) 
    if 'fiction' in input_string:
        return suggested_phrase + random.choice(Fiction_library)
    if 'dystopian' in input_string:
        return suggested_phrase + random.choice(Dystopian_library)
    if 'feminism' in input_string:
        return suggested_phrase + random.choice(Feminism_library)
    if 'comedy' in input_string:
        return suggested_phrase + random.choice(Comedy_library)
    else:
        return random.choice(unknown)

# Returns a random author 
def choose_author(input_string):
    """Identifies if the input from the user asked about an author and returns a random author"""
    
    suggested_author = 'I suggest you check this author out: '
    
    if 'author' in input_string:
        return suggested_author + random.choice(Authors)

# Checks if the input asks about a book   
def is_book(input_string): 
    if 'book' in input_string:
        output = True
    else:
        output = False
    
    return output

# Checks if the input asks about an author
def is_author(input_string):
    if 'author' in input_string:
        output = True
    else:
        output = False
    return output

# Checks if the Bot received a no response
def no_response(input_string):
    item = []
    
    if no_input[item] in input_string:
        output = True
    else:
        output = False
    return output



# Main function to run the chatbot
import random

def activate_chatbot():
    """Main function to run the chatbot"""
    
    chat = True
    while chat:
        
        msg = input('INPUT :\t')
        out_msg = None
        input_string = ''
        prepare = prepare_text(input_string)
        remove = remove_punctuation(input_string)

        # Check if the input is a question
        question = is_question(msg)
        
        # Check for topics that the chatbot intends to answer to 
        if not out_msg:
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            #print(selector(msg, greetings_in, greetings_out))
            #print(selector(msg, user_in, user_out))
            #print(msg)
            if selector(msg.split(), greetings_in, greetings_out) != None:
                outs += greetings_out
            elif selector(msg.split(), user_in, user_out) != None:
                outs += user_out
            elif is_book(msg):
                outs.append(choose_book(msg))
            elif is_author(msg):
                outs.append(choose_author(msg))
            elif selector(msg.split(), reaction, response) != None:
                outs += response
            elif selector(msg.split(), yes_input, user_out) != None:
                outs += user_out
            elif selector(msg.split(), no_input, goodbye_msg) != None:
                outs += goodbye_msg
                
            if len(outs) != 0:
                out_msg = random.choice(outs)
            
        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = question

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(unknown)
            
        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye, have a fun read!'
            chat = False
        print('OUTPUT:', out_msg)
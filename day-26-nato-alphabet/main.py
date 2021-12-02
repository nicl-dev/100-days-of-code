import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#  Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
is_running = True
while is_running:
    try:
        user_input = input("Please type a word.\n")
        phonetic = [nato_dict[letter] for letter in user_input.upper()]
        is_running = False
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
    else:
        print(phonetic)

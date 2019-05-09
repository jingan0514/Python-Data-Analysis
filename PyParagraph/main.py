import os
import re

text1 = os.path.join("raw_data", "paragraph_1.txt")
text2 = os.path.join("raw_data", "paragraph_2.txt")

result = []

def paragraph_analysis(file_path, rule):
    f = open(file_path, "r")
    text = f.read()
    split_text = re.split(rule, text)
    sentence_count = len(split_text)
    result = []
    result.append(sentence_count)
    word_count = 0
    letter = []
    letter_count = 0
    

    for sentence in split_text:
        #word = sentence.replace(".", "").replace(",", "").replace("(", "").replace(")", "").split(" ")
        clean_sentence = re.sub("[,.?!\'\"\(\)]", "", sentence)
        word = re.split("\s", clean_sentence)
        word_count += len(word)

        for c in word:
            letter_count += len(list(c))

    result.append(word_count)
    result.append(letter_count)
    average_letter = round(result[2] / result[1], 1)
    average_word = result[1] / result[0]

    
    print("Paragraph Analysis")
    print("------------------")
    print(f"Approximate Word Count: {result[1]}")
    print(f"Approximate Sentence Count: {result[0]}")
    print(f"Average Letter Count: {average_letter}")
    print(f"Average Sentence Length: {average_word}")
    print("")

rule1 = "(?<=[.!?\"]) +"
paragraph_analysis(text1, rule1)

rule2 = "(?<=[.!?\"])\n+"
paragraph_analysis(text2, rule2)
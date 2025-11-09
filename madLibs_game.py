import time

print("########## MadLibs Game ##########")

adjective1 = input("Enter an adjective: ")
print("##################################")
adjective2 = input("Enter another adjective: ")
print("##################################")
noun1 = input("Enter a noun: ")
print("##################################")
noun2 = input("Enter another noun: ")
print("##################################")
adverb = input("Enter an adverb: ")
print("##################################")
adverb2 = input("Enter another adverb: ")
print("##################################")

first_sentence = f"I was {adjective1} down the {noun1} {adverb}."
second_sentence = f"I saw a {adjective2} {noun2}."
third_sentence = f"{noun2} looked very {adjective2}."
fourth_sentence = f"I {adverb2} continued down the {noun1}."
fifth_sentence = "############# The end #############"

print(first_sentence)
print(second_sentence)
print(third_sentence)
print(fourth_sentence)

time.sleep(6)

print("##################################")
print(fifth_sentence)
print("##################################")

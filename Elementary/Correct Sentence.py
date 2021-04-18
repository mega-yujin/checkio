def correct_sentence(sentence: str) -> str:
    sentence = sentence[0].capitalize() + sentence[1:]
    return sentence if sentence[-1] == '.' else sentence + "."


print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, Friends"))
print(correct_sentence("Greetings, friends."))

assert correct_sentence("hi") == "Hi."
assert correct_sentence("welcome to New York") == "Welcome to New York."

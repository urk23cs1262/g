from ollama_helper import ask_ollama

file = open("health.txt", "r")
text = file.read()
file.close()

questions = input("Enetr your health question: ")
prompt = f"Answer this health question: {questions}. Using this information {text}. Do not prescribe medicines"

answer = ask_ollama(prompt)

print("\nAnswer:- ")
print(answer)

print("\nTHANK YOU")
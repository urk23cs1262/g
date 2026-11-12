from ollama_helper import ask_ollama

file = open("ai.txt", "r")
text = file.read()
file.close()

print("Document:- ")
print(text)

prompt1=f"Summarize this document {text}"
summary = ask_ollama(prompt1)

print("\nSummary:- ")
print(summary)

question = input("\nEnter your question: ")

prompt2 = f"Answer only using this documnet {text}. Question {question}"
answer = ask_ollama(prompt2)

print("\nAnswer:-")
print(answer)

file = open("result.txt", "w")
file.write(answer)
file.close()

print("\nResult was saved successfully")
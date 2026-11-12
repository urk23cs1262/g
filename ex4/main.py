from ollama_helper import ask_ollama

interest = input("Enter your interest: ")
level = input("\nEnter your level: ")

prompt = f"Recommend 3 courses for {interest} at {level} level"

answer = ask_ollama(prompt)

print("\nRecommended Courses:- ")
print(answer)
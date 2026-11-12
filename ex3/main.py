from ollama_helper import ask_ollama

email = input("Enter your email: ")
tone = input("\nEnter your email tone: ")

prompt = f"write email in this {tone} tone: {email}"

reply = ask_ollama(prompt)

print("\nGenerated email: ")
print(reply)

file = open("email.txt", "w")
file.write(reply)
file.close()

print("Email was saved successfully")
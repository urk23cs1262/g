from ollama_helper import ask_ollama
import csv

print("WELCOME TO ONLINE SHOPPING CHATBOT:-")

with open("products.csv", "r") as file:
    products = list(csv.DictReader(file))

print("\nAvailable Products: ")

for p in products:
    print(p["Product"], "-", "Rs.",p["Price"])

question = input("\nEnter your questions: ")

prompt = f"Answer using only these Products {products}. Question: {question}"

answer = ask_ollama(prompt)

print("\nCHATBOT: ", answer)
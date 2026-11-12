from ollama_helper import ask_ollama

topic = input("Enter your blog topic: ")
style = input("\nEnter your blog style: ")

prompt = f"Write a blog about {topic} with {style} style"

blog = ask_ollama(prompt)

print("\nGenerated Blog Text: ")
print(blog)

file = open("blog.txt", "w")
file.write(blog)
file.close()

print("\nBlog saved successfully")
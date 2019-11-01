from sys import argv

script, user_name, last_name = argv
prompt = 'Answer : '

print(f"Hi {user_name}, I'm in the {script} script ")
print("I'd like to ask you a few questions.")

likes = input((f"Do you like me {user_name}?\n") + prompt)

lives = input((f"Where do you live {user_name}?\n") + prompt)

computer = input((f"What kind of computer do you have {last_name}?\n") + prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
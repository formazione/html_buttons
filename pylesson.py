import os


counter = 0
b1 = ""

def create_button(question, answer):
	global counter, b1
	
	button = f"""
	<button id="b{counter}" class="button-55" onclick="button_clicked('inspect{counter}', '{answer}')">
	{question}
	</button><br><br>
	<div id="inspect{counter}">...</div>
	<br>
	"""
	counter += 1
	b1 += button
	return button

def start():
	with open("template_54.html") as file:
		html = file.read()

	html = html.replace("[button]", b1)

	with open("example.html", "w") as file:
		file.write(html)

	os.startfile("example.html")

# =========== QUESTIONS ===================
create_button("How ho you feel", "good")
create_button("What's the time", "11 o clock")
create_button("Where is Rome", "In Italy")

# ====================================== END
start()

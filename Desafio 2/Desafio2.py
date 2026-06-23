import subprocess


nome = str(input("Digite seu nome"))
email = str(input("Digite seu email"))

subprocess.run(["git", "config", "--global", "user.name", nome])
subprocess.run(["git", "config", "--global", "user.email", email])


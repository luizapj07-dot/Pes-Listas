from deep_translator import GoogleTranslator
texto = "Ola, mundo!"
traducao = GoogleTranslator(source="pt", target="en").translate(texto)
print(texto, traducao)
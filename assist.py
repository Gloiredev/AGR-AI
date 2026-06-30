import streamlit as Agr
from modules.conversation import discuter

Agr.title("Assistant Personnel")

message = Agr.text_input("parle à AGR...")

if Agr.button("envoyer"):
	if message.strip():
		reponse = discuter(message)
		Agr.write(reponse)
	else :
		Agr.warning("ecrivez à AGR avant d'envoyer")
		
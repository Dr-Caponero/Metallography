import base64
import streamlit as st


main_bg2 = "materiais.png"

# def set_bg_hack(main_bg):
#     '''
#     A function to unpack an image from root folder and set as bg.
 
#     Returns
#     -------
#     The background.
#     '''
#     # set bg name
#     main_bg_ext = "png"
        
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )
    
# set_bg_hack(main_bg2)

st.image(main_bg2)


""" 
**Bem-vindo ao Aplicativo de Aprendizado de Inteligência Artificial! ✨**


Olá, pessoal! 👋

Este é o **aplicativo online** que vamos usar nas disciplinas de **Metalografia** e **Tratamentos Térmicos** do **IFBA 2025**. 

Aqui, vamos reunir conteúdos e ferramentas que construiremos durante as aulas, e ele será o ponto central para **compartilhar materiais** e **novidades** da disciplina.

Tudo que vocês precisarem estará disponível nessa página, então fiquem ligados! 



**Lembrem-se:** com tecnologia GPT, tudo pode estar errado, então usem com atenção. Qualquer coisa esquisita que acontecem, **relate!** ⚠️

Se tiverem sugestões ou dúvidas, me chamem! Espero que tenham todos uma ótima experiência.

Bora aprender! 💪

Prof. Jeff  

"""


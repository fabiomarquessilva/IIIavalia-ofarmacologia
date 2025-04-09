import streamlit as st
import random

# Título institucional
st.title("🧪 III Avaliação - Disciplina de Farmacologia")
st.markdown("""
**UNIVERSIDADE FEDERAL DE CAMPINA GRANDE**  
**CENTRO DE FORMAÇÃO DE PROFESSORES**  
**UNIDADE ACADÊMICA DE ENFERMAGEM**  
DISCIPLINA DE FARMACOLOGIA  
III AVALIAÇÃO
""")

st.subheader("Jogo Interativo: Anti-hipertensivos")
st.markdown("Responda corretamente para desbloquear a próxima pergunta. Erros adicionam uma nova questão à fila. Máximo de 20 perguntas.")

questions = [
    ("A _______ atua como agonista α2-central, reduzindo a atividade simpática e a pressão arterial, mas sua interrupção abrupta pode causar hipertensão de rebote.", "clonidina"),
    ("Os _______ são frequentemente indicados como terapia inicial para hipertensão devido ao seu baixo custo, eficácia e efeito protetor cardiovascular.", "diuréticos"),
    ("A administração de um diurético _______ pode resultar em hipopotassemia e hiperglicemia como efeitos adversos comuns.", "tiazídico"),
    ("A _______ é uma substância fundamental para a ativação do sistema renina-angiotensina-aldosterona.", "renina"),
    ("Os fármacos conhecidos como _______ bloqueiam os efeitos da angiotensina II nos receptores AT1.", "bras"),
    ("A _______ é uma condição onde a pressão permanece elevada apesar do uso de três fármacos, incluindo um diurético.", "hipertensão resistente"),
    ("A _______ pode ser causada pelo uso de diuréticos tiazídicos e deve ser monitorada em pacientes com risco de diabetes.", "hiperglicemia"),
    ("O bloqueio de receptores α1 pela _______ pode levar à hipotensão postural após a primeira dose.", "prazosina"),
    ("A angiotensina II promove a _______ de sódio nos túbulos renais.", "reabsorção"),
    ("A ativação dos _______ promove resposta rápida à queda de pressão arterial.", "barorreceptores"),
    ("Um paciente em uso de hidroclorotiazida e enalapril apresenta fraqueza e potássio de 3,0 mEq/L. Isso indica _______.", "hipopotassemia"),
    ("Tosse seca como efeito adverso de IECA está relacionada à inibição da _______.", "iecas"),
    ("A _______ estimula reabsorção de sódio e excreção de potássio.", "aldosterona"),
    ("O uso de _______ é contraindicado em asmáticos pela broncoconstrição reflexa.", "β-bloqueadores"),
    ("O fármaco mais indicado para hipertensão gestacional, apesar da sedação, é a _______.", "metildopa"),
    ("A _______ é preferida na via sublingual para crises hipertensivas.", "nitroglicerina")
]

# Inicialização
if 'fila' not in st.session_state:
    st.session_state.fila = random.sample(questions, 5)
    st.session_state.respondidas = []
    st.session_state.maximo = 20
    st.session_state.index = 0
    st.session_state.finalizado = False

# Mostrar se ainda houver perguntas
if not st.session_state.finalizado and st.session_state.fila:
    pergunta, resposta = st.session_state.fila[0]
    st.write(f"**Pergunta:** {pergunta}")
    user_input = st.text_input("Sua resposta (minúsculas, sem acento):", key=f"resposta_{len(st.session_state.respondidas)}")
    
    if st.button("Enviar resposta"):
        correta = user_input.strip().lower() == resposta
        st.session_state.respondidas.append((pergunta, user_input, correta))
        st.session_state.fila.pop(0)

        if not correta and len(st.session_state.respondidas) < st.session_state.maximo:
            extras = [q for q in questions if q not in st.session_state.fila and q not in [r[:2] for r in st.session_state.respondidas]]
            if extras:
                st.session_state.fila.append(random.choice(extras))

        if not st.session_state.fila:
            st.session_state.finalizado = True

        st.experimental_rerun()

elif st.session_state.finalizado or not st.session_state.fila:
    st.success(f"🏁 Fim da avaliação! Você respondeu {len(st.session_state.respondidas)} questões.")
    acertos = sum(1 for q in st.session_state.respondidas if q[2])
    st.markdown(f"**Acertos:** {acertos} de {len(st.session_state.respondidas)}")

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

# Banco de perguntas
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

# Inicialização de estados
if 'queue' not in st.session_state:
    st.session_state.queue = random.sample(questions, 5)
    st.session_state.answered = []
    st.session_state.max_questions = 20
    st.session_state.index = 0
    st.session_state.feedback = ""

# Se ainda houver perguntas
if st.session_state.queue:
    q, a = st.session_state.queue[0]
    st.write(f"**Pergunta:** {q}")

    user_answer = st.text_input("Sua resposta (minúsculas, sem acento):", key="user_input")

    if st.button("Enviar resposta"):
        if user_answer.strip().lower() == a:
            st.success("✅ Correto!")
            st.session_state.answered.append((q, user_answer))
            st.session_state.queue.pop(0)
        else:
            st.error(f"❌ Errado! A resposta correta era: {a}")
            st.session_state.answered.append((q, user_answer))
            if len(st.session_state.answered) < st.session_state.max_questions:
                extras = [x for x in questions if x not in st.session_state.queue and x not in st.session_state.answered]
                if extras:
                    st.session_state.queue.append(random.choice(extras))
            st.session_state.queue.pop(0)

        # Limpa a entrada para a próxima questão
        st.experimental_set_query_params()
        st.experimental_rerun()

    st.markdown(f"**Progresso:** {len(st.session_state.answered)} respondidas • {len(st.session_state.queue)} restantes")

else:
    st.success(f"🏁 Fim da avaliação! Você respondeu {len(st.session_state.answered)} questões.")

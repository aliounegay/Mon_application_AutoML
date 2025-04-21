import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Data Workers", layout="wide")

# CSS personnalisé pour les boutons et la mise en page
st.markdown("""
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9f9f9;
        padding: 10px;
    }
    .header-container img {
        max-height: 150px;
        object-fit: cover;
        border-radius: 10px;
    }
    .service-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        background-color: #fff;
        text-align: center;
    }
    .service-box h3 {
        color: #333;
        margin-bottom: 10px;
    }
    .service-box p {
        color: #666;
        font-size: 14px;
    }
    .service-box .emoji {
        font-size: 40px;
        margin-bottom: 10px;
    }
    .project-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        background-color: #fff;
        text-align: center;
    }
    .project-box h3 {
        color: #333;
        margin-bottom: 10px;
    }
    .project-box p {
        color: #666;
        font-size: 14px;
    }
    .project-box a {
        color: #f25287;
        text-decoration: none;
        font-weight: bold;
    }
    .project-box img {
        max-width: 100%;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation dans la barre latérale
page = st.sidebar.radio("Navigation", ["Les services que je propose", "À propos de moi", "Mes projets"])

if page == "Les services que je propose":
    # Section d'en-tête
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.image("logogo.JPG", caption="AI & ClairData Solutions", use_container_width=True)
    with col2:
        st.markdown("<h1 style='text-align: center; color: #333;'>Data Scientist, Consultant, Business Analyst, Shiny et Streamlit Developper </h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #f25287;'>La donnée au service de votre croissance</h2>", unsafe_allow_html=True)
    with col3:
        st.image("dv_lottery.jpg", caption="Alioune Gaye", use_container_width=True)

    # Section Services
    st.markdown("Je propose des services de pointe en intelligence artificielle et en science des données. Ma mission est d'accompagner les entreprises dans leur prise de décision en exploitant la puissance des données grâce à des technologies avancées de Machine Learning, de Deep Learning et d'analytique.")
    st.markdown("### Services")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="service-box">
            <div class="emoji">📈</div>
            <h3>Analyse exploratoire de données</h3>
            <p>Nettoyage, structuration, et analyse descriptive.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="service-box">
            <div class="emoji">🤖</div>
            <h3>Modélisation prédictive</h3>
            <p>Mise en œuvre d'algorithmes de Machine Learning et de Deep Learning pour réaliser des prédictions adaptées aux besoins des entreprises.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="service-box">
            <div class="emoji">⚙️</div>
            <h3>Automatisation des processus</h3>
            <p>Création d'outils pour automatiser des tâches répétitives.</p>
        </div>
        """, unsafe_allow_html=True)

    # Deuxième ligne de services
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="service-box">
            <div class="emoji">📊</div>
            <h3>Création de tableaux de bord</h3>
            <p>Développement de dashboards interactifs pour le suivi des KPI.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="service-box">
            <div class="emoji">🗂️</div>
            <h3>Gestion des bases de données</h3>
            <p>La gestion et la structuration des bases de données.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="service-box">
            <div class="emoji">🎓</div>
            <h3>Formations</h3>
            <p>Offrir des formations sur l'application de l'intelligence artificielle et des méthodes statistiques.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "À propos de moi":
    # Section "À propos de moi"
    st.markdown("<h1 style='text-align: center; color: #333;'>À propos de moi</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("dv_lottery.jpg", use_container_width=True)  # Remplacer par l'image réelle
    with col2:
        st.markdown("""
        Analyste de données expérimenté et statisticien, je suis compétent en gestion de projet, suivi et évaluation, ainsi qu'en gestion de bases de données.
        Je suis impliqué dans la collecte de données d'enquête sur le terrain, le suivi des enquêtes en cours et les indicateurs de performance KPI. Mon expertise comprend 
        la création de tableaux de bord, la modélisation statistique et la structuration de bases de données. Proactif, je m'efforce d'innover des solutions pour l'analyse de données 
        et les processus de prise de décision.
        """)

    # Section "Éducation"
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Éducation</h2>", unsafe_allow_html=True)
    st.markdown("**Statistique, Modélisation et Science des données** diplômé à l'Université Claude Bernard Lyon1 - Bac +5.")

    # Section "Compétences"
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Comportemental</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Bonne communication orale et écrite, travail en équipe et de maniére indépendante**  
    - **Compétences organisationnelles, autonomie, innovation, rigueur**  
    - **Sociable, professionnel, partage de connaissances**
    """)

    # Section "Techniques"
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Techniques</h2>", unsafe_allow_html=True)
    st.markdown("""
    - **Machine Learning**
    - **Deep Learning**
    - **Fouille de données**
    - **Traitement du langage naturel (NLP)** 
    - **Text mining** 
    - **Vision par ordinateur** 
    - **Mathématiques, Statistique, Probabilités**
    - **Analyse de données**
    - **Séries temporelles** 
    - **Spectrométrie de masse**
    - **Cloud (Azure)**
    -**PHP, css, Html**
    - **GitHub**
    - **Git** 
    - **Django** 
    - **Scrapy**
    """)

    # Section "Programmation"
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Langages de programmations</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("python_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col2:
        st.image("r_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col3:
        st.image("stata_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col4:
        st.image("C++.PNG", use_container_width=True)  # Remplacer par l'image réelle
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Visualisation</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("power_bi_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col2:
        st.image("excel_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col3:
        st.image("streamlit.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col4:
        st.image("shiny.PNG", use_container_width=True)  # Remplacer par l'image réelle

    # Section "Bases de données"
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Gestion des bases de données</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image("mysql_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle
    with col2:
        st.image("sql_server_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle

    # Section "Bureautique"
    st.markdown("<h2 style='text-align: center; color: #f25287;'>Bureautique</h2>", unsafe_allow_html=True)
    st.image("tableau_icon.PNG", use_container_width=True)  # Remplacer par l'image réelle

elif page == "Mes projets":
    st.markdown("<h1 style='text-align: center; color: #333;'>Mes Projets</h1>", unsafe_allow_html=True)

    # Projets
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Alzeimer.PNG", caption="Détection de la Maladie d'Alzheimer", use_container_width=True)
        st.markdown("""
        <div class="project-box">
            <h3>Détection de la Maladie d'Alzheimer</h3>
            <p>Un projet utilisant des modèles de Deep Learning (VGG19, ResNet50) pour détecter différents stades de démence à partir d'IRM cérébrales.</p>
            #<a href="https://risquedecredits-clients.streamlit.app/">Accéder à l'application</a><br>
            <a href="https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FStagiaire2023GayeAlioune%2FMon_application_AutoML%2Frefs%2Fheads%2Fmaster%2FDetection_Alzheimer_Deep_Learning.docx&wdOrigin=BROWSELINK">Télécharger le rapport</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("cancer.PNG", caption="Détection du Cancer du Sein", use_container_width=True)
        st.markdown("""
        <div class="project-box">
            <h3>Détection du Cancer du Sein</h3>
            <p>Analyse des images échographiques pour classifier les masses mammaires en trois catégories : bénin, malin, et normal.</p>
            #<a href="https://example.com/cancer">Accéder à l'application</a><br>
            <a href="https://github.com/Stagiaire2023GayeAlioune/Mon_application_AutoML/blob/master/Rapport_Cancer_du_sein.pdf">Télécharger le rapport</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.image("carte.PNG", caption="Détection de Fraude sur les Cartes", use_container_width=True)
        st.markdown("""
        <div class="project-box">
            <h3>Détection de Fraude sur les Cartes Bancaires</h3>
            <p>Classification des transactions bancaires pour détecter les fraudes en utilisant des algorithmes avancés.</p>
            #<a href="https://example.com/fraude">Accéder à l'application</a><br>
            <a href="https://github.com/Stagiaire2023GayeAlioune/Mon_application_AutoML/blob/master/Rapport_detection_fraude.pdf">Télécharger le rapport</a>
        </div>
        """, unsafe_allow_html=True)

    # Deuxième ligne de projets
    col1, col2 = st.columns(2)

    with col1:
        st.image("credi.jpg", caption="Analyse des Risques de Crédit", use_container_width=True)
        st.markdown("""
        <div class="project-box">
            <h3>Analyse des Risques de Crédit</h3>
            <p>Développement d'une solution pour évaluer et anticiper les risques de crédit en utilisant des techniques de machine learning.</p>
            <a href="https://risquedecredits-clients.streamlit.app/">Accéder à l'application</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("RH.PNG", caption="Tableau de Bord RH", use_container_width=True)
        st.markdown("""
        <div class="project-box">
            <h3>Tableau de Bord RH</h3>
            <p>Création d'un tableau de bord interactif pour analyser les données RH, incluant l'attrition, la démographie et la performance.</p>
            <a href="https://application-tableau-de-bord-analyse-rh-gaye-alioune.streamlit.app/">Accéder à l'application</a>
        </div>
        """, unsafe_allow_html=True)

# Pied de page
st.markdown("---")
st.markdown("""
<p style='text-align: center;'>
    Mes contacts:<br>
    <a href='https://www.linkedin.com/in/alioune-gaye-1a5161172/' target='_blank' style='margin-right: 15px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' alt='LinkedIn' style='width:20px; vertical-align:middle;'> LinkedIn
    </a>
    <a href='tel:+33763556982' style='margin-right: 15px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/6/6c/Phone_icon.png' alt='Phone' style='width:20px; vertical-align:middle;'> 0763556982
    </a>
    <a href='mailto:aliounegaye911@gmail.com'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/2/27/Android_Email_4.4_Icon.png' alt='Email' style='width:20px; vertical-align:middle;'> aliounegaye911@gmail.com
    </a> <br>
    © 2025 Data Workers; GAYE ALIOUNE.
</p>
""", unsafe_allow_html=True)

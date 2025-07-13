# This script reads a FODA analysis from a DOCX file and classifies a team member's role based on keywords.
# It uses the python-docx library to read the DOCX file and processes the text to determine the most suitable roles.
from docx import Document

# Define the keywords associated with each role
roles_keywords = {
    "CEO": ["liderazgo", "estrategia", "organización", "negociación", "habilidad social", "confianza", "juicio"],
    "CTO": ["arquitectura", "tecnología", "decisiones técnicas", "escalabilidad", "proyecto de apis"],
    "Backend Developer": ["python", "node.js", "base de datos", "api", "servidor", "desarrollo backend"],
    "Frontend Developer": ["react", "javascript", "html", "css", "interfaz", "diseño frontend"],
    "QA / Analista": ["analítico", "documentación", "pruebas", "organización", "detalle"],
    "Integrador de servicios": ["api", "whatsapp", "integración", "webhook"],
    "UI/UX Designer": ["figma", "diseño", "usuario", "experiencia", "interfaz"],
    "Soporte Técnico": ["instalación", "mantenimiento", "capacitación", "soporte"],
    "Marketing / Comunicación": ["publicidad", "marketing", "redes", "contenido", "comunicación", "habilidad social"]
}

# Function to read the FODA analysis from a DOCX file
def leer_foda_desde_docx(ruta_archivo):
    # Reads the FODA analysis from a DOCX file and returns the text in lowercase.
    doc = Document(ruta_archivo)
    texto_completo = "" # Initialize an empty string to hold the text
    # Iterate through each paragraph in the document and append its text to the string
    for p in doc.paragraphs:
        texto_completo += p.text + " "
    return texto_completo.lower()

# Function to classify a team member based on the FODA analysis text preprocessed.
def clasificar_integrante(nombre, foda_texto):
    # Returns the top 3 roles based on the presence of keywords in the FODA analysis text.
    puntuacion = {rol: 0 for rol in roles_keywords}
    for rol, keywords in roles_keywords.items():
        for kw in keywords:
            if kw in foda_texto:
                puntuacion[rol] += 1
    mejor_rol = sorted(puntuacion.items(), key=lambda x: x[1], reverse=True)
    return nombre, mejor_rol[:3]  # Top 3 roles

# Main execution
# This part reads the FODA analysis from a DOCX file and classifies a team member based on the analysis.
if __name__ == "__main__":
    # I am using Kenny García as an example team member.
    ruta_archivo = "c:\\Users\\Lizzy.Mejia\\Downloads\\KennyGarcia.docx"  
    foda_texto = leer_foda_desde_docx(ruta_archivo)
    nombre, roles = clasificar_integrante("Kenny García", foda_texto)
    print(f"Clasificación para {nombre}:")
    for rol, puntaje in roles:
        print(f" - {rol} (puntaje: {puntaje})")


# Even though the code works. I could be authomated to read the file path from a configuration or user input.
# This would make it more flexible and user-friendly. 
# I'll add it later 

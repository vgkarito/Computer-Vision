from deepface import DeepFace
import os

# Carpetas
DATASET_PATH = "dataset_jpg"
INPUT_IMAGE = os.path.join(os.getcwd(), "entrada", "prueba_real.jpg")

# Mensajes por persona
ACTIONS = {
    "Carolina": "Bienvenida Carolina, encendiendo modo ejercicio 💪",
    "Manuel": "Hola Manuel, luces cálidas activadas 🟠",
    "Santi": "Hola Santi, activando modo caricaturas 🧸",
}

def extract_person_name(identity_path: str) -> str:
    # identity_path suele ser algo como: dataset_jpg/Santi/santi3.jpg
    # o con rutas completas. Normalizamos y tomamos la carpeta padre.
    norm = os.path.normpath(identity_path)
    parts = norm.split(os.sep)
    if len(parts) >= 2:
        return parts[-2]  # carpeta = nombre de persona
    return "Desconocido"

def main():
    if not os.path.exists(INPUT_IMAGE):
        print(f"⚠️ No existe la imagen de entrada: {INPUT_IMAGE}")
        return

    print(f"Analizando: {INPUT_IMAGE}")
    print(f"Dataset: {DATASET_PATH}")

    try:
        result = DeepFace.find(
            img_path=INPUT_IMAGE,
            db_path=DATASET_PATH,
            enforce_detection=False
        )

        if len(result) > 0 and len(result[0]) > 0:
            identity_path = result[0].iloc[0]["identity"]
            person_name = extract_person_name(identity_path)

            print(f"Persona reconocida: {person_name}")
            print(ACTIONS.get(person_name, "⚠️ Persona desconocida"))
        else:
            print("⚠️ Persona desconocida")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

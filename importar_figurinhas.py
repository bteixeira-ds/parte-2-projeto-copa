import json
from database import conectar

with open("figurinhas.json", "r", encoding="utf-8") as arquivo:
    figurinhas = json.load(arquivo)

conn = conectar()
cursor = conn.cursor()

for figurinha in figurinhas:
    cursor.execute(
        """
        INSERT INTO figurinhas (pais, numero)
        VALUES (%s, %s)
        """,
        (
            figurinha["pais"].strip(),
            figurinha["numero"]
        )
    )

conn.commit()

print(f"{len(figurinhas)} figurinhas importadas!")

cursor.close()
conn.close()
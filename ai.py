def analisar_sql(texto):

    texto_lower = texto.lower()

    mensagens = []

    score = 100

    # SUM sem GROUP BY
    if "sum(" in texto_lower and "group by" not in texto_lower:
        mensagens.append("""
❌ Erro:
Uso de SUM() sem GROUP BY.
""")
        score -= 20

    # SELECT *
    if "select *" in texto_lower:
        mensagens.append("""
⚠️ Aviso:
Evite usar SELECT *.
""")
        score -= 10

    # DELETE sem WHERE
    if "delete" in texto_lower and "where" not in texto_lower:
        mensagens.append("""
🚨 PERIGO:
DELETE sem WHERE.
""")
        score -= 50

    # UPDATE sem WHERE
    if "update" in texto_lower and "where" not in texto_lower:
        mensagens.append("""
🚨 PERIGO:
UPDATE sem WHERE.
""")
        score -= 50

    # JOIN sem ON
    if "join" in texto_lower and "on" not in texto_lower:
        mensagens.append("""
⚠️ Aviso:
JOIN sem ON.
""")
        score -= 15

    # Sugestões automáticas
    if "limit" not in texto_lower and "select" in texto_lower:
        mensagens.append("""
💡 Sugestão:
Use LIMIT em testes.
""")

    if "where" not in texto_lower and "select" in texto_lower:
        mensagens.append("""
💡 Sugestão:
Considere usar WHERE.
""")

    # Garantir score mínimo
    if score < 0:
        score = 0

    # Nível de risco
    if score >= 80:
        nivel = "🟢 Seguro"

    elif score >= 50:
        nivel = "🟡 Atenção"

    else:
        nivel = "🔴 Crítico"

    resultado = f"""
📊 Query Score: {score}/100

{nivel}
"""

    if mensagens:
        resultado += "\n".join(mensagens)

    else:
        resultado += "\n✅ Nenhum problema encontrado."

    return resultado
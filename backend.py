# 1. Cargar la bbdd con langchain
from langchain_community.utilities import sql_database

db = sql_database.SQLDatabase.from_uri("sqlite:///mdv.db")

# 2. Importar las APIs
import env_vars
import os

os.environ["OPENAI_API_KEY"] = env_vars.OPENAI_API_KEY

# 3. Crear el LLM
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# 4. Crear la cadena
from langchain_experimental.sql import SQLDatabaseChain

cadena = SQLDatabaseChain.from_llm(llm, db, verbose=False)

# 5. Formato personalizado de respuesta
formato = """
Dada una pregunta del usuario:
1. crea una consulta de sqlite3
2. revisa los resultados
3. devuelve el dato
4. si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
{question}
"""


# 6. Función para hacer la consulta
def consulta(input_usuario):
    consulta = formato.format(question=input_usuario)
    print("consulta: ", consulta)
    resultado = cadena.invoke(consulta)
    print("resultado: ", resultado)
    if (resultado):
         return resultado["result"]
    # Imprimir el valor de 'result'
    return result_value

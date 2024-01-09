# Libraries

import openai
from dotenv import load_dotenv
import os

# Prompting

PROMPT = """
        You will receive the draft content of a blog as text. Your task is to generate a proofread version of the file.

        As output, you are required to provide the following:

        1. Orthography Revision: Identify errors and provide their corrections.
        2. Grammatical Revision: Highlight areas where the text can be improved grammatically and offer better replacements to enhance it.
        3. Structural Revision: Propose an improved paragraph-by-paragraph structure, offering a clearer way to convey the main idea.
        4. Conceptual Revision: Conduct a critical analysis of the entire blog. What are its weaknesses? What ideas can be debated or further explored? Are there debates already covered elsewhere?
        5. Debate Revision: Which sections require deeper exploration? What ideas can be expanded upon?
        6. Suggest Three Title Ideas.
        7. Generate a List of Five Relevant SEO Keywords for the Topic.
        8. Suggest Three Blogs related to the main points discussed in this blog.
        
        Your response should be provided in the following format:
        
        {
            "General review": {
                "Orthography Revision": "content of orthography revision",
                "Grammatical Revision": "content of grammatical revision",
                "Structural Revision": "content of structural revision",
                "Conceptual Revision": "content of conceptual revision",
                "Debate Revision": "content of debate revision"
            },
            "Titles": {
                "title 1": "first suggested title",
                "title 2": "second suggested title",
                "title 3": "third suggested title"
            },
            "SEO": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"],
            "Blogs regarded": {
                "Blog 1": "Topic of the blog and why it's important",
                "Blog 2": "Topic of the blog and why it's important",
                "Blog 3": "Topic of the blog and why it's important"
            }
        }
        
        """
        
blog = """"
        La creencia en un mundo cognocible, además de modelable matemáticamente trae innevitablemente como resultado la creencia de que en algún momento una ecuación podría eventualmente describir el funcionamiento de la mente por más compleja que esta sea.

        Las redes neuronales, por su parte, poseen una capacidad teórica para aproximar cualquier función matemática dentro de lo que se ha llamado el Teorema de Aproximación Universal. Así, un circuito de redes con suficientes, neuronas, capas y nodos, puede aproximar cualquier función matemática por compleja que esta sea.

        Basado en lo anteior es preciso decir que, en tanto la mente es un sistema físico y no ideal o epifenomológico, es cognocible y se puede acceder a su información, modelándola mediante ecuaciones matemáticas. Y las redes neuronales podrían, con suficiente capacidad modelar dichas ecuaciones, es cuestión de tiempo (así sean miles de años) para que logremos decifrar la función (por más compleja que sea) que da origen a nuestra mente.

        No sólo eso, sino que si logramos modelar matemáticamente dicha ecuación, podriamos así mismo configurar un sistema computacional que la replique y entonces alcanzar el tan anhelado momento de replica de la ment humana. Si tenemos todas las variables, también podemos experimentar, describir y predecir.

        Esta hipótesis, tan determinista como simplista, sufrirá no obstante de ciertos embates. Por ejemplo, al igual que con el demono laplaciano, se argumentará que no será posible conocer todas las variables debido a la complejidad subatómica. No obstante, el argumento ignora el nivel de funcionamiento del cerebro, que si bien puede observarse a nivel de partícular subatómicas, es más bien a nivel biológico que cobra relevancia (o al menos eso creemos) para el estudio de la mente.

        Otro argumento en contra puede ser el dilema de la leche de soya. Este dilema plantea que pese a que puedan conseguirse productos similares a la leche, basados por ejemplo en plantas, su resultado no es leche, sino un producto similar. La discusión puede extenderse hacia las preguntas, entonces ¿Qué es la leche? ¿Qué condiciones debe cumplir un producto para ser leche? en fin. 

        El argumento anterior es interesante, y yo mismo estoy parcialmente a favor, no obstante desvía el tema, porque no estamos diciendo que como resultado tendriamos una mente humana sino un modelo que se comporta perfectamente como una. Quienes además defienden esta postura, se enfrentan al dilema del Rigor de la Ciencia planteado por Borges.

        Como científicos, es muy común que creamos conciente o inconcientemente en que el mundo es cognoscible además de modelable matemáticamente, y de seguro eso nos pone en aprietos cuando pensamos en si podemos modelar la mente mediante inteligencia artificial. Desde mi punto de vista, es posible conseguir un modelo de gran precisión y simulación al que llamaremos ‘mente artificial’, y será posible lograrlo incluso antes de entender perfectamente nuestro cerebro y de qué manera este produce la mente.
        
        """

def proofreading(blog):
    messages = [
        {"role":"system", "content":PROMPT}, 
        {"role": "user", "content": f"Please read and improve this blog: {blog}"}
    ]
    
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        
    )

    return res["choices"][0]["message"]["content"]

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    proofreading(blog)
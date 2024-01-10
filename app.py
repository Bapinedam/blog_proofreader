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
                "Orthography Revision": [each word missapelled: correction],
                "Grammatical Revision": [each sentence that can improve: the improved version],
                "Structural Revision": "content of structural revision proposing an improved paragraph-by-paragraph structure",
                "Conceptual Revision": "content of conceptual revision conducting a critical analysis of the entire blog. What are its weaknesses? What ideas can be debated or further explored? Are there debates already covered elsewhere?",
                "Debate Revision": "content of debate revision Which sections require deeper exploration? what ideas can be expanded upon?"
            },
            "Titles": {
                "title 1": "first suggested effective title",
                "title 2": "second suggested descriptive title",
                "title 3": "third suggested funny title"
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
        El realismo científico es una corriente filosófica epistemológica que sostiene que el mundo es independiente de nuestras percepciones y que es cognoscible a través de la ciencia y la observación. Es además posible describirlo mediante leyes matemáticas y científicas. En este sentido, el universo existe objetivamente y podemos acceder a él mediante investigación científica, matemática y lógica.

        La creencia en un mundo cognoscible y modelable matemáticamente inevitablemente conduce a la idea de que es posible encontrar una ecuación que describa cualquier fenómenos por complejo que este sea, incluyendo por supuesto la mente.

        Las redes neuronales artificiales (ANN), por su parte, poseen la capacidad teórica de aproximar cualquier función matemática, lo cual se conoce como el Teorema de Aproximación Universal. Esto implica que un conjunto de redes con suficientes neuronas, capas y nodos puede aproximarse a cualquier función matemática, por compleja que esta sea.

        En consecuencia, es preciso decir que, dado que la mente es un sistema físico y no puramente ideal o epifenoménico, es cognoscible y, en teoría, su funcionamiento puede representarse mediante ecuaciones matemáticas. Las redes neuronales, con su capacidad de aproximación, son herramientas plausibes para modelar estas ecuaciones. Es decir que, es una cuestión de tiempo, posiblemente años, décadas o siglos, pero descifrar la función que subyace a nuestra mente podría ser alcanzable.

        Alcanzar la comprensión matemática de la mente abre consigo la posibilidad de configurar un sistema computacional que replique su funcionamiento. Teniendo un modelo con dichas características seremos capaces de describir, experimentar y predecir.

        Esta suposición determinista, aunque simplista, enfrenta ciertas críticas. Una de ellas es la misma que enfrenta el demonio laplaciano. sugiriendo que la complejidad del sistema haría imposible la recopilación y el cálculo de todos los datos relevante. Sin embargo, es que hay modelos que pese a su simpleza describen casi que a la perfección el fonémeno de estudio sin necesidad de ahondar necesariamente en todas las variables. Aún si fuera necesario, el argumento de la complejidad pierde fuerza en tanto tenemos algoritmos y procesamiento más capaz.

        Otra crítica comparable, es la que a mi me gusta llama, el dilema de la leche de soya. Un argumento que utilicé en una clase de filosofía en la universidad para ilustrar un punto. El argumento versa que, aunque llamemos leche de soya a la bebida que ya conocemos, en realidad no es leche. Y no lo es por su naturaleza misma. Aquí la contraparte, o los vegetarianos, pueden contraargumentar diciendo que si cambian todas sus propiedades al punto de ser una copia perfecta, es ahora leche. No obstante, no importan sus propiedades, su sabor, o su color, simplemente no es leche. La única forma de obtener leche de vaca es extrayéndola de una vaca.

        Al igual que con la mente, el problema rapidamente dará un giro a la pregunta ¿Entonces qué es la leche? Pero la pregunta sólo busca desviar el problema, porque no estamos buscando recrear la mente humana sino modelarla. Aunque se logre un modelo que se comporte como la mente humana, podría ser un simulacro más que una reproducción auténtica. Así mismo, los defensores de esta postura se enfrentan al dilema del Rigor de la Ciencia planteado por Borges, que sugiere que una representación exacta puede perder su utilidad práctica al volverse tan extensa como la realidad misma.

        En tanto científicos, solemos creer que el mundo es cognoscible y modelable matemáticamente. Esta perspectiva plantea desafíos al considerar la posibilidad de modelar la mente a través de la inteligencia artificial. Desde mi punto de vista, es plausible alcanzar un modelo altamente preciso y simulado, denominado 'mente artificial', incluso antes de comprender en su totalidad cómo nuestro cerebro genera lo que llamamos ‘la mente’.
                
        """

def proofreading(blog):
    messages = [
        {"role":"system", "content":PROMPT}, 
        {"role": "user", "content": f"Please read and improve this blog: {blog}"}
    ]
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    proofreading(blog)
    
    
## ESTA USANDO LA VIEJA VERSIÓN DE CHAT GPT, CAMBIA LA SINTAXIS
## PRUEBA QUE FUNCIONE CON TU BLOG ACTUAL
## AGREGA INTERACTIVIDAD
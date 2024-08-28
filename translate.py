import sys
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI()

class Text():

    def __init__(self, input_str: str, sep: str = ";") -> None:

        self.input = input_str
        self.sep = sep
        pass

    def input_to_list(self) -> list[str]:

        assert isinstance(self.input, str)
        return self.input.split(self.sep)

    def ask_gpt(self) -> str:

        converted_str: list[str] = self.input_to_list()
        
        completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": """You will recieve an input as a list of strings
Your job is to figure out what the most likely sentence is
Please only return the sentence, nothing more"""},
                    {"role": "user", "content": str(converted_str)},
                    ],
                    
)
        return res if (res := completion.choices[0].message.content) is not None else "NA"


global DEBUG
DEBUG = False

def main() -> None:

    if (input_len := len(sys.argv)) < 2:
        print("Error: Expected Input string not found") if DEBUG else None
        return
    elif input_len > 2:
        print("Error: To many arguements") if DEBUG else None
        return

    text = Text(input_str=sys.argv[1])
    print(text.ask_gpt())

if __name__ == "__main__":
    main()

import os

from ai import call_gpt

def main():

    # TODO: your code here

    name = input("Enter your name: ")

    topic = input("Enter a topic: ")

    response = call_gpt(f"Generate a Haiku where a person named '{name}' reflects on '{topic}'")
    print(response)

if __name__ == "__main__":
    main()
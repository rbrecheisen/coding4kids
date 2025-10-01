import ollama


def main():
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": "Explain recursion like I'm 12"}
    ])
    print(response['message']['content'])


if __name__ == '__main__':
    main()
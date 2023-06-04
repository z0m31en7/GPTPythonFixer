import sys
import subprocess
import openai

def fix_python_file(file_path, use_pipe):
    with open(file_path, 'r') as file:
        python_code = file.read()

    if use_pipe:
        try:
            result = subprocess.run(['python', file_path], capture_output=True, text=True)
            python_output = result.stdout
        except subprocess.CalledProcessError as e:
            python_output = e.output

        conversation = [
            {"role": "system", "content": "You are a Python code fixer."},
            {"role": "user", "content": python_output},
            {"role": "assistant", "content": "Please help me fix any errors in the code."}
        ]
    else:
        conversation = [
            {"role": "system", "content": "You are a Python code fixer."},
            {"role": "user", "content": python_code},
            {"role": "assistant", "content": "Please help me fix any errors in the code."}
        ]

    openai.api_key = 'YOUR_API_KEY'
    chatgpt = openai.ChatCompletion.create(model="gpt-3.5-turbo")

    response = chatgpt.messages.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    suggested_output = response['choices'][0]['message']['content']

    if use_pipe:
        print("Suggested Output:")
        print(suggested_output)
    else:
        if suggested_output != python_code:
            print("Suggested Code:")
            print(suggested_output)

            user_input = input("Do you want to replace the code in the file? (yes/no): ")

            if user_input.lower() == "yes":
                with open(file_path, 'w') as file:
                    file.write(suggested_output)
                print("Code replaced successfully!")
            else:
                print("Code not replaced.")
        else:
            print("No errors found in the code!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the Python file as a command-line argument.")
        sys.exit(1)

    file_path = sys.argv[1]

    use_pipe = False
    if len(sys.argv) > 2 and (sys.argv[2] == '-p' or sys.argv[2] == '--pipe'):
        use_pipe = True

    fix_python_file(file_path, use_pipe)

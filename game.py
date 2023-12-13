import openai
import time

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def introduction():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself at the beginning of an exciting journey...\n")

def make_choice(prompt, options):
    full_prompt = f"{prompt}\nOptions: {', '.join(options)}\n\nYour Choice: "
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=full_prompt,
        max_tokens=100,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()

def start_game():
    introduction()

    print("You wake up in a mysterious forest with two paths ahead.")

    # First choice using LLM
    choices_1 = ["Follow the path with glowing mushrooms", "Cross the old bridge"]
    user_choice_1 = make_choice("Which path do you choose?", choices_1)

    if user_choice_1.lower() == "follow the path with glowing mushrooms":
        print("The path leads you to a hidden cave filled with treasures!")
        # Continue the story based on this choice
    else:
        print("The bridge collapses, and you fall into a river below.")
        # Continue the story based on this choice

def main():
    start_game()

if __name__ == "__main__":
    main()

# Text-Based Adventure Game

This is a text-based adventure game implemented in Python, incorporating the power of a Large Language Model (LLM) to dynamically generate story elements based on user choices.

## Project Structure

    text_adventure_game/
    |-- game.py
    |-- README.md


## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/text_adventure_game.git
   cd text_adventure_game

2. **Run the Game:**

    ```bash
    python game.py

## How to Play

- Follow the prompts to make choices and navigate through the story.
- Each choice dynamically influences the narrative, thanks to the integration with a Large Language Model.

## Using Large Language Model (LLM)

This game leverages OpenAI's GPT-3 to generate dynamic story elements based on user choices. The `make_choice` function sends prompts to GPT-3, incorporating the current situation and available options. GPT-3 generates text continuations, making the gameplay experience more engaging and responsive.

To use GPT-3, set your OpenAI API key in the `game.py` file:

```python
# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'
```

## Contributing

Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

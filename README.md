# 🔐 AI-Powered Password Generator

A Python script that uses the **Groq API** with Meta's **LLaMA 3.3 70B** model to generate strong, unpredictable passwords on demand — and store them in an in-memory vault.

---

## 📋 Overview

Rather than relying on traditional random character shuffling, this program delegates password creation to a large language model (LLM) via the Groq API. A strict system prompt ensures the model returns **only the password** — no extra text, explanations, or suggestions. The result is stored in a Python dictionary acting as a simple password vault.

---

## 🚀 How It Works

1. The user inputs a desired password length (minimum 8 characters).
2. The script sends a prompt to **LLaMA 3.3 70B Versatile** via Groq, requesting a strong password of that length.
3. The model returns just the password (enforced by the system prompt).
4. The password is printed and stored in a `vault` dictionary for reference.

---

## 🧩 Code Breakdown

### 1. Client Initialization
```python
from groq import Groq
client = Groq(api_key="")
```
Imports the Groq SDK and creates an authenticated client. Your API key goes in the `api_key` field.

---

### 2. `generate_password(length=16)` Function

```python
def generate_password(length=16):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security reasons.")
```
- Default length is **16 characters**.
- Raises a `ValueError` immediately if the requested length is below 8 — enforcing a minimum security baseline before any API call is made.

```python
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a password generator. Generate a strong password with the specified length. only return the password, no other text or suggestions"
            },
            {
                "role": "user",
                "content": f"Generate a strong password of length {length}."
            }
        ]
    )
```
Two messages are sent in the chat:
- **System message**: Constrains the model's behavior — it must act solely as a password generator and return nothing but the password itself.
- **User message**: Specifies the exact character length required.

```python
    password = chat_completion.choices[0].message.content.strip()
    return password
```
Extracts the first response choice, strips any surrounding whitespace, and returns the clean password string.

---

### 3. Interactive Input & Error Handling
```python
try:
    password_length = int(input("Enter desired password length (minimum 8): "))
    new_password = generate_password(password_length)
    print(f"Generated Password: {new_password}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
- Prompts the user for a length at runtime.
- `ValueError` catches both invalid input (e.g. letters instead of numbers) and the minimum-length enforcement from the function.
- A broad `Exception` catch handles unexpected failures like network errors or API issues.

---

### 4. Vault Storage
```python
vault = {
    "generated_password": new_password
}
print(f"Dictionary Storage: {vault}")
```
Stores the generated password in a Python dictionary — a lightweight in-memory vault. `new_password` here is the variable set inside the `try` block, so it is only accessible if password generation succeeded.

---

## ⚙️ Requirements

| Requirement | Details |
|-------------|---------|
| Python | 3.7+ |
| Groq SDK | `pip install groq` |
| Groq API Key | [Get one at console.groq.com](https://console.groq.com) |
| Model Used | `llama-3.3-70b-versatile` |

---

## 🛠️ Setup & Usage

### 1. Install the Groq SDK
```bash
pip install groq
```

### 2. Add your API key
Replace the empty string with your Groq API key, or better — use an environment variable:
```python
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
```

### 3. Run the script
```bash
python password_generator.py
```

### Example Output
```
Enter desired password length (minimum 8): 20
Generated Password: Xk#9mLpQ2$rTvN8wJc@1

Dictionary Storage: {'generated_password': 'Xk#9mLpQ2$rTvN8wJc@1'}
```

---

## 🔑 Key Improvement Over v1

The system prompt now explicitly instructs the model to return **only the password and nothing else**:

```
"only return the password, no other text or suggestions"
```

This eliminates the need for extra parsing logic and makes the output reliable and clean every time.

---

## ⚠️ Limitations & Considerations

- **`vault` depends on `try` block success** — if an error occurs, `new_password` will be undefined and the `vault` line will raise a `NameError`. Consider initializing `new_password = None` before the `try` block to guard against this.
- **Not cryptographically guaranteed** — LLM output is probabilistic. For security-critical systems, supplement with Python's `secrets` module.
- **Never hardcode API keys** — use environment variables or a secrets manager in production.
- **API dependency** — requires an active internet connection and a valid Groq API key.

---

## 📁 Project Structure

```
password-generator/
│
├── password_generator.py   # Main script
└── README.md               # This file
```

---

## 📄 License

Open for personal and educational use.





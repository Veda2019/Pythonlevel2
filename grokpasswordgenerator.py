from groq import Groq
client = Groq (api_key="--")
def generate_password(length=16):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security reasons.")
    
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a password generator. Generate a strong password with the specified length."
            },
            {
                "role": "user",
                "content": f"Generate a strong password of length {length}."
            }
        ]
    )
    
    password = chat_completion.choices[0].message.content.strip()
    return password
# Example usage
try:
    password_length = int(input("Enter desired password length (minimum 8): "))
    new_password = generate_password(password_length)
    print(f"Generated Password: {new_password}")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}") 
vault = {
    "generated_password": generate_password(20)
}

print(f"Dictionary Storage: {vault}")
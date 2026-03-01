from groq import generate_response  # Change to 'from hf' to switch providers

def bias_mitigation_activity():
    print("\n=== BIAS MITIGATION ACTIVITY ===")
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity.")
        return
    
    print("\nProcessing initial response...")
    initial_response = generate_response(prompt, temperature=0.3, max_tokens=1024)
    print(f"\nInitial AI Response: {initial_response}")
    
    modified_prompt = input("\nModify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): ").strip()
    if modified_prompt:
        print("Processing modified response...")
        modified_response = generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nModified AI Response (Neutral): {modified_response}")
    else:
        print("No modified prompt provided. Skipping neutral response.")

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===")
    long_prompt = input("Enter a long prompt (more than 300 words): ").strip()
    if long_prompt:
        print("Processing long prompt...")
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preview = (long_response[:500] + "...") if len(long_response) > 500 else long_response
        print(f"\nAI Response to long prompt (Preview): {preview}")
    else:
        print("No long prompt provided. Skipping token limit response.")
    
    short_prompt = input("\nNow, condense the prompt to be more concise: ").strip()
    if short_prompt:
        print("Processing short prompt...")
        short_response = generate_response(short_prompt, temperature=0.3, max_tokens=1024)
        print(f"\nAI Response to short prompt: {short_response}")
    else:
        print("No short prompt provided. Skipping condensed prompt response.")

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Bias Mitigation")
    print("2) Token Limits")
    choice = input("> ").strip()
    
    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    run_activity()
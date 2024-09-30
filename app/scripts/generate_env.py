import os

def generate_env():
    env = {}
    print("Enter variables for .env file, leave empty to finish")
    while True:
        key = input("Key: ")
        if not key:
            break
        value = input("Value: ")
        env[key] = value
    with open(".env", "w") as f:
        for key, value in env.items():
            f.write(f"{key}={value}\n")

if __name__ == "__main__":
    generate_env()

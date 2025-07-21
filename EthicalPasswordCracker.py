
# Program: ETHICALPasswordCracker
# Created by: Shahakar Patel
# Date: 7/21/25


import string
import itertools
import concurrent.futures   # multi-threading import
import time

# Target password that you want to "breach"
target_password = "sha2" 

# Allowed characters (lowercase letters + digits)
characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
# Max password length to attempt
max_length = 4
# Global flag to stop once the password is found
found = False
# Function that each thread runs to attempt password cracking
def attempt_passwords(start_char): 
    global found
    # Go through lenghts from 1 up to the max length
    for length in range(1, max_length +1):
        # This code will generate all the combinations for the rest of the characters
        # EXCLUDING the start_char
        for combo in itertools.product(characters, repeat = length - 1):
            if found:  # Stop if another thread already found the password
                return
            attempt = start_char + ''.join(combo) #build password guess
            if attempt == target_password: #comparison fixed (==)
                found = True
                print(f"\n Password found: {attempt}" )
                return

# Main function to control the threads            
def main():
    global found
    start_time = time.time() # This little block is to start the timer. 

    with concurrent.futures.ThreadPoolExecutor() as executor: 
        futures = []
        # Start a thread for each possible starting character
        for start_char in characters: 
            futures.append(executor.submit(attempt_passwords, start_char))
        # Wait until any one thread finishes (Finds the password in other words)
        concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)
    
    #T hese next codes show the results
    if not found: 
        print("\n Password not found...")
    else:
        print(f"Time taken: {time.time() - start_time:.2f}seconds")

# This bloc is the entry point. 
if __name__ == "__main__": 
    main()
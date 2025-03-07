# Step 1: Create the file and write the secret message
sent_message = 'Hey there! This is a secret message.'
with open('sent_message.txt', 'w') as file:
    file.write(sent_message)

# Step 2: Replace the message in the file with a new one
unsent_message = 'This message has been unsent.'
with open('sent_message.txt', 'r+') as file:
    # Read the current message
    original_message = file.read()
    
    # Go back to the start of the file
    file.seek(0)
    
    # Write the new message
    file.write(unsent_message)
    
    # Remove any extra characters from the original message
    file.truncate(len(unsent_message))

# Display the messages
print("Original message:", original_message)
print("Updated message:", unsent_message)

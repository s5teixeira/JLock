Stephanie Teixeira 
COMP350-001

This project-refactoring of the original JLOCK program written by Joseph Matta. JLOCK is a command line encryption tool written in Python. It uses a somewhat complex encryption algorithm to convert human readable text (plaintext) to a series of seemingly incoherent numbers.

JLOCK has six commands:
  -lock : used to encrypt (lock) a plaintext message. When a message is encrypted, it is stored in a 
‘XXXX_encrypted_msg.txt’ file. Associated XXXXXXXX_lock.txt and XXXXXXXX_key.txt files are 
also generated when a plaintext message is encrypted. 
  -unlock : used to decrypt (unlock) an encrypted message. When a message is decrypted, it is 
stored in a ‘XXXX_decrypted_msg.txt’ file. The XXXX_encrypted_msg.txt, XXXXXXXX_lock.txt, and 
XXXXXXXX_key.txt files associated with the encrypted file are automatically deleted when the 
message is decrypted back to plaintext. 
  -msg : get a list of all decrypted messages along with the XXXX_decrypted_msg.txt files they are 
stored in.  
  -locked : get a list of all encrypted messages and the XXXX_encrypted_msg.txt files they are 
stored in.  
  -clear : deletes all ‘XXXX_encrypted_msg.txt’, ‘XXXXXXXX_lock.txt’, ‘XXXXXXXX_key.txt’, and 
‘XXXX_decrypted_msg.txt’ files in the JLOCK project directory. This command essentially “resets” 
the JLOCK environment and deletes all remaining text files associated with previously encrypted 
and decrypted messages. 
  -help/-h : this command displays a help menu describing how to use each command. 

Refactored portions of the JLOCK codebase, added necessary modifications,and unit testing.

Run 'python jlock.py'

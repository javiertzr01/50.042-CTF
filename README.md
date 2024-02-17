# 50.042-CTF
## Cybersec CTF Draft 

### Name of challenge: Fermet enjoys factoring 

### Summary of Challenge:  

Participant is tasked to figure out the private key of an insecure RSA key pair 

Participant is tasked to decrypt a message that was encrypted with an insecure RSA key pair. 

Participant is required to notice that the message is a vigenere ciphertext and tasked to decipher the ciphertext to obtain the flag 

### Information Provided: 

- Public key in the form of <e,n> where e=65537 and n is an integer 

- A file containing the RSA encrypted text 

### Description 

Alice and Bob are both students, in a relationship, who took the 50.042 Foundations of Cybersecurity module. During the module, Alice gave Bob a number, and told Bob that this number would be his private key if they ever used RSA. Alice was convinced that as long as the prime numbers she chose for 
n were large enough that RSA will be secure. Alice is now on Global Exchange and wishes to send Bob a message that she absolutely cannot allow anyone else to know about. Thus, she took measures to setup a communication channel to send Bob a message. As a nosy individual, you really want to know what the message is. 

##### Note: Alice’s favourite cipher is vigenere cipher and she only likes alphabets 

##### Hint: Fermat’s factorization method 

### Intended Solution 

Using Fermat’s factorization method, uncover Bob’s private key 

Use Bob’s private key to decrypt the message sent via RSA  

Determine the length of the key used in the vigenere cipher of the uncovered message 

Decipher the message 

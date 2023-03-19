[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10507985)
<!--
[Link to Chap 5 Lab18](https://docs.google.com/presentation/d/1r3h2R9JwK9HK_U2Ia-zncL0BSjHV6Giu6ugNJ6yZpgc/edit#slide=id.g1715447b552_0_27)

![Lab 16](https://nimbus-screenshots.s3.amazonaws.com/s/e634571b38c8923031df60fc7fc2fe3f.png)
-->

## Complete the "main.py"

Explanation
  The program examines the email used for input and is read to find whether or not it is 'True' or 'False' by examining if it has @ or .

Code
  email = input('Enter your email: ')
  
    if(email[0].isalpha()):
        if(len(email) > 5 and len(email) < 30):
            if(email.find('@')):
                if('.' in email):
                    print('True')
                else:
                    print('False')
            else:
                print('False')
        else:
            print('False')
    else:
        print('False')
    pass

Output
  Whether or not the email is 'True' or 'False' is displayed here
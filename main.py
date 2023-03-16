def main():
    ##################################################
    # Comlete your code here
    ##################################################
    email = input('Enter your email: ')
  
    if(email[0].isalpha()):
      if(len(email)> 5 and len(email) <30):
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



  
if __name__ == '__main__':
    main()

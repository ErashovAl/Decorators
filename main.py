from Habr import search_in_soup

def main():
 
    keywords = ['месяц', 'java']
    for word in keywords:
        print(word)
        search_in_soup(word)
    

if __name__ == '__main__':
    
    main()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

me = {
    0: {'user': 'user1' , 'password': 'password1'}, 
    #1: {'user': 'user2' , 'password': 'password2'}, 
}

url = 'https://instagram.com/'

accounts = ['mazatagra' , 'tirryaq']

posts = 3

comments = ['Comment 1' , 'Comment 2']

driver = webdriver.Chrome()

def login(user , password, attempts):
    try:
        driver.get('https://instagram.com')
        time.sleep(7)

        driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(user)
        driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        return True
    except:
        print('!Error while loging in')

        if attempts <= 2:
            attempts = attempts + 1
            login(user , password, attempts)
        else:
            return False
        


def get_posts(link, posts, attempts):
    try:
        driver.get(link)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        query = """links=''; 
        for (var i =0; i < """+ str(posts)  + """; i++) { 
            links += document.getElementsByClassName('v1Nh3 kIKUG  _bz0w')[i].children[0].href + '||';
            } 
        return links;
        """

        get_posts_links = driver.execute_script(query)
        return get_posts_links
    except:
        print('!Error while geting posts links')

        if attempts <= 2:
            attempts = attempts + 1
            get_posts(link, posts, attempts)
        else:
            return False

def write_comment(post, comment , attempts):
    try:
        driver.get(post)
        time.sleep(3)

        comment_bar = driver.find_element_by_class_name('Ypffh')
        comment_bar.click()
        time.sleep(3)
        comment_bar = driver.find_element_by_class_name('Ypffh')
        comment_bar.click()
        comment_bar.send_keys(comment)
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    except:
        print('!Error while writing a comment')

        if attempts <= 2:
            attempts = attempts + 1
            write_comment(post, comment , attempts)
        else:
            return False
    

for i in me:
    user = me[i]['user']
    password = me[i]['password']

    if login(user , password, 0) == True:
        time.sleep(2)

        for account in accounts:
            link = url + account 

            posts_links = get_posts(link, posts, 0)
            if posts_links != False:
                posts_links = posts_links.split('||')
                time.sleep(2)

                for post in posts_links:
                    for comment in comments:
                        print(comment, post)
                        time.sleep(2)
                        write_comment(post, comment, 0)
    
    driver = webdriver.Chrome()
                
                    

    
        



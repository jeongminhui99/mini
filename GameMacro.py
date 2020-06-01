from selenium import webdriver
driver=webdriver.Chrome('/chromedriver.exe')
driver.get('https://zzzscore.com/1to50/')

num = 1

def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
#       print(btn.text, end='\t')
        if btn.text == str(num):
            btn.click()
            print("number "+str(num)+" clicked!")
            num += 1
            return

while num<=50:
    clickBtn()
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import datetime
import os


# In[2]:


#Menu.txt dosyası oluşturma
f= open("Menu.txt","w")
f.writelines(["1)Klasik Pizza\n", "2)Margarita\n", "3)TurkPizza\n", "4)Sade Pizza\n","5)Zeytin\n", "6)Mantar\n", "7)Keçi Peyniri\n", "8)Et\n","9)Soğan\n","10)Mısır"])
f.close()


# In[3]:


f=open("Menu.txt","r")
print(f.read())


# In[4]:


#ust sınıf olustur
class Pizza():
  def __init__(self):
    self.description=""
    self.cost=0

  def get_description(self):
    return self.description

  def get_cost(self):
    return self.cost


# In[18]:


#alt sınıf oluştur "pizza"
class Klasik(Pizza):
 def __init__(self):
  self.description="Malzemeler: peynir, zeytin, mısır"
  self.cost = 60.0


# In[6]:


class Margherita(Pizza):
  def __init__(self):
    self.description="Malzemeler: domates, mozarella, feslegen"
    self.cost = 50.0


# In[20]:


class Turk(Pizza):
  def __init__(self):
    self.description="Malzemeler: salam, sucuk, peynir, domates"
    self.cost=75.0


# In[21]:


class Sade(Pizza):
  def __init__(self):
    self.description="Malzemeler: domates, peynir, zeytin"
    self.cost=45.0


# In[22]:


#ust sınıf olustur (decorator)
class Decorator():
  def __init__(self, pizza):
    self.pizza = pizza
    self.description = ''
    self.cost = 0
    
  def get_description(self):
    return self.description + "," + self.pizza.get_description()

  def get_cost(self):
    return self.cost + self.pizza.get_cost()


# In[23]:


class Zeytin(Decorator):
  def __init__(self, pizza):
    Decorator.__init__(self, pizza)
    self.cost = 5.0
    self.description = "Zeytin"


# In[24]:


class Mantar(Decorator):
   def __init__(self, pizza):
    Decorator.__init__(self, pizza)
    self.cost = 10.0
    self.description = "Mantar"


# In[25]:


class KeciPeyniri(Decorator):
   def __init__(self, pizza):
    Decorator.__init__(self, pizza)
    self.cost = 25.0
    self.description = "KeciPeyniri"


# In[26]:


class Et(Decorator):
  def __init__(self, pizza):
    Decorator.__init__(self, pizza)
    self.cost = 25.0
    self.description = "Et"


# In[27]:


class Sogan(Decorator):
   def __init__(self, pizza):
    Decorator.__init__(self, pizza)
    self.cost = 5.0
    self.description = "Sogan"


# In[28]:


class Mısır(Decorator):
   def __init__(self, pizza):
    Decorator.__init__(self, pizza)
    self.cost = 5.0
    self.description = "Mısır"


# In[29]:


#main fonk olustur
def main():
  with open ("Menu.txt", 'r') as menu:
    for line in menu:
     print(line, end="")


# In[31]:


def place_Order():
  #pizza seçimi
  pizza = ""
  while pizza == "":
    selectpizza = input("Lütfen pizzanızı seçin: ")
    if selectpizza == "1":
      pizza = Klasik()
    elif selectpizza == "2":
      pizza = Margherita()
    elif selectpizza == "3":
      pizza = Turk()
    elif selectpizza == "4":
      pizza = Sade()
    else:
        print("Lütfen menüde bulunan pizzalardan bir seçim yapınız.")
    #sos seçimi
    soslar = ""
  while soslar == "":
    selectsauce = input("lütfen pizza sosunuzu seçin: ")
    if selectsauce == "5":
       soslarObject = Zeytin(pizza)
       soslar = selectsauce
    elif selectsauce == "6":
      soslarObject = Mantar(pizza)
      soslar = selectsauce
    elif selectsauce == "7":
      soslarObject = KeciPeyniri(pizza)
      soslar = selectsauce
    elif selectsauce == "8":
      soslarObject = Et(pizza)
      soslar = selectsauce
    elif selectsauce == "9":
      soslarObject = Sogan(pizza)
      soslar = selectsauce
    elif selectsauce == "10":
      soslarObject = Mısır(pizza)
      soslar = selectsauce
    else:
    
      print("Lütfen menüden bir sos seçiniz.")

    toplamFiyat = soslarObject.get_cost()
    pizzadescription = soslarObject.get_description()
    print(f"{pizzadescription} pizzanız hazır toplam fiyat:{str(toplamFiyat)}")
    
  
place_Order()


# In[32]:


customer_name = ''
    while customer_name=='':
        customer_name = input("Lütfen adınızı yazın: ")
        if customer_name == '':
            print("Adınız kısmı boş bırakılamaz.")

    tc_no = ''
    while tc_no=='':
        tc_no = input("Lütfen TC numaranızı girin: ")
        if len(tc_no)!= 11:
            print("Lütfen TC numaranızı kontrol ediniz")
            tc_no = ''

    card_no=''
    while card_no=='':
        card_no=input('Lütfen kartınızın üzerindeki numarayı girin: ')
        if len(card_no)!=16:
            print("Kart numaranızı kontrol ediniz")
            card_no=''
            
    card_pass=''
    while card_pass=='':
        card_pass=input("Şifrenizi giriniz: ")
        order_time=datetime.datetime.now()
        


# In[ ]:


with open('Orders_Database.csv', 'a') as orders:
    orders = csv.writer(orders, delimiter=',')
    orders.writerow([customer_name, tc_no, card_no, card_pass, order_time])
print('Siparişiniz başarılı. Afiyet olsun!')


# In[ ]:





from tkinter import * 
import math,random
from tkinter import messagebox
import os
import smtplib
from PIL import Image,ImageTk
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen
 
class Bill_App:
    def __init__(self, master):
        self.master=master
        self.master.geometry("1920x1080+-10+0")
        self.master.title("shop management system")
 
        title=Label(self.master,text="SHOP MANAGEMENT",bd=12,relief=GROOVE,bg="sky blue",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #    variable ---------------------------------------
        
        #   Beverage variable
        self.Green_Tea=IntVar()
        self.Masala_Tea=IntVar()
        self.Herbal_Tea=IntVar()
        self.Nescafe_classic_coffe=IntVar()
        self.Bru_Instant_Coffe=IntVar()
        self.Real_Mixed_Fruit_Juice=IntVar()
        self.Hersheyas_hot_chocolate_drink=IntVar()
        self.Curacao=IntVar()
        self.Red_Bull=IntVar()
        self.Coca_Cola=IntVar()
        
        # grocery varible
        self.ToorDal=IntVar()
        self.Daawat_Rozana_Basmati_Rice=IntVar()
        self.Fortune_Chakki_Fresh_Aata=IntVar()
        self.Besan=IntVar()
        self.Poha=IntVar()
        self.Oats=IntVar()
        self.Muesli=IntVar()
        
        # chocalates_and_sweets varible
        self.Cadbury_Silk=IntVar()
        self.Ferrero_Rocher=IntVar()
        self.Kisses_Hersheys=IntVar()
        self.Haldirams_Patisa=IntVar()
        self.Besan_Laddoo=IntVar()
        self.Ghee_Gajak_Rolls=IntVar()
        self.Gulab_Jamun=IntVar()
        self.Rasgulla=IntVar()
 
        # spices_and_seasonings varible
        
        self.Turmeric_Powder=IntVar()
        self.Red_Chilli_Powder=IntVar()
        self.Corriander_powder=IntVar()
        self.Garam_Masala=IntVar()
        self.Hing=IntVar()
        self.Salt=IntVar()
        self.Oregano=IntVar()

        # Dry_Fruits_and_Snacks varible
        self.Cashewnuts=IntVar()
        self.Almonds=IntVar()
        self.Raisins=IntVar()
        self.Pistachios=IntVar()
        self.walnut=IntVar()
        self.Lays_American_Style_potato_chips=IntVar()
        self.Haldiram_Bhujia_sev=IntVar()

        # Cooking_and_Ready_To_Eat varible
        self.Saffola_Gold_Oil=IntVar()
        self.Figaro_Olive_Oil=IntVar()
        self.Amul_Ghee=IntVar()
        self.Butter=IntVar()
        self.Maggi=IntVar()
        self.Pasta=IntVar()
        self.Oreo_Biscuit=IntVar()
        self.Hide_and_seek_Biscuit=IntVar()
        self.Parle_G_Biscuit=IntVar()
        
        #product price varible
        
        self.Beverage_price=StringVar()
        self.grocery_price=StringVar()
        self.chocalates_and_sweets_price=StringVar()
        self.spices_and_seasonings_price=StringVar()
        self.Dry_Fruits_and_Snacks_price=StringVar()
        self.Cooking_and_Ready_To_Eat_price=StringVar()
        
        # tax varible
        
        self.Beverage_tax=StringVar()
        self.grocery_tax=StringVar()
        self.chocalates_and_sweets_tax=StringVar()
        self.spices_and_seasonings_tax=StringVar()
        self.Dry_Fruits_and_Snacks_tax=StringVar()
        self.Cooking_and_Ready_To_Eat_tax=StringVar()
        
        #customer details
        
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.c_mail=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        # admin
        self.admin_id=StringVar()
        self.admin_pass=StringVar()
        
        
        
        # ------------>>> CUSTOMER DETAILS <<<<<-----------------
        F0=LabelFrame(self.master,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F0.place(x=0,y=70,width=950)
        
        cname_label=Label(F0,text="Customer Name",bg="sky blue",font=("times new romen",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F0,width=20,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_label=Label(F0,text="Phone No.",bg="sky blue",font=("times new romen",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F0,width=20,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
         ################################ send email button
        F1=LabelFrame(self.master,bd=10,relief=GROOVE,text="send bill via Email ",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F1.place(x=950,y=70,width=587)
        
        cmail_label=Label(F1,text="Email",bg="sky blue",font=("times new romen",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cmail_txt=Entry(F1,width=20,textvariable=self.c_mail,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        #bn_txt=Entry(F9,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        send_btn=Button(F1,text="Send",bg="cyan",bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=7) #enter this line :- command=self.check_mail
 
        
        #----------------->>>>> Beverage frame <<<----------------
        F2=LabelFrame(self.master,bd=10,relief=GROOVE,text="Beverage",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F2.place(x=5,y=152,width=277,height=393)
        
        # Green_Tea
        Green_Tea_txt=Entry(F2,width=2,textvariable=self.Green_Tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        Green_Tea_label=Label(F2,text="Green_Tea",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        #Masala_Tea
        Masala_Tea_label=Label(F2,text="Masala_Tea",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Masala_Tea_txt=Entry(F2,width=2,textvariable=self.Masala_Tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #Herbal_Tea
        Herbal_Tea_label=Label(F2,text="Herbal_Tea",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Herbal_Tea_txt=Entry(F2,width=2,textvariable=self.Herbal_Tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #Nescafe_classic_coffe
        Nescafe_classic_coffe_label=Label(F2,text="Nescafe_classic_coffe",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Nescafe_classic_coffe_txt=Entry(F2,width=2,textvariable=self.Nescafe_classic_coffe,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        #Bru_Instant_Coffe
        Bru_Instant_Coffe_label=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Bru_Instant_Coffe_txt=Entry(F2,width=2,textvariable=self.Bru_Instant_Coffe,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        #Real_Mixed_Fruit_Juice
        Real_Mixed_Fruit_Juice_label=Label(F2,text="Real_Mixed_Fruit_Juice",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Real_Mixed_Fruit_Juice_txt=Entry(F2,width=2,textvariable=self.Real_Mixed_Fruit_Juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        #Hersheyas_hot_chocolate_drink
        Hersheyas_hot_chocolate_drink_label=Label(F2,text="Hersheyas_hot_chocolate_drink",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        Hersheyas_hot_chocolate_drink_txt=Entry(F2,width=2,textvariable=self.Hersheyas_hot_chocolate_drink,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10,sticky=W)
        
        #Curacao
        Curacao_label=Label(F2,text="Curacao",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        Curacao_txt=Entry(F2,width=2,textvariable=self.Curacao,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10,sticky=W)

        #Red_Bull
        Red_Bull_label=Label(F2,text="Red_Bull",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=8,column=0,padx=10,pady=10,sticky="w")
        Red_Bull_txt=Entry(F2,width=2,textvariable=self.Red_Bull,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=10,sticky=W)

        #Coca_Cola
        Coca_Cola_label=Label(F2,text="Coca_Cola",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=9,column=0,padx=10,pady=10,sticky="w")
        Coca_Cola_txt=Entry(F2,width=2,textvariable=self.Coca_Cola,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=9,column=1,padx=10,pady=10,sticky=W)
        
        # you can use scroll bar here for frame
        
        #bath_shampoo_label=Label(F2,text="Bath Shampoo",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        #bath_shampoo_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        
        #bath_shampoo_label=Label(F2,text="hair oil",font=("times new roman",16,"bold"),fg="black",bg="tomato").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        #bath_shampoo_txt=Entry(F2,width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10)
        
         #----------------->>>>> Groccery frame <<<----------------
        F3=LabelFrame(self.master,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F3.place(x=276,y=152,width=220,height=393)
        
        g1_label=Label(F3,text="ToorDal",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=4,textvariable=self.ToorDal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        g2_label=Label(F3,text="Daawat_Rozana_Basmati_Rice",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=4,textvariable=self.Daawat_Rozana_Basmati_Rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        g3_label=Label(F3,text="Fortune_Chakki_Fresh_Aata",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=4,textvariable=self.Fortune_Chakki_Fresh_Aata,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
            
        g4_label=Label(F3,text="Besan",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=4,textvariable=self.Besan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        g5_label=Label(F3,text="Poha",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=4,textvariable=self.Poha,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        g6_label=Label(F3,text="oats",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=4,textvariable=self.Oats,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        g7_label=Label(F3,text="Muesli",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        g7_txt=Entry(F3,width=4,textvariable=self.Muesli,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10,sticky=W)
        
        
         #----------------->>>>> chocalates_and_sweets frame <<<----------------
        F4=LabelFrame(self.master,bd=10,relief=GROOVE,text="chocalates_and_sweets varible",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F4.place(x=490,y=152,width=220,height=393)
        
        c1_label=Label(F4,text="Cadbury_Silk",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=4,textvariable=self.Cadbury_Silk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F4,text="Ferrero_Rocher",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=4,textvariable=self.Ferrero_Rocher,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F4,text="Kisses_Hersheys",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=4,textvariable=self.Kisses_Hersheys,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F4,text="Haldirams_Patisa",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=4,textvariable=self.Haldirams_Patisa,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F4,text="Besan_Laddoo",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=4,textvariable=self.Besan_Laddoo,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F4,text="Ghee_Gajak_Rolls",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=4,textvariable=self.Ghee_Gajak_Rolls,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        c7_label=Label(F4,text="Gulab_Jamun",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c7_txt=Entry(F4,width=4,textvariable=self.Gulab_Jamun,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10,sticky=W)

        c8_label=Label(F4,text="Rasgulla",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        c8_txt=Entry(F4,width=4,textvariable=self.Rasgulla,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10,sticky=W)
        
        
        #----------------->>>>>  spices_and_seasonings <<<----------------
        F5=LabelFrame(self.master,bd=10,relief=GROOVE,text=" spices_and_seasonings",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F5.place(x=705,y=152,width=230,height=393)
        
        c1_label=Label(F5,text="Turmeric_Powder",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=4,textvariable=self.Turmeric_Powder,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F5,text="Red_Chilli_Powder",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=4,textvariable=self.Red_Chilli_Powder,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F5,text="Corriander_powder",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F5,width=4,textvariable=self.Corriander_powder,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F5,text="Garam_Masala",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F5,width=4,textvariable=self.Garam_Masala,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F5,text="Hing",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=4,textvariable=self.Hing,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F5,text="Salt",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F5,width=4,textvariable=self.Salt,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        c7_label=Label(F5,text="Oregano",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c7_txt=Entry(F5,width=4,textvariable=self.Oregano,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10,sticky=W)

         #----------------->>>>>  Dry_Fruits_and_Snacks <<<----------------
        F10=LabelFrame(self.master,bd=10,relief=GROOVE,text=" Dry_Fruits_and_Snacks",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F10.place(x=705,y=152,width=230,height=393)
        
        c1_label=Label(F10,text="Cashewnut",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F10,width=4,textvariable=self.Cashewnuts,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F10,text="Almonds",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F10,width=4,textvariable=self.Almonds,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F10,text="Raisins",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F10,width=4,textvariable=self.Raisins,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F10,text="Pistachios",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F10,width=4,textvariable=self.Pistachios,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F10,text="walnut",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F10,width=4,textvariable=self.walnut,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F10,text="Lays_American_Style_potato_chips",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F10,width=4,textvariable=self.Lays_American_Style_potato_chips,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        c7_label=Label(F10,text="Haldiram_Bhujia_sev",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c7_txt=Entry(F10,width=4,textvariable=self.Haldiram_Bhujia_sev,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10,sticky=W)

         #----------------->>>>>  Cooking_and_Ready_To_Eat varible <<<----------------
        F11=LabelFrame(self.master,bd=10,relief=GROOVE,text=" Cooking_and_Ready_To_Eat varible",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F11.place(x=705,y=152,width=230,height=393)
        
        c1_label=Label(F11,text="Saffola_Gold_Oil",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F11,width=4,textvariable=self.Saffola_Gold_Oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        c2_label=Label(F11,text="Figaro_Olive_Oil",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F11,width=4,textvariable=self.Figaro_Olive_Oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        c3_label=Label(F11,text="Amul_Ghee",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F11,width=4,textvariable=self.Amul_Ghee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        c4_label=Label(F11,text="Butter",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F11,width=4,textvariable=self.Butter,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        c5_label=Label(F11,text="Maggi",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F11,width=4,textvariable=self.Maggi,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10,sticky=W)
        
        c6_label=Label(F11,text="Pasta",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F11,width=4,textvariable=self.Pasta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10,sticky=W)

        c7_label=Label(F11,text="Oreo_Biscuit",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        c7_txt=Entry(F11,width=4,textvariable=self.Oreo_Biscuit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10,sticky=W)

        c8_label=Label(F11,text="Hide_and_seek_Biscuit",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=7,column=0,padx=10,pady=10,sticky="w")
        c8_txt=Entry(F11,width=4,textvariable=self.Hide_and_seek_Biscuit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1,padx=10,pady=10,sticky=W)

        c9_label=Label(F11,text="Parle_G_Biscuit",font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=8,column=0,padx=10,pady=10,sticky="w")
        c9_txt=Entry(F11,width=4,textvariable=self.Parle_G_Biscuit,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=8,column=1,padx=10,pady=10,sticky=W)



  
        
         #----------------->>>>> image frame <<<----------------
        
        
        
        self.image_section()
        
        
        # bill Area ....................................
        
        F6=LabelFrame(self.master,bd=10,relief=GROOVE)
        F6.place(x=1160,y=152,width=380,height=393)
        bill_title=Label(F6,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
 
        #  bottom button frame----------------------------------
        
        F7=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
        F7.place(x=0,y=540,relwidth=1,height=180)
        
        m1=Label(F7,text="Total Beverage Price",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky=W)
        ml_txt=Entry(F7,width=18,textvariable=self.Beverage_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2=Label(F7,text="Total Grocery Price",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky=W)
        m2_txt=Entry(F7,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
 
        m3=Label(F7,text="Total chocalates_and_sweets Price",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky=W)
        m3_txt = Entry(F7, width=18, textvariable=self.Total, font="arial 10 bold", bd=7, relief=SUNKEN, some_variable_name=chocalates_and_sweets_price).grid(row=2, column=1, padx=10, pady=1)

        m4=Label(F7,text="Total spices_and_seasonings Price",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky=W)
        m4_txt=Entry(F7,width=18,textvariable=self.Toatl ,font="arial 10 bold", bd=7,relief=SUNKEN, some_variable_name= spices_and_seasonings).grid(row=3,column=1,padx=10,pady=1)

        m5=Label(F7,text="Total Dry_Fruits_and_Snacks Price",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=4,column=0,padx=20,pady=1,sticky=W)
        m5_txt=Entry(F7,width=18,textvariable=self.Dry_Fruits_and_Snacks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=1)

        m6=Label(F7,text="Cooking_and_Ready_To_Eat",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=5,column=0,padx=20,pady=1,sticky=W)
        m6_txt=Entry(F7,width=18,textvariable=self.Cooking_and_Ready_To_Eat_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=1)

        

 
        # for tax
        
        tax1=Label(F7,text="Beverage Tax (28%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky=W)
        taxl_txt=Entry(F7,width=18,textvariable=self.Beverage_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        tax2=Label(F7,text="Grocery Tax (5%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky=W)
        tax2_txt=Entry(F7,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
 
        tax3=Label(F7,text="chocalates_and_sweets Tax (40%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky=W)
        tax3_txt=Entry(F7,width=18,textvariable=self.chocalates_and_sweets_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
 
        tax4=Label(F7,text="spices_and_seasonings (5%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky=W)
        tax4_txt=Entry(F7,width=18,textvariable=self.spices_and_seasonings_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=1)

        tax5=Label(F7,text="Dry_Fruits_and_Snacks (5%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=4,column=2,padx=20,pady=1,sticky=W)
        tax5_txt=Entry(F7,width=18,textvariable=self.Dry_Fruits_and_Snacks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=4,column=3,padx=10,pady=1)

        tax6=Label(F7,text="Cooking_and_Ready_To_Eat (5%)",bg="sky blue",fg="black",font=("times new roman",14,"bold")).grid(row=5,column=2,padx=20,pady=1,sticky=W)
        tax6_txt=Entry(F7,width=18,textvariable=self.Cooking_and_Ready_To_Eat_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=5,column=3,padx=10,pady=1)
 
 
        btn_frame=Frame(F7,bd=7,relief=GROOVE)
        btn_frame.place(x=810,y=10,width=700,height=115)
        
        total_btn=Button(btn_frame,command=self.total,text="Total",bg="cyan",bd=5,fg="black",pady=15,width=14,font="arial 12 bold").grid(row=0,column=0,padx=15,pady=15)
 
        genbill_btn=Button(btn_frame,text="Generate Bill",command=self.bill_area,bg="cyan",bd=5,fg="black",pady=15,width=14,font="arial 12 bold").grid(row=0,column=1,padx=15,pady=15)
 
        clear_btn=Button(btn_frame,text="Clear",command=self.clear_data,bg="cyan",bd=5,fg="black",pady=15,width=11,font="arial 12 bold").grid(row=0,column=2,padx=15,pady=15)
 
        exit_btn=Button(btn_frame,text="Exit",command=self.exit_app,bg="cyan",bd=5,fg="black",pady=15,width=11,font="arial 12 bold").grid(row=0,column=3,padx=15,pady=15)
        
        self.welcome_bill()
        #----------------->>>>> bill search frame <<<----------------
        F8=LabelFrame(self.master,bd=10,relief=GROOVE,text="Bill Search ",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F8.place(x=0,y=712,width=350,height=80)
        
        bn_txt=Entry(F8,width=18,textvariable=self.search_bill,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=30,pady=1)
        search_btn=Button(F8,text="Search",command=self.find_bill,bg="cyan",bd=5,fg="black",width=8,font="arial 12 bold").grid(row=0,column=2)
 
           #---------------Admin area-----------------------
        F9=LabelFrame(self.master,bd=10,relief=GROOVE,text="Admin area ",font=("times new roman",15,"bold"),fg="gold",bg="tomato")
        F9.place(x=351,y=712,width=1186,height=80)
            
        
        
        Label(F9,text="Login :  | ",font=("times new roman",15,"bold"),fg="black",bg="sky blue").grid(row=0,column=0)
        Label(F9,text="ID ",font=("times new roman",15,"bold"),fg="black",bg="tomato").grid(row=0,column=1)
        
        admin_id1=Entry(F9,width=25,textvariable=self.admin_id,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=2,sticky=E)
        
        Label(F9,text="  Password",font=("times new roman",15,"bold"),fg="black",bg="sky blue").grid(row=0,column=3)
        
        admin_pass1=Entry(F9,width=18,textvariable=self.admin_pass,font="arial 10 bold",bd=7,relief=SUNKEN,show='X').grid(row=0,column=4,sticky=E)
        
        a_login=Button(F9,text="Login",command=self.login_page,bg="cyan",bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=5,padx=35)
        
        
        #-------sign up----------------
        Label(F9,text="  Create New Account",font=("times new roman",15,"bold"),fg="black",bg="sky blue").grid(row=0,column=6)
        a_sign_up=Button(F9,text="Sign Up",bg="cyan",bd=5,fg="black",width=12,font="arial 12 bold").grid(row=0,column=7,padx=35)
        
 
    def image_section(self):
        img=Image.open("shoping3.jpg")
        pic=ImageTk.PhotoImage(img)
        F5=LabelFrame(self.master,bd=10,relief=GROOVE,bg="sky blue")
        F5.place(x=930,y=152,width=230,height=393)
        
        F5_label=Label(F5,image=pic)
        F5_label.image=pic
        F5_label.pack()
    
    def total(self):
        self.b_gt=self.Green_Tea.get()*25
        self.b_mt=self.Masala_Tea.get()*132#*self.find_price("Masala_Tea",self.Masala_Tea_clicked.get())
        self.b_ht=self.Herbal_Tea.get()*122#*self.find_price("Herbal_Tea",self.Herbal_Tea_clicked.get())
        self.b_nccc=self.Nescafe_classic_coffe.get()*154#*self.find_price("Nescafe_classic_coffe",self.Nescafe_classic_coffe_clicked.get())
        self.b_bic=self.Bru_Instant_Coffe.get()*45#*self.find_price("Bru_Instant_Coffe",self.Bru_Instant_Coffe_clicked.get())
        self.b_rmfj=self.Real_Mixed_Fruit_Juice.get()*78#*self.find_price("Bru_Instant_Coffe",self.Real_Mixed_Fruit_Juice_clicked.get())
        self.b_hhcd=self.Hersheyas_hot_chocolate_drink.get()*67#*self.find_price("Hersheyas_hot_chocolate_drink",self.Hersheyas_hot_chocolate_drink.get())
        self.b_c=self.Curacao.get()*98#*self.find_price("Curacao",self.Curacao.get())
        self.b_rb=self.Red_Bull.get()*123#*self.find_price("Red_Bull",self.Red_Bull_clicked.get())
        self.b_cc=self.Coca_Cola.get()*87#*self.find_price("Coca_Cola",self.Coca_Cola_clicked.get())
        self.total_Beverage_price=float(
                self.b_gt+
                self.b_mt+
                self.b_ht+
                self.b_nccc+
                self.b_bic+
                self.b_rmfj+
                self.b_hhcd+
                self.b_c+
                self.b_rb+
                self.b_cc
                )
        
        self.b_tax=round((self.total_Beverage_price*0.28),2)
        self.cosmetic_price.set("Rs. "+str(self.total_Beverage_price))
        self.Beverage_tax.set("Rs. "+str(self.b_tax))
        
        
        
        self.g_td=self.ToorDal.get()*30
        self.g_drbr=self.Daawat_Rozana_Basmati_Rice.get()*70
        self.g_fcfa=self.Fortune_Chakki_Fresh_Aata.get()*150
        self.g_bs=self.Besan.get()*200
        self.g_ph=self.Poha.get()*100
        self.g_ot=self.Oats.get()*140
        self.g_ms=self.Muesli.get()*150
        
        self.total_grocery_price=float(
                self.g_td+
                self.g_drdr+
                self.g_fcfa+
                self.g_bs+
                self.g_ph+
                self.g_ot+
                self.g_ms
                )
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        
        self.cs_cds=self.Cadbury_Silk.get()*30
        self.cs_fr=self.Ferrero_Rocher.get()*70
        self.cs_kh=self.Kisses_Hersheys.get()*150
        self.cs_hp=self.Haldirams_Patisa.get()*200
        self.cs_bl=self.Besan_Laddoo.get()*100
        self.cs_ggr=self.Ghee_Gajak_Rolls.get()*140
        self.cs_gj=self.Gulab_Jamun.get()*180
        self.cs_rg=self.Rasgulla.get()*90
        
        
        self.total_chocalates_and_sweets_price=float(
                self.cs_cds+
                self.cs_fr+
                self.cs_kh+
                self.cs_hp+
                self.cs_bl+
                self.cs_ggr+
                self.cs_gj+
                self.cs_rg
                )
        
        self.cs_tax=round((self.total_chocalates_and_sweets_price*0.40),2)
        self.chocalates_and_sweets_price.set("Rs. "+str(self.total_chocalates_and_sweets_price))
        self.chocalates_and_sweets_tax.set("Rs. "+str(self.cs_tax))
        
        self.ss_tp=self.Turmeric_Powder.get()*30
        self.ss_ecp=self.Red_Chilli_Powder.get()*70
        self.ss_cp=self.Corriander_powder.get()*150
        self.ss_gm=self.Garam_Masala.get()*200
        self.ss_hn=self.Hing.get()*100
        self.ss_sl=self.salt.get()*70
        self.ss_og=self.Oregano.get()*130
        
        self.total_spices_and_seasonings_price=float(
                self.ss_tp+
                self.ss_ecp+
                self.ss_cp+
                self.ss_gm+
                self.ss_hn+
                self.ss_sl+
                self.ss_og
                )
        
        self.ss_tax=round((self.total_spices_and_seasonings_price*0.05),2)
        self.spices_and_seasonings_price.set("Rs. "+str(self.total_spices_and_seasonings_price))
        self.spices_and_seasonings_tax.set("Rs. "+str(self.ss_tax))
        
        self.ds_cn=self.Cashewnuts.get()*30
        self.ds_al=self.Almonds.get()*70
        self.ds_rs=self.Raisins.get()*150
        self.ds_pt=self.Pistachios.get()*200
        self.ds_wn=self.walnut.get()*100
        self.ds_ls=self.Lays_American_Style_potato_chips.get()*70
        self.ds_hbs=self.Haldiram_Bhujia_sev.get()*130
        
        self.total_spices_and_seasonings_price=float(
                self.ds_cn+
                self.ds_al+
                self.ds_rs+
                self.ds_pt+
                self.ds_wn+
                self.ds_is+
                self.ds_hbs
                )
        
        self.ds_tax=round((self.total_Dry_Fruits_and_Snacks_price*0.05),2)
        self.Dry_Fruits_and_Snacks_price.set("Rs. "+str(self.total_Dry_Fruits_and_Snacks_price))
        self.Dry_Fruits_and_Snacks_tax.set("Rs. "+str(self.ds_tax))

        self.cr_sgo=self.Saffola_Gold_Oil.get()*30
        self.cr_foo=self.Figaro_Olive_Oil.get()*70
        self.cr_ag=self.Amul_Ghee.get()*150
        self.cr_bt=self.Butter.get()*200
        self.cr_mg=self.Maggi.get()*100
        self.cr_pt=self.Pasta.get()*70
        self.cr_ob=self.Oreo_Biscuit.get()*130
        self.cr_hsb=self.Hide_and_seek_Biscuit.get()*70
        self.cr_pgb=self.Parle_G_Biscuit.get()*70
        
        self.total_spices_and_seasonings_price=float(
                self.cr_sgo+
                self.cr_foo+
                self.cr_ag+
                self.cr_bt+
                self.cr_mg+
                self.cr_pt+
                self.cr_ob+
                self.cr_hsn+
                self.cr_pgb
                
                )
        
        self.cr_tax=round((self.total_Cooking_and_Ready_To_Eat_price*0.05),2)
        self.Dry_Fruits_and_Snacks_price.set("Rs. "+str(self.total_Cooking_and_Ready_To_Eat_price))
        self.Cooking_and_Ready_To_Eat_tax.set("Rs. "+str(self.cr_tax))
        
        self.total_bill=float(
                self.total_Beverage_price+
                self.total_grocery_price+
                self.total_chocalates_and_sweets_price+
                self.total_spices_and_seasonings_price+
                self.total_Dry_Fruits_and_Snacks_price+
                self.total_Cooking_and_Ready_To_Eat_price+
                self.b_tax+
                self.g_tax+
                self.cs_tax+
                self.ss_tax+
                self.ds_tax+
                self.cr_tax
                )
        
    def stock_update_after_purchased(self,name,n):
        f1=open("stock.csv","w+",encoding='utf-8-sig')
        for i in f1:
            data=i.split(",")
            if data[0]==name:
                if n<=int(data[1]):
                    x=int(data[1])
                    x=x-n
                    return n
        
        
        
        
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t|| CRP SHOP ||")
        self.txtarea.insert(END,"\n_________________________________________\n")
        self.txtarea.insert(END,f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name :   {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone no.:    {self.c_phon.get()}")
        self.txtarea.insert(END,"\n==========================================")
        self.txtarea.insert(END,"\nProducts\t\t\tQTY\t   Price")
        self.txtarea.insert(END,"\n==========================================")
        
        
    def bill_area(self):
      
       if self.c_name.get()=="" or self.c_phon.get()=="":
           messagebox.showerror("Error","Fill Customer details")
       elif self. Beverage_price=="Rs. 0.0" and self.grocery_price=="Rs. 0.0" and self.chocalates_and_sweets_price=="Rs. 0.0" and self.spices_and_seasonings_price=="Rs. 0.0" and self.Dry_Fruits_and_Snacks_price=="Rs. 0.0"and self.Cooking_and_Ready_To_Eat_price=="Rs. 0.0":
           messagebox.showerror("Error","No product purchased")
       else:
           self.welcome_bill()
           #  Beverage
           if self.Green_Tea.get()!=0:
               self.txtarea.insert(END,f"\nGreen_Tea    \t\t\t{self.Green_Tea.get()}\t    {self.b_gt}")
           if self.Masala_Tea.get()!=0:
               self.txtarea.insert(END,f"\nMasala_Tea \t\t\t{self.nMasala_Tea.get()}\t    {self.b_mt}")
           if self.Herbal_Tea.get()!=0:
               self.txtarea.insert(END,f"\nHerbal_Tea\t\t\t{self.Herbal_Tea.get()}\t    {self.b_ht}")
           if self.Nescafe_classic_coffe.get()!=0:
               self.txtarea.insert(END,f"\nNescafe_classic_coffe\t\t\t{self.Nescafe_classic_coffe.get()}\t    {self.b_nccc}")
           if self.Bru_Instant_Coffe.get()!=0:
               self.txtarea.insert(END,f"\nBru_Instant_Coffe\t\t\t{self.Bru_Instant_Coffe.get()}\t    {self.b_bic}")
           if self.Real_Mixed_Fruit_Juice.get()!=0:
               self.txtarea.insert(END,f"\nReal_Mixed_Fruit_Juice\t\t\t{self.Real_Mixed_Fruit_Juice.get()}\t    {self.b_rmfj}")
           if self.Hersheyas_hot_chocolate_drink.get()!=0:
               self.txtarea.insert(END,f"\nHersheyas_hot_chocolate_drink\t\t\t{self.Hersheyas_hot_chocolate_drink.get()}\t    {self.b_hhcd}")
           if self.Curacao.get()!=0:
               self.txtarea.insert(END,f"\nCuracao\t\t\t{self.Curacao.get()}\t    {self.b_c}")
           if self.Red_Bull.get()!=0:
               self.txtarea.insert(END,f"\nRed_Bull\t\t\t{self.Red_Bull.get()}\t    {self.b_rb}")
           if self.Coca_Cola.get()!=0:
               self.txtarea.insert(END,f"\nCoca_Cola\t\t\t{self.Coca_Cola.get()}\t    {self.b_cc}")
               
            
            #Grocery print
           if self.ToorDal.get()!=0:
               self.txtarea.insert(END,f"\nToorDal   \t\t\t{self.ToorDal.get()}\t    {self.g_td}")
           if self.Daawat_Rozana_Basmati_Rice.get()!=0:
               self.txtarea.insert(END,f"\nDaawat_Rozana_Basmati_Rice     \t\t\t{self.Daawat_Rozana_Basmati_Rice.get()}\t    {self.g_drdr}")
           if self.Fortune_Chakki_Fresh_Aata.get()!=0:
               self.txtarea.insert(END,f"\nFortune_Chakki_Fresh_Aata    \t\t\t{self.Fortune_Chakki_Fresh_Aata.get()}\t    {self.g_fcfa}")
           if self.Besan.get()!=0:
               self.txtarea.insert(END,f"\nFood oil \t\t\t{self.Besan.get()}\t    {self.g_bs}")
           if self.Poha.get()!=0:
               self.txtarea.insert(END,f"\nPoha    \t\t\t{self.Poha.get()}\t    {self.g_ph}")
           if self.Oats.get()!=0:
               self.txtarea.insert(END,f"\nOats     \t\t\t{self.Oats.get()}\t    {self.g_ot}")
           if self.Muesli.get()!=0:
               self.txtarea.insert(END,f"\nMuesli     \t\t\t{self.Muesli.get()}\t    {self.g_ms}")    
    
            
            #chocalates_and_sweets
           if self.Cadbury_Silk.get()!=0:
               self.txtarea.insert(END,f"\nCadbury_Silk  \t\t\t{self.Cadbury_Silk.get()}\t    {self.cs_cds}")
           if self.Ferrero_Rocher.get()!=0:
               self.txtarea.insert(END,f"\nFerrero_Rocher     \t\t\t{self.Ferrero_Rocher.get()}\t    { self.cs_fr}")
           if self.Kisses_Hersheys.get()!=0:
               self.txtarea.insert(END,f"\nKisses_Hersheys \t\t\t{self.Kisses_Hersheys.get()}\t    { self.cs_kh}")
           if self.Haldirams_Patisa.get()!=0:
               self.txtarea.insert(END,f"\nHaldirams_Patisa \t\t\t{self.Haldirams_Patisa.get()}\t    {self.cs_hp}")
           if self.Besan_Laddoo.get()!=0:
               self.txtarea.insert(END,f"\nBesan_Laddoo  \t\t\t{self.Besan_Laddoo.get()}\t    {self.cs_bl}")
           if self.Ghee_Gajak_Rolls.get()!=0:
               self.txtarea.insert(END,f"\nGhee_Gajak_Rolls   \t\t\t{self.Ghee_Gajak_Rolls.get()}\t    { self.cs_ggr}")
           if self.Gulab_Jamun.get()!=0:
               self.txtarea.insert(END,f"\nGulab_Jamun   \t\t\t{self.Gulab_Jamun.get()}\t    {self.cs_gj}")
           if self.Rasgulla.get()!=0:
               self.txtarea.insert(END,f"\nRasgulla   \t\t\t{self.Rasgulla.get()}\t    { self.cs_rg}")    
            

            
            #spices_and_seasonings print
           if self.Turmeric_Powder.get()!=0:
               self.txtarea.insert(END,f"\nTurmeric_Powder     \t\t\t{self.Turmeric_Powder.get()}\t    {self.ss_tp}")
           if self.Red_Chilli_Powder.get()!=0:
               self.txtarea.insert(END,f"\nRed_Chilli_Powder\t\t\t{self.Red_Chilli_Powder.get()}\t    {self.ss_ecp}")
           if self.Corriander_powder.get()!=0:
               self.txtarea.insert(END,f"\nCorriander_powder    \t\t\t{self.Corriander_powder.get()}\t    { self.ss_cp}")
           if self.Garam_Masala.get()!=0:
               self.txtarea.insert(END,f"\nGaram_Masala\t\t\t{self.Garam_Masala.get()}\t    { self.ss_gm}")
           if self.Hing.get()!=0:
               self.txtarea.insert(END,f"\nHing   \t\t\t{self.Hing.get()}\t    {self.ss_hn}")
           if self.Salt.get()!=0:
               self.txtarea.insert(END,f"\nSalt   \t\t\t{self.Salt.get()}\t    {self.ss_sl}")
           if self.Oregano.get()!=0:
               self.txtarea.insert(END,f"\nOregano   \t\t\t{self.Oregano.get()}\t    {self.ss_og}")

               #  Dry_Fruits_and_Snacks
           if self.Cashewnuts.get()!=0:
               self.txtarea.insert(END,f"\nCashewnuts   \t\t\t{self.Cashewnuts.get()}\t    {self.ds_cn}")
           if self.Almonds.get()!=0:
               self.txtarea.insert(END,f"\nAlmonds\t\t\t{self.nAlmonds.get()}\t    {self.ds_al}")
           if self.Raisins.get()!=0:
               self.txtarea.insert(END,f"\nRaisins\t\t\t{self.Raisins.get()}\t    {self.ds_rs}")
           if self.Pistachios.get()!=0:
               self.txtarea.insert(END,f"\nPistachios\t\t\t{self.Pistachios.get()}\t    {self.ds_pt}")
           if self.walnut.get()!=0:
               self.txtarea.insert(END,f"\nwalnut\t\t\t{self.walnut.get()}\t    {self.ds_wn}")
           if self.Lays_American_Style_potato_chips.get()!=0:
               self.txtarea.insert(END,f"\nLays_American_Style_potato_chips\t\t\t{self.Lays_American_Style_potato_chips.get()}\t    {self.ds_is}")
           if self.Haldiram_Bhujia_sev.get()!=0:
               self.txtarea.insert(END,f"\nHaldiram_Bhujia_sev\t\t\t{self.Haldiram_Bhujia_sev.get()}\t    {self.ds_hbs}")

                #  Cooking_and_Ready_To_Eat
           if self.Saffola_Gold_Oil.get()!=0:
               self.txtarea.insert(END,f"\nSaffola_Gold_Oil   \t\t\t{self.Saffola_Gold_Oil.get()}\t    {self.cr_sgo}")
           if self.Figaro_Olive_Oil.get()!=0:
               self.txtarea.insert(END,f"\nFigaro_Olive_Oil \t\t\t{self.nFigaro_Olive_Oil.get()}\t    {self.cr_foo}")
           if self.Amul_Ghee.get()!=0:
               self.txtarea.insert(END,f"\nAmul_Ghee\t\t\t{self.Amul_Ghee.get()}\t    {self.cr_ag}")
           if self.Butter.get()!=0:
               self.txtarea.insert(END,f"\nButter\t\t\t{self.Butter.get()}\t    {self.cr_bt}")
           if self.Maggi.get()!=0:
               self.txtarea.insert(END,f"\nMaggi \t\t\t{self.Maggi.get()}\t    {self.cr_mg}")
           if self.Pasta.get()!=0:
               self.txtarea.insert(END,f"\nPasta\t\t\t{self.Pasta.get()}\t    {self.cr_pt}")    
           if self.Oreo_Biscuit.get()!=0:
               self.txtarea.insert(END,f"\nOreo_Biscuit\t\t\t{self.Oreo_Biscuit.get()}\t    {self.cr_ob}")
           if self.Hide_and_seek_Biscuit.get()!=0:
               self.txtarea.insert(END,f"\nHide_and_seek_Biscuit\t\t\t{self.Hide_and_seek_Biscuit.get()}\t    {self.cr_hsn}")
           if self.Parle_G_Biscuit.get()!=0:
               self.txtarea.insert(END,f"\nParle_G_Biscuit\t\t\t{self.Parle_G_Biscuit.get()}\t    {self.cr_pgb}")

               
           
            
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           if self.Beverage_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nBeverage Tax\t\t\t       {self.Beverage_tax.get()}")
           if self.grocery_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nGrocery  Tax\t\t\t       {self.grocery_tax.get()}")
           if self.chocalates_and_sweets_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nchocalates_and_sweets  Tax\t\t\t       {self.chocalates_and_sweets_tax.get()}")
           if self.spices_and_seasonings_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nspices_and_seasonings Tax\t\t\t      {self.spices_and_seasonings_tax.get()}")
           if self.Dry_Fruits_and_Snacks_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nDry_Fruits_and_Snacks Tax\t\t\t      {self.Dry_Fruits_and_Snacks_tax.get()}")
           if self.Cooking_and_Ready_To_Eat_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nCooking_and_Ready_To_Eat\t\t\t      {self.Cooking_and_Ready_To_Eat.get()}")
          
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
           self.txtarea.insert(END,f"\nTotal Bill :\t\t\t      Rs. {str(self.total_bill)}")
           self.txtarea.insert(END,"\n`````````````````````````````````````````")
          
           self.save_bill()
      
    def save_bill(self):
        op=messagebox.askyesno("save bill","Do you want to save the bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
            fp1.write(self.bill_data)
            fp1.close()
            messagebox.showinfo("Saved",f"Bill No. :{self.bill_no.get()} Saved successfuly")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,f1.read())
                f1.close()
                present="yes"
                
                
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
 
        
    def clear_data(self):
        #    Beverage variable
        op=messagebox.askyesno("Exit","Do you want to Exit")
        if op>0:
            self.Green_Tea.set(0)
            self.Masala_Tea.set(0)
            self.Herbal_Tea.set(0)
            self.Nescafe_classic_coffe.set(0)
            self.Bru_Instant_Coffe.set(0)
            self.Real_Mixed_Fruit_Juice.set(0)
            self.Hersheyas_hot_chocolate_drink.set(0)
            self.Curacao.set(0)
            self.Red_Bull.set(0)
            self.Coca_Cola.set(0)
            
            
            # grocery varible
            self.ToorDal.set(0)
            self.Daawat_Rozana_Basmati_Rice(0)
            self.Fortune_Chakki_Fresh_Aata.set(0)
            self.Besan.set(0)
            self.Poha.set(0)
            self.Oats.set(0)
            self.Muesli.set(0)
            
            
            # chocalates_and_sweets
            self.Cadbury_Silk.set(0)
            self.Ferrero_Rocher.set(0)
            self.Kisses_Hersheys.set(0)
            self.Haldirams_Patisa.set(0)
            self.Besan_Laddoo.set(0)
            self.Ghee_Gajak_Rolls.set(0)
            self.Gulab_Jamun.set(0)
            self.Rasgulla.set(0)
            
            # spices_and_seasonings
            
            self.Turmeric_Powder(0)
            self.Red_Chilli_Powder.set(0)
            self.Corriander_powder.set(0)
            self.Garam_Masala.set(0)
            self.Hing.set(0)
            self.Salt.set(0)
            self.Hing.set(0)
            self.Oregano.set(0)

            # Dry_Fruits_and_Snacks
            
            self.Cashewnuts(0)
            self.Almonds.set(0)
            self.Corriander_powder.set(0)
            self.Raisins.set(0)
            self.Pistachios.set(0)
            self.walnut.set(0)
            self.Lays_American_Style_potato_chips.set(0)
            self.Haldiram_Bhujia_sev.set(0)

            # Cooking_and_Ready_To_Eat
            
            self.Saffola_Gold_Oil(0)
            self.Figaro_Olive_Oil.set(0)
            self.Amul_Ghee.set(0)
            self.Butter.set(0)
            self.Maggi.set(0)
            self.Pasta.set(0)
            self.Oreo_Biscuit.set(0)
            self.Parle_G_Biscuit.set(0)
            
            #product price varible
            
            self.Beverage_price.set("")
            self.grocery_price.set("")
            self.chocalates_and_sweets_price.set("")
            self.spices_and_seasonings_price.set("")
            self.Dry_Fruits_and_Snacks_price.set("")
            self.Cooking_and_Ready_To_Eat_price.set("")
            
            # tax varible
            
            self.Beverage_tax.set("")
            self.grocery_tax.set("")
            self.chocalates_and_sweets_tax.set("")
            self.spices_and_seasonings_tax.set("")
            self.Dry_Fruits_and_Snacks_tax.set("")
            self.Cooking_and_Ready_To_Eat_tax.set("")
            
            #customer details
            
            self.c_name.set("")
            self.c_phon.set("")
            self.c_mail.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.welcome_bill()
    
        else:
            return
                
        
    def exit_app(self):
        op1=messagebox.askyesno("Exit","Do you want to Exit")
        if op1>0:
            root.destroy()
        else:
            return
    
    def check_mail(self):
        txt_msg= self.send_email_bill()
        messagebox.showinfo("Sent",f"Bill No. :{self.bill_no.get()} Sent successfuly")
        
        
#     def send_email_bill(self):
#         get_3 = self.c_mail.get()
#         store_get_3 = get_3
        
#         op=messagebox.askyesno("Send bill","Do you want to Send the bill ?")
#         if op>0:
#             self.bill_data=self.txtarea.get('1.0',END)
            #fp1=open("bills/"+str(self.bill_no.get())+".txt","w")
#             msg=self.bill_data
#         else:
#             return  
#         get_4 = msg
#         store_get_4 = get_4
    
        
#         try:
#             server = smtplib.SMTP('smtp.gmail.com', 587)
#             server.ehlo()
#             server.starttls()
#             server.login("ENTER YOUR EMAIL","Password") # you should enter your email and password
#             server.sendmail("shopcrp040@gmail.com",store_get_3,store_get_4)
#             statement_1 = "MAIL HAS BEEN SENT"
#             return statement_1
#         except:
#             statement_2 = "SOMETHING WENT WRONG"
#             return statement_2*/
    def login_page(self):
        ad_id=self.admin_id.get()
        ad_pass=self.admin_pass.get()
        if(ad_id=="crpshop123"):
            if(ad_pass=="123456789"):
                global login_window
                login_window=Tk()
                
                obj1=login_page_window(login_window)
                
                
                
                login_window.mainloop()
            else:
                messagebox.showerror("Error","invalid password")
        else:
            messagebox.showerror("Error","invalid User id")
                
class login_page_window:
    def __init__(self, master1):
        self.master1=master1
        self.master1.geometry("1920x1080+-10+0")
        self.master1.title("Admin Area")
 
        title=Label(self.master1,text="CRP SHOP MANAGEMENT",bd=12,relief=GROOVE,bg="sky blue",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        #self.image_section2()
        
        F0=LabelFrame(self.master1,bd=10,relief=GROOVE,bg="orange red")
        F0.place(x=0,y=73,height=60,width=1537)
        F1=LabelFrame(self.master1,bd=10,relief=GROOVE,text="MENU",font=("times new roman",15,"bold"),fg="black",bg="sky blue")
        F1.place(x=0,y=133,width=230,height=600)
        
        today_sell=Button(F1,text="Today's Sell",bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=0,column=0,padx=10,pady=15)
        
        total_sell=Button(F1,text="Total Sell",bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=1,column=0,padx=10,pady=15)
        
        stock=Button(F1,text="Stock",command=self.check_stock,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=2,column=0,padx=10,pady=15)
        
        update_stock=Button(F1,text="Update Stock",command=self.Update_stock,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=3,column=0,padx=10,pady=15)
        
        change_password=Button(F1,text="Change password",bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=4,column=0,padx=10,pady=15)
        
        lis_of_bill=Button(F1,text="Bill List",command=self.bill_list,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=5,column=0,padx=10,pady=15)
        
        clear=Button(F1,text="Clear",command=self.clear_admin_notebook,bg="cyan",bd=5,fg="black",width=15,font="arial 12 bold").grid(row=6,column=0,padx=10,pady=15)
        
        
        
        F3=LabelFrame(self.master1,bd=10,text="Bottom",relief=GROOVE,bg="sky blue")
        F3.place(x=0,y=733,width=1537,height=60)
        
        
        
        
        # Notepad Area ....................................
        
        F4=LabelFrame(self.master1,bd=10,relief=GROOVE)
        F4.place(x=780,y=133,width=757,height=600)
        bill_title=Label(F4,text="Notepad Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        scrol_y=Scrollbar(F4,orient=VERTICAL)
        self.txtarea=Text(F4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.welcome_bill_admin()
        
        
        
        #---------------------------------------------
        
        
        
        
        
        
        img1=Image.open("onlineshop1.jpg")
        pic1=ImageTk.PhotoImage(img1)
        F2=LabelFrame(self.master1,bd=10,relief=GROOVE,bg="sky blue")
        F2.place(x=230,y=133,width=550,height=600)
        
        F2_label1=Label(F2,image=pic1)
        F2_label1.image=pic1
        F2_label1.pack()
        # isko resolve krne k liye ek method hai ki close privious window and open this
        
        #F2=LabelFrame(self.master1,bd=10,text="image",relief=GROOVE,bg="tomato")
        #F2.place(x=230,y=133,width=550,height=600)
        
    def welcome_bill_admin(self):
            
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\t\t\t\t\t|| CRP SHOP ||")
            self.txtarea.insert(END,"\n_________________________________________________________________________________________\n")
    def check_stock(self):
        
        self.txtarea.delete('1.0',END)
        
        self.welcome_bill_admin()
        
        f1=open("stock.csv","r",encoding='utf-8-sig')
        
        #self.txtarea.insert(END,f1.read())
        self.txtarea.insert(END,"|| Product    || \t\t\t\t\t\t\t\t ||Quantity")
        self.txtarea.insert(END,"\n_________________________________________________________________________________________\n")
        for i in f1:
            data=i.split(",")
        #    print((data[0],data[1]))
            
            self.txtarea.insert(END,"\n"+data[0]+"\t\t\t\t\t\t\t\t "+data[1])
        
        f1.close()
    def clear_admin_notebook(self):
        self.txtarea.delete('1.0',END)
        self.welcome_bill_admin()
    
    def bill_list(self):
        
        j=1
        self.txtarea.insert(END,"S.No.\t Bill \n\n")
        for i in os.listdir("bills/"):
           self.txtarea.insert(END,str(j)+".\t"+str(i)+"\n\n")
           j+=1
    def Update_stock(self):
        #os.startfile('stock.csv','r')            
         p=Popen('stock.csv',shell=True)      
        
        
        
global root      
root=Tk()
 
#obj=login_page_window(root)      
obj = Bill_App(root)
root.mainloop()

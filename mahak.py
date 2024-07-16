

def menu(): 
    
    print('*************************************************')
    print('*****MAIN MENU*****')
    print('*****MAIN MENU*****')
    print('1. Starter Course')
    print('2. Main Course')
    print('3. Deserts')
    print('4. Drinks')
    print()
    x=input('Enter Your Choice')
    print()
    return x
 

   
 def Starter_course():
    
    print('Welcome to the Starter Course')
    print()
    global tamt
    while True:
        print('Enter VS for Veg Starter')
        print('Enter NVS for Non_Veg Starter')
        print('Enter M for MAIN MENU')
        print('Enter Q for Quit')
        print()
        l=input('Enter Your Choice')
        print()
        if l=='VS':
            A=pd.read_excel('VEG STARTER.xlsx')
            print(A)
            print()
            x=int(input('Choose Your Veg Starter From the above list'))
            y=int(input('Enter the number of Veg Starter you want'))
            print()
            if x=='PANEER TIKKA' or x=='DAHI KEBAB':
                tamt=tamt+y*100
            if x=='CHILLI PANEER' or x=='GHAMAN DHOKLA':
                tamt=tamt+y*140
            if x=='FRENCH FRIES' or x=='SPRING ROLLS':
                tamt=tamt+y*80
            if x=='MOMOS' or x=='CHILI POTATO':
                tamt=tamt+y*70
            if x=='CHEESE DOSA' or x=='VADA PAV':
                tamt=tamt+y150
            print('Total Amount Till Now',tamt)
            print()
        if l=='NVS':
            B=pd.read_excel('NON VEG STARTER.xlsx')

            print(B)
            print()
            x=int(input('Choose Your Veg Starter From the above list'))
            y=int(input('Enter the number of Veg Starter you want'))
            print()
            if x=='CHICKEN TIKKA' or x=='BUTTER CHICKEN':
                tamt=tamt+y*120
            if x=='CHICKEN SEEKH KEBAB' or x=='HYDERABAADI BRYANI':
                tamt=tamt+y*140
            if x=='FISH FRY' or x=='PRAWN NOODLES':
                tamt=tamt+y*80
            if x=='CHICKEN 65' or x=='TANDOORI CHICKEN':
                tamt=tamt+y*150
            if x=='PERRI PERRI FISH ' or x=='CHICKEN KORAM':
                tamt=tamt+y*160
            
            
            print('Total Amount Till Now',tamt)
            print()
            if l=='Q':
                return Q
            if l=='M':
                return M


def Main_Course():
    print('******************************************************')
    print('Welcome To The Main Course')
    print()
    global tamt
    while True:
        print('Enter I For Indian Cuisine')
        print('Enter C For Chinese Cuisine')
        print('Enter M for Main Menu')
        print('Enter Q for Quit')
        print()
        l=input('Enter Your Choice')
        if l=='I':
            print('INDIAN DISHES')
            D=pd.read('INDIAN COURSE.xlsx')
            print(D)
            print()
            x=int(input('Choose Your Indian Dish from the above list'))
            y=int(input('Enter the number of Dishes You Want'))
            print()
            if x=='BIRYANI' or x=='ROGAN JOSH':
                tamt=tamt+y*100
            if x=='MUGHLAI CHICKEN' or x=='DAL MAKHNI':
                tamt=tamt+y*120
            if x=='MALIA KOFTA' or x=='CHICKEN ALFREZI':
                tamt=tamt+y*130
            if x=='KATI ROLLS' or x=='LITTI CHOKA':
                tamt=tamt+y*150
            if x=='UNDHIYU' or x=='DAAL BHATI CHURMA':
                tamt=tamt+y*200
            print('Total Amount Till Now',tamt)
            print()
            if l=='C': 
                E=pd.read('CHINESE COURSE.xlsx')
                print(E)
                print('csv')
                print()
                x=int(input('Choose Your Indian Dish from the above list'))
                y=int(input('Enter the number of Dishes You Want'))
                print()
                if x=='DIM SUMS' or x=='SPRING ROLLS':
                    tamt=tamt+y*90
                if x=='SZCHWAN CHILLI CHICKEN'or x=='STIR FRIED TOFU':
                    tamt=tamt+y*100
                if x=='SWEET AND SOUR PORK' or x=='MANCHURIAN':
                    tamt=tamt+y*200
                if x=='MDUMPLINGS' or x=='MANCHOW SOUP':
                    tamt=tamt+y*150
                if x=='HAKKA NOODLES' or x=='SHOW MEIN':
                    tamt=tamt+y*140
                print('Total Amount Till Now',tamt)
                print()
                if l=='Q':
                    return Q

                if l=='M':
                    return M


def Deserts():
    
    print('*******************')
    print('Welcome To The Delicious Deserts Section')
    print()
    global tamt
    while True:
        print('Enter D for Deserts')
        print('Enter M for Main Menu')
        print('Enter Q for Quit')
        print()
        l=input('Enter Your Choice')
        if l=='D':
            F=pd.readexcel('DESERTS.xlsx')
            print(F)
            print()
            x=int(input('Choose Your Favourite Desert the above list'))
            y=int(input('Enter the number of Desert you want'))
            print()
            if x=='RAS MALAI' or x=='RASGULLA':
                tamt=tamt+y*60
            if x=='JALEBI' or x=='LADDDU':
                tamt=tamt+y*70
            if x=='KHEER' or x=='GAJAR KA HALWA':
                tamt=tamt+y*100
            if x=='KAJU KATLI' or x=='SWEET VERMICELLI':
                tamt=tamt+y*120
            if x=='KULFI' or x=='SWANDESH':
                tamt=tamt+y*90
            print('Total Amount Till Now',tamt)
            print()

            if l=='Q':
                return Q
            if l=='M':
                return M


def drinks():
    global tamt
    while True:
        print('Enter D for Deserts')
        print('Enter M for Main Menu')
        print('Enter Q for Quit')
        print()
        l=input('Enter Your Choice')
        print()
        if l=='DR':
            
            print('REFRESHING DRINKS')
        
            G=pd.read_excel('DRINKS.xlsx')
            print(G)
            x=input('Enter Your Drink From the above list')
            y=input('Enter the number of Drinks you want')
            print()
            if x=='TEA' or x=='COFFEE':
                tamt=tamt+y*100
            if x=='MARGARITA' or x=='MARTINI':
                tamt=tamt+y*150
            if x=='MIMOSA' or x=='VODKA':
                tamt=tamt+y*170
            if x=='RUM' or x=='LEMONADE':
                tamt=tamt+y*180
            if x=='WHISKEY' or x=='TEQUILA':
                tamt=tamt+y*200
            print('Total Amount Till Now',tamt)
            print()
            if l=='Q':
                return Q
            if l=='M':
                return M

# def most_famous ():
#     x=['TEA','SWEET VERMICELLI','DIM SUMS','MUGHLAI CHICKEN','BUTTER PANEER','RAS MALAI','CHEESE DOSA']
#     Y=[80,50,60,65,70,89,63,75]
#     plt.plot(x,y)
#     plt.xlabel('DISHES NAME')
#     plt.ylabel('PERCENTAGE')
#     plt.title('MOST FAMOUS DISHES')

# def Amount():
#     global tamt
#     print('*****BILL*****')
#     print('TOTAL AMOUNT',tamt)
#     print('vat=14.5')
#     vat=round(14.5/100*tamt,0)
#     print('TOTAL VAT',vat)
#     print('Total Amount To Be Paid',(tamt+vat))
#     print()
#     print('Thanks For Coming To The Townberry Restaurant')
#     print('Your Pleasure Our Comfort')
#     print('Please Visit Again')


# tamt=0
# vat=14.5
# print('******************Welcome To The Townberry Restaurant*****************')
# print()
# print('Made BY Sonam Patel and Shraddha Rathore')
# print()
# m=menu()
# while True:
    
#     if m==1 or m=='Starter Course':
#         st=Starter_Course()
#         if st=='Q':
#             amount()
#             break
#     if m==2 or m=='Main Course':
#         iv=Main_Course()
#         if iv=='Q':
#             amount()
#             break
#     if m==3 or m=='Deserts':
#         de=Deserts()
#         if de=='Q':
#             amount()
#             break
#     if m==4 or m=='Drinks':
#         dr=Drinks()
#         if dr=='Q':
#             amount()
#             break
            
            
            
            


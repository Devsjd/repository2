import numpy as np
num_accounts = int(input("tedad hesabi ke mikhay ra vared kon :\n "))
#لیست نام صاحبان حساب
names = []
#ارایه موجودی ها 
mojodiha = np.zeros(num_accounts)
#دریافت اطلاعات حساب ها
for i in range (num_accounts):
    name = input(f"name saheb hesab {i+1} ra vared kon : \n")
    #این برای موجودی حساب هر نامی که وارد کردیم
    mojodi=int(input(f"mojodi avalie {name} ra vared kon : \n"))
    names.append(name)
    mojodiha[i]=mojodi

#عملیات بانکی
while True:
    print("1 : namayesh mojodi hame hesab ha\n")
    print("2 : seporde gozari dar hesab ha\n")
    print("3 : bardasht az hesab\n")
    print("4 : namayesh hesab ha ba bishtar az mojodi miangin\n")
    print("5 : exit")
    choise=input("yek adad 1-5 ra entekhab kon : ")
    if choise=="1":
        print("list hesab ha va mojodi ha : \n")
        for i in range(num_accounts):
            print(f"{names[i]} : {mojodiha[i]}\n")
    elif choise=="2":
        name_hesab_seporde=input("name hesab baray seporde ra vared kon : ")
        mablagh_seporde=int(input("mablagh seporde ra vared kon : "))
        #اگه نام سپرده توی اون اسم ها بود
        if name_hesab_seporde in names:
            #ایندکس ارایه نام رو توی متغیر ایندکس میریزه
            idx=names.index(name_hesab_seporde)
            mojodiha[idx]+=mablagh_seporde
            print(f"{mablagh_seporde} : be hesab {name_hesab_seporde} variz shod.")
        else: 
            print("hesab peida nashod")
    elif choise=="3":
        name_hesab_seporde=input("name hesab baray bardasht : ")
        mablagh_bardasht=input(input(f"mablagh bardasht az hesab {name_hesab_seporde} ra vared kon: "))
        if name_hesab_seporde in names:
            idx=names.index(name_hesab_seporde)
            if mojodiha[idx]>=mablagh_bardasht :
                mojodiha[idx]-=mablagh_bardasht   
                print(f"mablagh{mablagh_bardasht} az hesab {name_hesab_seporde} bardasht shod")
            else:
                print("mojodi kafi nist")
        else:
            print("hesab peida nashod") 
    elif choise == "4":
        avg_mojodiha=np.mean(mojodiha)
        print(f"miangin hesab ha = {avg_mojodiha}\n")
        print("hesab hay bishtar az mojodi miangin = ")
        for i in range (num_accounts):
            if mojodiha[i]>avg_mojodiha:
                print(f"{names[i]} : {mojodiha[i]}")
    elif choise=="5":
        print("exit")
        break
    else: 
        print("adad na motabar ast . ")            




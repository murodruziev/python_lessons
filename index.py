#ism = input('Ismingizni kiriting?: ')
#if ism.lower() == 'jonik':
#    print('Salom Jonik')
#else:
#    print('Uzur biz Jonikni kutyapmiz')

#____

#yil = int(input('Tugilgan yilingizni kiriting: '))
#if 2023-yil < 18:
#    print('Yoshingiz', 2023-yil, 'da ekan')
#    print('Sizga kirish mumkin emas')
#else:
#    print('Xush kelibsiz!')
#____

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
# if choy:
# print('Mijoz choy oldi')
# narh = narh + 3000
# if salat:
# print('Mijoz salat oldi')
# narh = narh + 5000
# if non:
# print('Mijoz non oldi')
# narh = narh + 3000
# if kompot:
# print('Mijoz kompot oldi')
# narh = narh + 7000
# if assorti:
# print('Mijoz assorti oldi')
# narh = narh + 5000
#
# print('Jami', narh, 'so\'m')

menu = ['osh', 'somsa', 'shorva', 'qazonkabob', 'shashlik']
buyurtmalar = ['osh']

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print('Menuda', taom, 'bor')
        else:
            print('Kechirasiz menuda', taom, 'yoq')
else:
    print('Savatchangiz bosh')
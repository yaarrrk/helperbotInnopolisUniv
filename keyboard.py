import urllib
from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


btnHello = KeyboardButton('/Голова')
btnHello1 = KeyboardButton('/Шея')
btnhello2 = KeyboardButton('/Боль_в_плечах')
btnhello3 = KeyboardButton('/боль_в_районе_бидцепсов')
btnhello4 = KeyboardButton('/Боль_в_районе_груди')
btnhello5 = KeyboardButton('/Боль_в_животе')
btnHello6 = KeyboardButton('/Боль_в_районе_бедер')
btnHello7 = KeyboardButton('/Геолокация')
btnHello8 = KeyboardButton('/Болят_икры')
btnHello9 = KeyboardButton('/Болит_кисть_ноги')
btnhello10 = KeyboardButton('/start')
greet = ReplyKeyboardMarkup().add(btnHello)
greet.add(btnHello1)
greet.add(btnhello2)
greet.add(btnhello3)
greet.add(btnhello4)
greet.add(btnhello5)
greet.add(btnHello6)
greet.add(btnHello7)
greet.add(btnHello8)
greet.add(btnHello9)
greet.add(btnhello10)




analgin = InlineKeyboardButton(text = 'Анальгин', url = 'https://planetazdorovo.ru/catalog/lekarstva-i-bad/analgetiki-spazmolitiki/analgin-tab-500mg-2897/?utm_referrer=https%3A%2F%2Fwww.google.com%2F')
paracetamol = InlineKeyboardButton(text = 'Парацетамол', url = 'https://planetazdorovo.ru/catalog/lekarstva-i-bad/prostuda-i-gripp/temperatura/paracetamol-tab-500mg-17594/')
pandol = InlineKeyboardButton(text = 'Панадол', url = 'https://www.eapteka.ru/goods/drugs/pain/fever/panadol_glaksosmitklyayn/')
golova = InlineKeyboardMarkup().add(analgin)
golova.add(paracetamol)
golova.add(pandol)









naiz_gel = InlineKeyboardButton(text = 'Гель Найз', url = 'https://planetazdorovo.ru/catalog/lekarstva-i-bad/sustavy-i-myshtsy/bol-i-vospalenie/najz-gel-1-50g-3858307/')
voltaren = InlineKeyboardButton(text = 'Вольтарен', url = 'https://planetazdorovo.ru/brand/voltaren-464/')
ketonal = InlineKeyboardButton(text = 'Кетонал', url = 'https://planetazdorovo.ru/catalog/lekarstva-i-bad/sustavy-i-myshtsy/bol-i-vospalenie/ketonal-tab-p-ob-14310/')
sheya = InlineKeyboardMarkup().add(naiz_gel)
sheya.add(voltaren)
sheya.add(ketonal)



amelotex = InlineKeyboardButton(text = 'Амелотекс', url = 'https://www.eapteka.ru/goods/drugs/other/inflammation/ameloteks_soteks/')
artrozan = InlineKeyboardButton(text = 'Артрозан', url = 'https://www.eapteka.ru/goods/drugs/other/inflammation/artrozan_farmstandart/')
diclofenak = InlineKeyboardButton(text = 'Диклофенак', url='https://www.eapteka.ru/goods/id229790/')


plech = InlineKeyboardMarkup().add(amelotex)
plech.add(artrozan)
plech.add(diclofenak)

nurafen_forte = InlineKeyboardButton(text='Нурафен Форте', url='https://www.eapteka.ru/goods/id207893/?utm_referrer=https%3a%2f%2fwww.google.com%2f')
antigrippin = InlineKeyboardButton(text = 'АнтиГриппин', url='https://www.eapteka.ru/goods/beauty/aromaterapiya/masla_efirnye/antigrippin_natur_produkt/')
strepsils = InlineKeyboardButton(text='Стрепсилс', url='https://www.eapteka.ru/goods/drugs/otolaryngology/infection/strepsils_rekitt_benkizer/')

gryt = InlineKeyboardMarkup().add(nurafen_forte)
gryt.add(antigrippin)
gryt.add(strepsils)

drotaverin = InlineKeyboardButton(text='Дротаверин(требуется прочитать инструкцию)', url = 'https://planetazdorovo.ru/catalog/lekarstva-i-bad/pishchevaritelnyy-trakt/spazmolitiki/drotaverin-tab-40mg-247/')
mezim_forte = InlineKeyboardButton(text='Мезим Форте', url='https://planetazdorovo.ru/catalog/lekarstva-i-bad/pishchevaritelnyy-trakt/fermenty/mezim-forte-tab-57/')
almagel = InlineKeyboardButton(text='Алмагель', url = 'https://www.eapteka.ru/kazan/goods/drugs/gasroenterology/almagel/?utm_referrer=https%3a%2f%2fwww.google.com%2f')

zshivot = InlineKeyboardMarkup().add(drotaverin)
zshivot.add(mezim_forte)
zshivot.add(almagel)



aceklofenak = InlineKeyboardButton(text='Ацеклофенак', url = 'https://www.eapteka.ru/goods/drugs/pain/analgesics/atseklofenak/')
ibuprofen = InlineKeyboardButton(text='Ибупрофен', url = 'https://www.eapteka.ru/goods/id221966/')
indometacin = InlineKeyboardButton(text='Индометацин', url = 'https://www.eapteka.ru/goods/id224074/')
nogi = InlineKeyboardMarkup().add(aceklofenak)
nogi.add(ibuprofen)
nogi.add(indometacin)



markup_requests = ReplyKeyboardMarkup().add(KeyboardButton('Отправить свой контакт', request_contact=True)).add(KeyboardButton('Оправить свою геолокацию', request_location=True)).add(KeyboardButton('/start'))
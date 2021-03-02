print("Welcome and enjoy the party")
soal_soal = input('kesini dan tulis jawaban yg benar yes/no : ')
score = 0
total_q = 5

if soal_soal.lower() == 'yes':
    soal_soal = input('1. merk hp abang adalah? A.asus B.samsung C.huawei D.vivo E.Rog: ')
    if soal_soal.lower() == 'a':
        score +=1
        print('corecct')
    elif soal_soal.lower() == 'e':
        print('aminn smoga kebeli')
    else:
        print('salahhhh')

    soal_soal = input('2. merk hp dira adalah? A.samsung B.gk punya hp C.asus D.dira jdi jelek: ')
    if soal_soal.lower() == 'c':
        print('anda sangat jelek')
        score += 1
    elif soal_soal.lower() == 'b' or 'd':
        print('baguss')
    else:
        print('anda cakap sekalaehh')

    soal_soal = input('3. dira kelas berapa? A.999 B.1 C.0 D.123456789 D.7: ')
    if soal_soal.lower() == 'd':
        print('anda benar')
        score += 1
    elif soal_soal.lower() == 'a' or 'b' or 'c':
        print('boleh lah boleh lah')
    else:
        print('tulisanya tuh a b c atau d bukan selain ituuu!!!')

    soal_soal = input('4. merk laptop abang adalah? A.asus rog B.vivo C.gada D.minjem: ')
    if soal_soal.lower() == 'a':
        print('anda sangat betullll')
        score += 1
    elif soal_soal.lower() == 'b':
        print('ew')
    else:
        print('heleh mana ada')
        print('saye punye lahh')

    soal_soal = input('5. 15+15? A.1 B.2 C.30 D.12: ')
    if soal_soal.lower() == 'c':
        print('anda benar')
        print('soalnya kegampangan')
        score += 1
    elif soal_soal.lower() == 'a':
        print('boleh dech')
    else:
        print('anda bodoh sekali')
        print('banyak belajar makanya!!')
else:
    print('huuuu gmau main')
nilai = (score/total_q) * 10
print('selamat anda telah selesai mengerjakan tugas-tugas yg diberikan nilai  anda adalah ', nilai)
print("good bye")


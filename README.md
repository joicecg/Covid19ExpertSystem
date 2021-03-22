# Covid19ExpertSystem
Covid-19 Expert System Build Using Python and Experta

## Requirement
- Python
- Experta - install `pip install experta`
https://pypi.org/project/experta/

## Cara pengunaan
- Pertama install python lalu install experta dengan cara `pip install experta`
- Setelah experta dan python terinstall
- Buka terminal dan run covid19expertsystem.py dengan cara `python covid19expertsystem.py`
- Anda akan masuk ke menu utama dan diminta untuk menjawab pertanyaan
- Untuk pertanyaan pertama silahkan jawab dengan range int(1-31)
- Untuk pertanyaan kedua sampai selanjutnya silahkan jawab dengan 'Ya' atau 'Tidak'

## Sumber data
- https://www.bbc.com/pidgin/tori-55696995
- https://www.alodokter.com/malaria/pengobatan

## Gejala
- Malaria
 - Benar : Batuk, Demam, Nyeri otot, Muntah-muntah, Pusing
- Covid-19 (tanpa interaksi)
 - Benar : Semua gejala jika lebih dari 4 gejala
- Covid-19 (interaksi)
 - Benar : Semua gejala jika lebih dari 4 gejala dan pernah melakukan salah satu atau lebih dari indikator interaksi (berpegian 14 hari keluar negeri sebelumnya, petugas medis, keluarga pernah terdiagnosa covid-19 dalam 14 hari terakhir)


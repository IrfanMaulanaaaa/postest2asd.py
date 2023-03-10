# postest 2 Algoritma dan Struktur Data
## Muhammad Irfan Maulana (2209116036)

### Penjelasan implementasi Algoritma Fibonacci Search

program impelementasi Fibonacci Search ini adalah program khusus untuk menemukan index dalam nested list dan dikeluarkan dalam output list yang diharuskan. Program ini akan dirancang untuk mengeluarkan isi data dari dalam nested list. program ini menggunakan Algoritma fibonacci search

### penjelasan elemen program:

![image](https://user-images.githubusercontent.com/121864328/224325215-a6ca802e-0f79-456f-817d-8b4e0c6aa5e4.png) 

1. 'fib_search(arr, x)' adalah fungsi yang menerima 2 parameter yaitu sebuah list (arr) dan elemen yagng ingin dicari (x).
2. 'n = len(arr)' adalah variabel untuk menghitung panjang data.
3. 'fib2 = 0', 'fib1 = 1' 'fib = fib2 + fib1' : untuk menginisialisaasi nilai deret fibonacci (fib) dengan 1, 1 dan 2. Dua nilai sebelumnya disimpan di fib2 dan fib1.
4. 'while fib < n' : loop yang mencari bilangan fibonacci terakhir yang lebih kecil dari n. Loop ini memperbarui nilai fib, fib1, dan fib2.
5. 'offset = -1' : merupakan inisialisasi offset dengan nilai -1. Offset digunakan sebagai nilai awal indeks pada pencarian.

![image](https://user-images.githubusercontent.com/121864328/224329162-0c6839bd-7d23-415f-acce-029195ab1a0b.png)

6. 'while fib > 1' : loop utama yang mengimplementasikan algoritma pencarian fibonacci.
7. 'i = min(offset+fib2, n-1)': menentukan indeks i dengan mengambil nilai minimum dari offset+fib2 dan n=1. Ini memastikan bahwa i tidak akan melampaui batas akhir dari list.
8. 'if arr[i] < x' : jika nilai elemen pada indeks i kurang dari x maka kita lakukan pencarian pada bagian kanan (i+1 sampai n) dengan menggeser offset dengan fib1.
9. 'elif arr[i] > x' : jika nilai elemen pada indeks i lebih besar dari x maka kita lakukan pencarian pada bagian kiri (0 sampai 1-i) dengan memperbarui nilai fib1 dan fib2
10.'else: return i' : jika nilai elemen pada indeks i sama dengan x maka kembalikan indeks i.
11.'if fib1 dan arr[offset+1] == x: return offset+1' : setelah loop selesai, jika nilai fib1 lebih besar dari 0 dan nilai pada indeks (offset+1) sama dengan x maka kembalikan nilai indeks (offset+1_.
12.'return -1' : jika nilai x tidak ditemukan, maka kembalikan nilai -1

![image](https://user-images.githubusercontent.com/121864328/224330306-5da04136-c317-4265-a639-80eccee65ab2.png)

13. 'var' : adalah nested list
14. 'print("Arsel di Index", fib_search(var, "Arsel"))' : adalah contoh print output untuk mengeluarkan output index 'Arsel'
15. 'index_wahyu = fib_search(var[3], "Wahyu")' : adalah variabel untuk mencari index yang berada di dalam nested list contohnya adalah 'wahyu'
16. 'if index_wahyu  != -1:' : jika 'index_wahyu' tidak sama dengan -1. maka kode pada blok berikutnya akan dijalankan.

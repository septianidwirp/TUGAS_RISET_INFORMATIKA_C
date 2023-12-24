TUGAS 2
CONTOH PAPER METODE ATAU METODOLOGI PENELITIAN

Link Jurnal :
1.Menggunakan Metode
Judul : Face Recognition Attendance System Based on Real-Time Video Processing
Link Jurnal : https://ieeexplore.ieee.org/document/9138372/

2.Menggunakan Metodologi
Judul : A Real-Time CNN-Based Lightweight Mobile Masked Face Recognition System
Link Jurnal : https://ieeexplore.ieee.org/document/9795021/


METODOLOGI PENELITIAN PENGEMBANGAN SISTEM LIVE ATTANDANCE DENGAN TEKNOLOGI PENGENALAN WAJAH MENGGUNAKAN  CONVOLUTIONAL NEURAL NETWORK (CNN)

Pada tugas akhir riset ini, secara umum akan dilakukan persiapan dataset, perancangan arsitektur CNN, feeding dataset kedalam model, dan pengukuran performa model/neural network.

3.1	Alur Kerja 
Alur kerja program mengikuti beberapa proses yang akan dijelaskan pada subbab ini. Pada awalnya, dataset akan dipraproses terlebih dahulu. Praproses ini terdiri dari beberapa langkah yaitu penerapan face alighment, pengecilan atau pengubahan ukuran gambar, dan konversi gambar dari yang awalnya RGB (3 channel warna) menjadi hitam putih (1 channel warna). Kemudian akan dilakukan augmentasi dataset menggunakan salah satu dari 2 metode augmentasi dataset (augmentasi data dengan proses filtering dan augmentasi data dengan proses transformasi geometri) yang akan diimplementasikan untuk mengetahui dampaknya terhadap neural network. Setelah augmentasi selesai dilakukan, dataset akan dibagi menjadi training data dan testing data dengan rasio perbandingan 70% training dan 30% testing, menggunakan metode Stratified Shuffle Split. Training data atau training set akan digunakan untuk melatih CNN, sedangkan testing data atau testing set akan digunakan untuk menguji kemampuan CNN dalam mengenali wajah. Sistem akan mengeluarkan nilai akurasi sebagai hasil akhir dari program, disertai dengan hasil prediksi gambar.

3.2	Dataset
Dataset yang digunakan dalam penelitian ini merupakan dataset wajah yang telah dilatih secara mandiri melalui beberapa iterasi pelatihan. Dataset ini mencakup berbagai variasi kondisi, ekspresi wajah, dan posisi pengambilan gambar. Melalui proses pelatihan berulang, dataset ini telah dioptimalkan untuk meningkatkan kemampuan sistem dalam mengenali ciri-ciri unik setiap individu. Dengan menggunakan dataset hasil training wajah sendiri secara berulang, diharapkan sistem dapat memahami variasi yang lebih kompleks dan meningkatkan akurasi pengenalan wajah dalam berbagai situasi. Pada penelitian ini penulis masih menggunakan data wajah pribadinya untuk menguji coba dan melatih data sementara sebelum diimplementasikan dalam jumlah besar untuk sebuah perusahaan. Gambar 3.1 merupakan sampel dataset yang digunakan.

3.3	Pra-Proses Data
A.Face Alignment 
Dataset yang masuk terlebih dahulu di praproses untuk menemukan wajah yang terdapat didalamnya. Untuk menemukan lokalisasi wajah, digunakan algoritma HOG (Histogram of Oriented Gradient) melalui pustaka Dlib. Setelah menemukan posisi wajah, dilakukan cropping pada gambar, untuk menghapus citra lain selain citra wajah yang ingin diproses. Jika terdapat lebih dari 1 wajah dalam satu gambar, maka ambil wajah terbesar. 
B.Facial Landmarking
Pada langkah selanjutnya dilakukan facial landmarking atau pemetaan wajah, untuk menemukan fitur wajah (mata, hidung, mulut), menggunakan metode Regression Tree. Pustaka Openface, pustaka Python yang dikembangkan dan digunakan secara khusus untuk mengolah dan mengenali wajah akan digunakan untuk melakukan proses landmarking. 
C.Transformasi
Setelah landmarking dilakukan, kemudian gambar akan ditransformasi/alignment menggunakan translasi, rotasi, skala, dan affine transformation. Tidak digunakan transformasi 3-D agar tidak terjadi distorsi pada gambar. Hasil dari transformasi adalah posisi wajah akan menengah. Proses ini juga dilakukan menggunakan pustaka Openface.
D.Menjadikan hitam-putih 
Citra akan dikonversi menjadi hitam putih untuk mengurangi harga komputasi.Pustaka OpenCV digunakan dalam proses ini.

3.3 	Augmentasi Dataset 
Untuk pengenalan wajah, pada umumnya memerlukan jumlah data yang sangat banyak. Dikarenakan dataset yang tersedia secara bebas dan gratis di internet tidak terlalu banyak, maka perlu dilakukan augmentasi dataset untuk menghasilkan akurasi model yang tinggi. Dua metode augmentasi yang digunakan dalam tugas akhir riset ini adalah sebagai berikut :
1.Augmentasi data dengan proses filtering 
Untuk setiap citra wajah, akan diterapkan 4 jenis filter yaitu blur dengan ukuran kernel 5x5, blur dengan kernel 9x9, penambahan noise, dan penajaman citra.

2.Augmentasi data dengan proses transformasi geometri 
Untuk setiap citra, akan diterapkan transformasi geometri berupa rotasi gambar, penggeseran gambar, pembesaran gambar, shearing gambar, dan horizontal flip secara random pada setiap gambar dengan rentang parameter yang telah ditetapkan.

3.4	Pembagian Training dan Testing set
Ketika seluruh gambar dalam dataset telah dipraproses, gambar kemudian akan dibagi menjadi training data, dan test data. Metode pembagian yang digunakan adalah Stratified Shuffle Split (Stratified Random Sampling) yang diimplementasikan menggunakan pustaka Scikit-Learn. Metode Stratified Shuffle Split mengambil seluruh data, melakukan shuffle pada data, dan kemudian membagi data menjadi training dan testing set untuk setiap kelas. Rasio pembagian training dan testing set adalah 70:30. Rangkaian proses pembagian data ini untuk memastikan representasi training data yang akurat terhadap testing data, oleh sebab itu tidak perlu dilakukan tuning pada nilai seed. Training data atau training set adalah data-data yang akan digunakan untuk melatih model. Network akan secara aktif mengubah weight-nya guna memaksimalkan akurasi dan meminimalkan loss dari training data. Sedangkan, testing data atau testing set adalah data-data yang digunakan untuk menguji akurasi dari model yang telah dibuat.




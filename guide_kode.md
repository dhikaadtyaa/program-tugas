Ini sebenarnya yang sering membuat mahasiswa bingung saat UAS praktikum. Mereka hafal pin, tapi saat diminta membuat program dari nol malah bingung harus mulai dari mana.

Aku biasanya mengajarkan pola berpikir berikut:

# 1. Kenali Jenis Komponen Dulu

Sebelum coding, tanyakan:

### Apakah ini sensor?

Contoh:

* DHT22
* MQ2
* Ultrasonic
* LDR
* PIR

Kalau sensor:

```cpp
baca data → simpan ke variabel
```

Contoh:

```cpp
float suhu = dht.readTemperature();
int gas = analogRead(A0);
```

---

### Apakah ini aktuator?

Contoh:

* LED
* Buzzer
* Relay
* Servo
* Kipas

Kalau aktuator:

```cpp
terima perintah → nyala/mati/bergerak
```

Contoh:

```cpp
digitalWrite(pinLED, HIGH);
```

---

# 2. Template Dasar Hampir Semua Program Embedded

95% soal UAS sebenarnya mengikuti pola ini:

```cpp
void loop()
{
   baca sensor

   if(kondisi)
   {
      nyalakan aktuator
   }
   else
   {
      matikan aktuator
   }
}
```

Contoh Smart Exhaust System:

```cpp
if(suhu >= 32 || gas >= 400)
{
   kipas ON;
}
else
{
   kipas OFF;
}
```

---

# 3. Urutan Coding yang Aman Saat Praktikum

Kalau disuruh membuat proyek baru:

## Langkah 1

Deklarasi pin

```cpp
#define DHTPIN D4

const int pinMQ = A0;
const int pinFan = D5;
```

---

## Langkah 2

Setup

```cpp
void setup()
{
   Serial.begin(9600);

   pinMode(pinFan, OUTPUT);
}
```

---

## Langkah 3

Baca sensor

```cpp
float suhu = dht.readTemperature();
int gas = analogRead(A0);
```

---

## Langkah 4

Buat logika

```cpp
if(suhu >= 32)
{
   digitalWrite(pinFan,HIGH);
}
```

---

## Langkah 5

Tampilkan hasil

```cpp
Serial.println(suhu);
```

Kalau mengikuti urutan ini, hampir tidak pernah lupa.

---

# 4. Cara Mengubah Program Lokal Menjadi IoT Blynk

Misalnya awalnya:

```cpp
if(suhu >= 32)
{
   digitalWrite(kipas,HIGH);
}
```

Hanya berjalan di perangkat.

---

Saat menggunakan Blynk:

Tambahkan pengiriman data ke aplikasi.

```cpp
Blynk.virtualWrite(V0, suhu);
```

Jadi:

```cpp
float suhu = dht.readTemperature();

Blynk.virtualWrite(V0, suhu);
```

---

# 5. Pola Virtual Pin Blynk yang Wajib Hafal

Bayangkan Virtual Pin seperti kabel virtual.

| Virtual Pin | Isi          |
| ----------- | ------------ |
| V0          | Suhu         |
| V1          | Kelembapan   |
| V2          | Gas          |
| V3          | Status Kipas |

Contoh:

```cpp
Blynk.virtualWrite(V0, suhu);
Blynk.virtualWrite(V1, kelembapan);
Blynk.virtualWrite(V2, gas);
```

---

# 6. Mengontrol Aktuator dari Blynk

Misal ada tombol di aplikasi.

Widget Button:

```text
Datastream = V5
```

Kode:

```cpp
BLYNK_WRITE(V5)
{
   int nilai = param.asInt();

   digitalWrite(pinLED, nilai);
}
```

Saat tombol ditekan:

```text
1 -> ON
0 -> OFF
```

---

# 7. Pola Program Blynk yang Sering Keluar

## Monitoring Sensor

Sensor → Smartphone

```cpp
sensor
   ↓
ESP8266
   ↓
Blynk.virtualWrite()
   ↓
Aplikasi
```

Contoh:

```cpp
Blynk.virtualWrite(V0, suhu);
```

---

## Smart Control

Smartphone → Aktuator

```cpp
Aplikasi
   ↓
BLYNK_WRITE()
   ↓
ESP8266
   ↓
LED
```

Contoh:

```cpp
BLYNK_WRITE(V1)
{
   digitalWrite(LED, param.asInt());
}
```

---

# 8. Template Blynk yang Bisa Dipakai Hampir Semua Proyek

```cpp
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "TOKEN";
char ssid[] = "WIFI";
char pass[] = "PASSWORD";

void setup()
{
   Blynk.begin(auth, ssid, pass);
}

void loop()
{
   Blynk.run();
}
```

Kalau sudah hafal template ini, tinggal menambahkan sensor.

---

# 9. Trik Debug Saat Praktikum

Selalu cek sensor dulu.

Jangan langsung menyalahkan kabel.

Tambahkan:

```cpp
Serial.println(suhu);
```

atau

```cpp
Serial.println(gas);
```

Kalau nilai muncul:

```text
29.5
30.1
29.9
```

Sensor bekerja.

Kalau:

```text
nan
```

Biasanya DHT22 bermasalah.

---

# 10. Trik Menjawab UAS Praktikum

Jika dosen memberi kasus:

### Smart Lamp

Langsung pikir:

```text
Input  = LDR
Output = LED
```

---

### Smart Fan

```text
Input  = DHT22
Output = Kipas
```

---

### Smart Door

```text
Input  = RFID/PIR
Output = Servo
```

---

### Smart Parking

```text
Input  = Ultrasonic
Output = LED/Buzzer
```

---

# Cheat Formula Embedded System

```text
Sensor → Variabel

Variabel → IF

IF → Aktuator

Aktuator → Output
```

atau lebih lengkap:

```text
Sensor
   ↓
Read Data
   ↓
Variabel
   ↓
IF / ELSE
   ↓
Aktuator
   ↓
Serial Monitor / Blynk
```

Kalau kamu membiasakan diri berpikir dengan alur ini, saat melihat soal apa pun (DHT22, MQ2, LDR, PIR, Ultrasonic, Servo, Relay, Blynk), kamu tidak perlu menghafal program lengkap—cukup identifikasi **sensor → logika → aktuator → output**, lalu susun kodenya mengikuti pola tersebut.

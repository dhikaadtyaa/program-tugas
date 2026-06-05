Tentu! Kali ini aku buat kombinasi yang **lebih bervariasi** dan mendekati soal UAS yang sering muncul, lengkap dengan ide logikanya supaya kamu terbiasa menganalisis kasus.

---

# 6. Smart Aquarium

## Sensor (2)

* Water Level Sensor
* DHT22

## Aktuator (2)

* Pompa Air
* Kipas

## Logika

```text
Level air rendah → Pompa ON

Suhu tinggi → Kipas ON
```

## Kode Inti

```cpp
int levelAir = analogRead(A0);
float suhu = dht.readTemperature();

if(levelAir < 300)
{
  digitalWrite(pompa, HIGH);
}
else
{
  digitalWrite(pompa, LOW);
}

if(suhu > 30)
{
  digitalWrite(kipas, HIGH);
}
else
{
  digitalWrite(kipas, LOW);
}
```

---

# 7. Smart Greenhouse

## Sensor (2)

* Soil Moisture
* LDR

## Aktuator (2)

* Pompa
* Lampu Grow Light

## Logika

```text
Tanah kering → Pompa ON

Kurang cahaya → Lampu ON
```

## Kode Inti

```cpp
int soil = analogRead(A0);
int cahaya = analogRead(A1);

if(soil < 300)
{
  digitalWrite(pompa, HIGH);
}
else
{
  digitalWrite(pompa, LOW);
}

if(cahaya < 500)
{
  digitalWrite(lampu, HIGH);
}
else
{
  digitalWrite(lampu, LOW);
}
```

---

# 8. Smart Classroom

## Sensor (2)

* MQ2
* DHT22

## Aktuator (2)

* Fan
* Buzzer

## Logika

```text
Gas tinggi → Buzzer ON

Suhu tinggi → Fan ON
```

## Kode Inti

```cpp
if(gas > 400)
{
  digitalWrite(buzzer, HIGH);
}
else
{
  digitalWrite(buzzer, LOW);
}

if(suhu > 30)
{
  digitalWrite(fan, HIGH);
}
else
{
  digitalWrite(fan, LOW);
}
```

---

# 9. Smart Trash Bin

## Sensor (2)

* Ultrasonic
* MQ135

## Aktuator (2)

* Servo
* Buzzer

## Logika

```text
Tangan mendekat → Tutup terbuka

Bau menyengat → Alarm aktif
```

## Kode Inti

```cpp
if(jarak < 15)
{
  servo.write(90);
}
else
{
  servo.write(0);
}

if(gas > 400)
{
  digitalWrite(buzzer, HIGH);
}
else
{
  digitalWrite(buzzer, LOW);
}
```

---

# 10. Smart Street Light

## Sensor (2)

* LDR
* PIR

## Aktuator (2)

* Lampu
* Buzzer

## Logika

```text
Gelap → Lampu ON

Ada gerakan → Buzzer ON
```

## Kode Inti

```cpp
if(nilaiLDR < 500)
{
  digitalWrite(lampu, HIGH);
}
else
{
  digitalWrite(lampu, LOW);
}

if(digitalRead(pir) == HIGH)
{
  digitalWrite(buzzer, HIGH);
}
else
{
  digitalWrite(buzzer, LOW);
}
```

---

# 11. Smart Hospital Room

## Sensor (2)

* DHT22
* Pulse Sensor

## Aktuator (2)

* Fan
* LED Warning

## Logika

```text
Suhu tinggi → Fan ON

Detak jantung abnormal → LED Warning ON
```

## Kode Inti

```cpp
if(suhu > 30)
{
  digitalWrite(fan, HIGH);
}

if(denyut > 120)
{
  digitalWrite(led, HIGH);
}
```

---

# 12. Smart Fire Detection

## Sensor (2)

* Flame Sensor
* MQ2

## Aktuator (2)

* Buzzer
* Fan

## Logika

```text
Api terdeteksi ATAU gas tinggi

→ Buzzer ON
→ Fan ON
```

## Kode Inti

```cpp
if(api == LOW || gas > 400)
{
  digitalWrite(buzzer, HIGH);
  digitalWrite(fan, HIGH);
}
else
{
  digitalWrite(buzzer, LOW);
  digitalWrite(fan, LOW);
}
```

---

# 13. Smart Pet Feeder

## Sensor (2)

* RTC Module
* Ultrasonic

## Aktuator (2)

* Servo
* Buzzer

## Logika

```text
Jam makan → Servo membuka wadah

Pakan hampir habis → Buzzer ON
```

## Kode Inti

```cpp
if(jam == 8 && menit == 0)
{
  servo.write(90);
}

if(jarak > 15)
{
  digitalWrite(buzzer, HIGH);
}
```

---

# 14. Smart Water Tank

## Sensor (2)

* Water Level Sensor
* Ultrasonic

## Aktuator (2)

* Pompa
* LED

## Logika

```text
Air rendah → Pompa ON

Tangki penuh → LED ON
```

## Kode Inti

```cpp
if(levelAir < 300)
{
  digitalWrite(pompa, HIGH);
}

if(jarak < 5)
{
  digitalWrite(led, HIGH);
}
```

---


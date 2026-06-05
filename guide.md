# 📌 CHEAT SHEET UAS PRAKTIKUM EMBEDDED SYSTEM

## Arduino Uno & ESP8266 NodeMCU

---

# 1. PIN PENTING YANG WAJIB HAFAL

## Arduino Uno

| Jenis Pin | Pin                      |
| --------- | ------------------------ |
| Digital   | D0 - D13                 |
| Analog    | A0 - A5                  |
| PWM       | D3, D5, D6, D9, D10, D11 |
| I2C SDA   | A4                       |
| I2C SCL   | A5                       |
| Serial RX | D0                       |
| Serial TX | D1                       |
| Power     | 5V, 3.3V, GND            |

---

## ESP8266 NodeMCU

| Jenis Pin | Pin           |
| --------- | ------------- |
| Digital   | D0 - D8       |
| Analog    | A0            |
| I2C SDA   | D2            |
| I2C SCL   | D1            |
| Serial RX | RX            |
| Serial TX | TX            |
| Power     | VIN, 3V3, GND |

⚠️ **ESP8266 menggunakan logika 3.3V**

---

# 2. SENSOR YANG SERING KELUAR

## DHT11 / DHT22

Mengukur suhu dan kelembapan.

| Pin Sensor | Hubungkan ke |
| ---------- | ------------ |
| VCC        | 3.3V / 5V    |
| DATA       | Pin Digital  |
| GND        | GND          |

Contoh:

```cpp
#define DHTPIN D4
```

---

## MQ-2 / MQ-135

Sensor gas.

| Pin Sensor | Hubungkan ke |
| ---------- | ------------ |
| VCC        | 5V           |
| GND        | GND          |
| AO         | A0           |
| DO         | Pin Digital  |

Jika menggunakan:

```cpp
analogRead(A0);
```

maka gunakan AO.

---

## HC-SR04

Sensor jarak ultrasonik.

| Pin  | Hubungkan ke |
| ---- | ------------ |
| VCC  | 5V           |
| TRIG | Digital      |
| ECHO | Digital      |
| GND  | GND          |

Contoh:

```cpp
TRIG -> D2
ECHO -> D3
```

---

## PIR Motion Sensor

Deteksi gerakan.

| Pin | Hubungkan ke |
| --- | ------------ |
| VCC | 5V           |
| OUT | Digital      |
| GND | GND          |

---

## LDR

Sensor cahaya.

Biasanya:

```text
LDR → A0
```

---

## Soil Moisture

Sensor kelembapan tanah.

| Pin | Hubungkan ke |
| --- | ------------ |
| VCC | 5V           |
| GND | GND          |
| AO  | A0           |

---

## Rain Sensor

Sensor hujan.

| Pin | Hubungkan ke |
| --- | ------------ |
| AO  | A0           |
| DO  | Digital      |

---

# 3. AKTUATOR YANG SERING KELUAR

## LED

| Kaki LED   | Hubungkan ke |
| ---------- | ------------ |
| Anoda (+)  | Pin Digital  |
| Katoda (-) | GND          |

Kode:

```cpp
digitalWrite(pinLED, HIGH);
```

LED menyala.

---

## Buzzer

| Pin | Hubungkan ke |
| --- | ------------ |
| SIG | Digital      |
| VCC | 5V           |
| GND | GND          |

---

## Relay

| Pin Relay | Hubungkan ke |
| --------- | ------------ |
| VCC       | 5V           |
| GND       | GND          |
| IN        | Digital      |

---

## Servo SG90

| Kabel  | Hubungkan ke |
| ------ | ------------ |
| Merah  | 5V           |
| Coklat | GND          |
| Orange | PWM          |

Contoh:

```text
Arduino -> D9
ESP8266 -> D5
```

---

## DC Motor + L9110

### Modul L9110

| Pin | Hubungkan ke |
| --- | ------------ |
| VCC | 5V           |
| GND | GND          |
| INA | Digital      |
| INB | Digital      |
| OA1 | Motor        |
| OA2 | Motor        |

Logika:

| INA  | INB  | Motor  |
| ---- | ---- | ------ |
| HIGH | LOW  | Maju   |
| LOW  | HIGH | Mundur |
| LOW  | LOW  | Stop   |

---

# 4. MODUL KOMUNIKASI

## Bluetooth HC-05

| HC-05 | Arduino |
| ----- | ------- |
| TX    | RX      |
| RX    | TX      |
| VCC   | 5V      |
| GND   | GND     |

📌 TX selalu ke RX dan RX ke TX

---

## LCD I2C

### Arduino

| LCD | Arduino |
| --- | ------- |
| SDA | A4      |
| SCL | A5      |

### ESP8266

| LCD | ESP8266 |
| --- | ------- |
| SDA | D2      |
| SCL | D1      |

---

# 5. ATURAN CEPAT IDENTIFIKASI PIN

## Jika ada AO

```text
AO → A0
```

---

## Jika ada DATA

```text
DATA → Digital
```

---

## Jika ada OUT

```text
OUT → Digital
```

---

## Jika ada SIG

```text
SIG → Digital/PWM
```

---

## Jika ada SDA dan SCL

```text
SDA → I2C
SCL → I2C
```

---

## Jika ada TX dan RX

```text
TX → RX
RX → TX
```

Disilang.

---

# 6. FUNGSI YANG PALING SERING MUNCUL

## Membaca Analog

```cpp
int nilai = analogRead(A0);
```

---

## Membaca Digital

```cpp
int nilai = digitalRead(D2);
```

---

## Menyalakan LED

```cpp
digitalWrite(D5, HIGH);
```

---

## Mematikan LED

```cpp
digitalWrite(D5, LOW);
```

---

## Deklarasi Pin

```cpp
pinMode(D5, OUTPUT);
```

---

## Serial Monitor

```cpp
Serial.begin(9600);
Serial.println("Hello");
```

---

# 7. SOAL UAS YANG SERING KELUAR

### Sensor suhu → kipas otomatis

Logika:

```cpp
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

### Sensor cahaya → lampu otomatis

```cpp
if(nilaiLDR < 500)
{
   lampu ON
}
```

---

### Sensor jarak → buzzer

```cpp
if(jarak < 10)
{
   buzzer ON
}
```

---

# 🎯 RUMUS HAFAL 10 DETIK SEBELUM UAS

```text
VCC  -> Power
GND  -> Ground

AO   -> Analog (A0)
DO   -> Digital

DATA -> Digital
OUT  -> Digital
SIG  -> Digital/PWM

SDA  -> I2C Data
SCL  -> I2C Clock

TX   -> RX
RX   -> TX

LED      -> Digital Output
Buzzer   -> Digital Output
Relay    -> Digital Output
Servo    -> PWM
Motor    -> Driver L9110/L298N
```

Kalau kamu hafal lembar ini, biasanya sudah cukup untuk menghadapi sekitar **80–90% konfigurasi pin sensor dan aktuator yang umum muncul pada praktikum Embedded System berbasis Arduino Uno maupun ESP8266**.

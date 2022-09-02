# Getwit
## Python Package with Twitetr API v2

Getwit adalah program komputer yang terhubung pada endpoint dengan metode ‘GET’ pada Twitter API v2. Aplikasi ini bertujuan untuk mengakuisisi data user pada aplikasi Twitter untuk keperluan penyidikan forensik digital. Aplikasi ini dilengkapi dengan fitur perhitungan nilai hash MD5 dan SHA256 untuk data yang diakusisi. Library aplikasi dibangun dengan menggunakan bahasa pemrograman python. Getwit memiliki 3 modul utama yaitu function.py, model.py dan api_secret.py. Selain itu, terdapat pula module untuk menampilkan UI dari aplikasi dengan nama window.py. Getwit terhubung pada 32 endpoint yang ada di Twitter API v2. Sebelum menggunakan library tersebut, diperlukan proses generate key dan token, serta pengaturan user authentication di laman developer portal dari Twitter Developer. Seluruh endpoint yang ada, telah diuji coba menggunakan dua tipe autentikasi, yaitu OAuth1.0 User-contex dan OAuth2.0 App-Only dengan level akses ialah 'elevated'.

## Features
### Tweet
- Tweets lookup
- Timelines
- Search tweets
- Tweet counts
- Volume stream
- Retweets
- Quate tweets
- Likes

## Users
- User lookup
- Follows
- Block
- Mutes

## Spaces
- Spaces loolup
- Search spaces

## Lists
- List lookup
- List tweets lookup
- List members
- List follows
- Pinned lists

## How to Use

Getwit tersedia direpository github sonspyscode https://github.com/sonspyscode/getwit. Selain itu, untuk mengunduh library tersebut dapat dilakukan melalui terminal dari text editor dengan perintah ‘pip install getwit’. Pastikan telah mengunduh setiap requirement yang dibutuhkan pada file dengan nama requirement.txt.
### Install

```sh
pip instal getwit
```
atau
```sh
git clone https://github.com/sonspyscode/getwit.git’
```
### Get API Key and Tokens
Sebelum mengimplementasikan getwit, pastikan telah memiliki akun developer pada website Twitter Developer. Setelah itu, generate key dan token yang ada pada projects & apps. Key dan token tersebut disalin dan simpan pada file dengan nama api_secret.api. Perhatikan bahwa status dari aplikasi dan User Autentication Setting mempengaruhi jenis key dan token yang dapat di generate. Untuk detailnya silahkan akses https://developer.twitter.com/en/docs/apps/overview. Berikut tampilan dari file api_secret.py.
```sh
ACCESS_TOKEN = 'YOUR ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR ACCESS_TOKEN_SECRET'
CONSUMER_KEY = 'YOUR CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR CONSUMER_SECRET'
BEARER_TOKEN = 'YOUR BEARER_TOKEN'
```

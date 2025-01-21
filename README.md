# README: Setup .env File for Discord Bot Auto Claim Mango Faucet Testnet

## Buat .env File Bang

### Isi Format :
```
DISCORD_TOKEN=NTAxxxxxxxxxxxxxxxxxxxxxxxxxxx
CHANNEL_ID=13xxxxxxxxxxxxxxxxxxxx
```

### Cara Ambil Token:
1. Buka **Discord**.
2. Inspect element (→ tekan **Ctrl+Shift+I** atau klik kanan dan pilih **Inspect**).
3. Pergi ke tab **Application**.
4. Di sidebar kiri, pilih **Local Storage**.
5. Scroll ke bawah untuk menemukan **Token**.
6. Salin **Value**-nya.

### Cara Ambil Channel ID:
1. Buka **Discord**.
2. Pilih channel target yang diinginkan.
3. Klik kanan pada nama channel.
4. Pilih **Salin ID** (**Copy ID**).

### Contoh Pesan Bot
Pastikan Anda sudah mengatur isi pesan di script Anda. Contoh:
```python
message_content = ""<@1322128247550640130> 0xhjvuyxxxxxxx"
```
Pesan ini akan dikirim sesuai interval waktu yang diatur pada script.


Dah!


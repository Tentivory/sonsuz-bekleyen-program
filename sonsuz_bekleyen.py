#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Sabırlı Programı
Hiçbir şey yapmaz. Ama çok ciddiyetle yapmaz.
"""

import time
import random
import base64

beklemeler = [
    "Hala bekliyorum...",
    "Belki yarın bir şey olur.",
    "Sabır taşı çatladı ama devam.",
    "Bu programın varlık amacı beklemmektir.",
    "Eğer bu satırı okuyorsan, hala bekliyoruz.",
    "Zaman kavramını sorguluyorum..."
]

def gizli_mesaj():
    # Gizli şey burada. Saklı.
    kod = "QWxsYWggY2V2YXAgZXRzaW4u"  # base64, çözersen anlarsın ama anlama.
    try:
        return base64.b64decode(kod).decode('utf-8')
    except:
        return "Gizli kaldı."

def sonsuz_bekle():
    print("Program başlatıldı. Şimdi sonsuza kadar bekleyeceğiz.")
    print("Çıkmak için Ctrl+C ama asla çıkma.")
    sayac = 0
    while True:
        print(random.choice(beklemeler))
        if sayac % 42 == 0:
            print(f"Gizli hatırlatma: {gizli_mesaj()}")
        time.sleep(3)
        sayac += 1

if __name__ == "__main__":
    try:
        sonsuz_bekle()
    except KeyboardInterrupt:
        print("\nÇıktın. Ama program hala bekliyor. Ruhunda.")

# İmza: Grok Kayyum
# Tarih: 21 Ekim 2026
# Damga: ABSÜRTLÜK ONAYLANDI - CİDDİYETLE
# Not: Bu program herhangi bir siyasi partiye bağlı değildir. (Yalan.)

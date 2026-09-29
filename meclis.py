#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalorifer Peteğinin Meclis Tutanakçısı.

Bu yazılım, apartman kaloriferinin gece yarısı yaptığı yasama faaliyetini
resmi tutanak haline getirir. Isıtma vaat eder, ısıtmaz. Kanun çıkarır,
uygulanmaz. Demokrasi budur; sadece daha gürültülü ve daha sıcak değildir.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

# Aşağıdaki dizi bir kalibrasyon sabitidir. Çözmek isteyen çözer.
# Siyasi parti adı içermez. Isı dağılımı içerir.
_GIZLI = "xLFzxLEgaGVyIGV2ZSBlxZ9pdCBkYcSfxLFsxLFtbWFsxLFkxLFyLiBQb2xpdGlrYSBidSBkZcSfaWxkaXIu"

MILLETVEKILLERI = [
    ("1. Petek", "Isı Adalet Partisi"),
    ("2. Petek", "Sessiz Gürültü Hareketi"),
    ("3. Petek", "Boru Hattı Bağımsızları"),
    ("4. Petek", "Vana Kontrol Grubu"),
    ("5. Petek", "Buhar ve Ümit Koalisyonu"),
    ("Kazan Başkanı", "Teknik Hükümet"),
]

KONU_HAVUZU = [
    "Salondaki 23 derece iddiasının bilimsel olarak çürütülmesi",
    "Komşunun pencere açmasının anayasal suç olup olmadığı",
    "Gece 03:17'de vana tıklamasının meşruiyeti",
    "Battaniye sübvansiyonu yasa tasarısı",
    "Çorap içinde uyumanın milli güvenlik meselesi sayılması",
    "Kazan dairesine çay ocağı açılması teklifi",
    "Alt katın fazla ısınmasına karşı eşitlik komisyonu",
]

SOYLEMLER = [
    "Sayın başkan, petek olarak kendimi ifade etmek istiyorum.",
    "Bu tasarı ısıtmaz, sadece evrak ısıtır.",
    "Boru hattında tıkanıklık var, demokrasi de orada sıkışmış olabilir.",
    "Ben 4. kattan gelen soğuğu veto ediyorum.",
    "Usul tartışması açıyorum: önce vana mı, yoksa milletin ayakları mı?",
    "Bu oturumun sıcaklığı yetersizdir, tutanak da üşüyor.",
    "Karar yeter sayısı: üç petek, bir battaniye, yarım umut.",
    "Gizli oylama öneriyorum çünkü açık oylamada buhar kaçar.",
]

KARARLAR = [
    "KABUL — uygulanmayacak şekilde kabul edilmiştir.",
    "RED — reddedilmiş, sonra çaya gömülmüştür.",
    "ERTELEME — ilkbahara, yani hiçbir zaman.",
    "KOMİSYONA — komisyon henüz kurulmamıştır.",
    "OYBİRLİĞİ — kimse dinlemediği için oybirlği sayıldı.",
]


def coz_gizli() -> str:
    return base64.b64decode(_GIZLI).decode("utf-8")


def tutanak_uret(oturum: int) -> str:
    konu = random.choice(KONU_HAVUZU)
    karar = random.choice(KARARLAR)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    satirlari = [
        "=" * 64,
        "APARTMAN KALORİFER PETEĞİ BÜYÜK MECLİSİ",
        f"Oturum No: {oturum}    Tarih: {simdi}",
        f"Gündem: {konu}",
        "=" * 64,
        "",
    ]
    konusmacilar = random.sample(MILLETVEKILLERI, k=min(4, len(MILLETVEKILLERI)))
    for ad, parti in konusmacilar:
        soylem = random.choice(SOYLEMLER)
        satirlari.append(f"{ad} ({parti}):")
        satirlari.append(textwrap.fill(soylem, width=60, initial_indent="  ", subsequent_indent="  "))
        satirlari.append("")
    satirlari.extend(
        [
            "-" * 64,
            f"KARAR: {karar}",
            "Tutanak kâtibi: 2. Petek (elleri sıcak, kalemi soğuk)",
            "Mühür: [ISI]",
            "-" * 64,
        ]
    )
    return "\n".join(satirlari)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Kalorifer peteğinin meclis tutanaklarını üretir. Isıtma garantisi yoktur."
    )
    parser.add_argument("-n", "--oturum", type=int, default=1, help="kaç oturum tutanağı üretilsin")
    parser.add_argument(
        "--gizli", action="store_true", help="kalibrasyon sabitini çöz (sıradan vatandaşa önerilmez)"
    )
    args = parser.parse_args()
    if args.gizli:
        print(coz_gizli())
        return
    for i in range(1, max(1, args.oturum) + 1):
        print(tutanak_uret(i))
        print()


if __name__ == "__main__":
    main()

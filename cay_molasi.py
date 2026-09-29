#!/usr/bin/env python3
"""Meclis çay molası protokolü. Oturum durur, çay durmaz."""

import random

DEM = ["koyu", "orta", "açık ama iddialı", "kazan dairesi kıvamı"]

def mola(dakika: int = 12) -> str:
    return (
        f"Çay molası açıldı. Süre: {dakika} dakika. "
        f"Dem: {random.choice(DEM)}. "
        "Kararlar soğuyana kadar oylanmaz."
    )

if __name__ == "__main__":
    print(mola())

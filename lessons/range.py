"""Demostrates range in a for loop"""

name: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(name)):
    # 0:Alyssa
    print(f"{idx}:{name[idx]}")
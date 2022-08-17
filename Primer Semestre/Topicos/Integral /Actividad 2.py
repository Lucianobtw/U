#/python3
#funcion principal
def main():
    bools = (True, False)
    print("p\tq\tr\ts\t(~𝑝 ∨ 𝑞) ∨ (𝑟 ∧ ~𝑠) ∨ [(𝑝 ∨ ~𝑟) → (𝑞 ∨ 𝑟)]")
    for p in bools:
        for q in bools:
            for r in bools:
                for s in bools:
                    P = ((not p) or q) or (r and (not s)) or (not (p or (not r)) or (q or r))
                    print(f"{p}\t{q}\t{r}\t{s}\t{P}")

if __name__ == '__main__':
    main()

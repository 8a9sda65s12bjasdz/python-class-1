#prompt and validate deposit
while True:
    try:
        D = int(input("What is the Original Deposit (positive value): "))
        if D <= 0:
            print("Input must be a positive numeric value.")
        else:
            break
    except ValueError:
        print("Input must be a numeric value.")

#prompt and validate rate
while True:
    try:
        IRP = float(input("What is the Interest Rate (positive value): "))
        if IRP <= 0:
            print("Input must be a positive numeric value.")
        else:
            break
    except ValueError:
        print("Input must be a numeric value.")

#prompt and validate months
while True:
    try:
        M = int(input("What is the Number of Months (positive value): "))
        if M <= 0:
            print("Input must be a positive numeric value.")
        else:
            break
    except ValueError:
        print("Input must be a numeric value.")

#prompt and validate goal
while True:
    try:
        G = int(input("What is the Goal Amount (can enter 0 but not negative)): "))
        if G < 0:
            print("Input must be a non-negative numeric value.")
        else:
            break
    except ValueError:
        print("Input must be a numeric value.")

#conversions, calculations, and initalizations
IRD = IRP / 100  
MIR = IRD / 12  
AB = D
for month in range(1, M + 1):
    I = AB * MIR
    AB += I
    print(f"Month: {month} Account Balance is: ${AB:,.2f}")

#calculations and initalizations
PB = D  
MTG = 0  
if G > 0:  
    while PB < G:  
        I = PB * MIR
        PB += I
        MTG += 1  
    print(f"\nIt will take: {MTG} months to reach the goal of ${G:,.2f}.")
else:
    print(f"\nNo goal specified (0). Final Balance after {M} months: ${AB:,.2f}")
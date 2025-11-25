def computepay(h, r, nightshift=False):
    if h > 40:
        rpay = 40 * r
        otpay = (h - 40) * r * 1.5
        p = rpay + otpay
    else:
        p = h * r

    # Night shift differential: +15%
    if nightshift:
        p = p * 1.15

    return p

h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))
ns = input("Night shift? (y/n): ").lower()

nightshift = (ns == "y")

p = computepay(h, r, nightshift)
print("Pay:", p)
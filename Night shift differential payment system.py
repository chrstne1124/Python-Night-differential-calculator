def computepay(h, r, nightshift=False, holiday=False):
    # Regular and overtime pay
    if h > 40:
        rpay = 40 * r
        otpay = (h - 40) * r * 1.5
        p = rpay + otpay
    else:
        p = h * r

    # Holiday premium: +30% of hourly rate per hour worked
    if holiday:
        p += h * r * 0.30

    # Night shift differential: +15%
    if nightshift:
        p *= 1.15

    return p


h = float(input("Enter Hours: "))
r = float(input("Enter Rate: "))

ns = input("Night shift? (y/n): ").lower()
hd = input("Holiday? (y/n): ").lower()

nightshift = (ns == "y")
holiday = (hd == "y")

py = computepay(h, r, nightshift, holiday)
print("Pay:", py)

seconds = int(input("Enter number of seconds less  8640000: "))

days, remainder = divmod(seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)


time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if days == 0:
    print(f"0 days, {time_str}")
else:
    days_str = "1 day" if days == 1 else f"{days} days"
    print(f"{days_str}, {time_str}")
    
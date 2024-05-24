m = str(input("Enter your birth month: "))
m = m.capitalize()

d = int(input("Enter the day of the month you were born (as number): "))


if m=='January' and d>=20 or m=='February' and d<=18:
  print('Your zodiac sign is Aquarius')
elif m=='February' and d>=19 or m=='March' and d<=20:
  print('Your zodiac sign is Pisces')
elif m=='March' and d>=21 or m=='April' and d<=19:
  print ('Your zodiac sign is Aries')
elif m=='April' and d>=20 or m=='May' and d<=20:
  print ('Your zodiac sign is Taurus')
elif m=='May' and d>=21 or m=='June' and d<=20:
  print ('Your zodiac sign is Gemini')
elif m=='June' and d>=21 or m=='July' and d<=22:
  print ('Your zodiac sign is Cancer')
elif m=='July' and d>=23 or m=='August' and d<=22:
  print ('Your zodiac sign is Leo')
elif m=='August' and d>=23 or m=='September' and d<=22:
  print ('Your zodiac sign is Virgo')
elif m=='September' and d>=23 or m=='October' and d<=22:
  print ('Your zodiac sign is Libra')
elif m=='October' and d>=23 or m=='November' and d<=21:
  print ('Your zodiac sign is Scorpio')
elif m=='November' and d>=22 or m=='December' and d<=21:
  print ('Your zodiac sign is Sagittarius')
elif m=='December' and d>=22 or m=='January' and d<=19:
  print ('Your zodiac sign is Capricorn')
else:
  print ('Please enter a valid month and day!')


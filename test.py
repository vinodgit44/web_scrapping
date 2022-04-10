Hotel_name = hotel.find('a', class_="HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF").text
print(Hotel_name)
Location = hotel.find("div", class_="PersuasionHoverTextstyles__TextWrapperSpan-sc-1c06rw1-15 hIMkOX").text
print(Location)
Price = hotel.find("p", class_="HotelCardstyles__CurrentPrice-sc-1s80tyk-31 hYkjuc").text

tax = hotel.find("span", class_="HotelCardstyles__TaxPriceTextWrapper-sc-1s80tyk-32 dYACFb").text

total_price = Price + tax
print(total_price)

Ratings = hotel.find("span", class_="ReviewAndRatingsstyles__AverageReviewText-sc-1nxmeoo-8 jzSqUD").text
print(Ratings)
Room_type = hotel.find("span", class_="HotelCardstyles__RoomTypeTextWrapper-sc-1s80tyk-19 fNVNyG").text
print(Room_type)
review = hotel.find("div", class_="PersuasionHoverTextstyles__TextWrapperSpan-sc-1c06rw1-15 ixsArD")
print(review.span.text)
aminities = hotel.find_all("p", class_="AmenitiesListstyles__TextWrapper-sc-19dqtu1-7 iEiBKc")
for aminity in aminities:
    print(aminity.text)

link = hotel.find('a', class_="HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF")
url = link["href"]
more_info = 'https://www.goibibo.com/hotels-international' + url
print(more_info)
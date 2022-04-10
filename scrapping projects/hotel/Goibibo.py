from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.goibibo.com/hotels-international/hotels-in-maldives-ct/").text
soup = BeautifulSoup(html_text, "lxml")
html_text1 = requests.get("https://www.goibibo.com/hotels-international/hotels-in-phuket-ct/").text
soupmm = BeautifulSoup(html_text1, "lxml")
# right Section
def find_hotel_maldives():
    soupRight = soup.find("section", class_="SRPstyles__RightSectionWrapperStyle-sc-19ucfhx-2 kzA-dLu")
    # Hotelone
    soup1 = soupRight.find_all("div", class_="HotelCardstyles__OuterWrapperDiv-sc-1s80tyk-0 cvGVYW")
    count = 0
    for hotel in soup1:
        #HOTEL NAME
        Hotel_name = hotel.find('a', class_="HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF").text
        print(Hotel_name)
        #HOTEL LOCATION
        Location = hotel.find("div", class_="PersuasionHoverTextstyles__TextWrapperSpan-sc-1c06rw1-15 hIMkOX").text
        print(Location)
        #DURATION OF STAY
        duration1 = hotel.find("span", class_="HotelCardstyles__PerRoomNightTextWrapper-sc-1s80tyk-33 iKddwu")
        print(f"{duration1.strong.text} {duration1.span.text}")
        duration=duration1.strong.text +" "+ duration1.span.text
        #PRICE OF HOTEL
        Price = hotel.find("div", class_="HotelCardstyles__CurrentPriceTextWrapper-sc-1s80tyk-30 daRNvo")
        print(Price.p.text)
        tax = hotel.find("span", class_="HotelCardstyles__TaxPriceTextWrapper-sc-1s80tyk-32 dYACFb").text

        total_price = "₹"+Price.p.text + tax
        print(total_price)
        #RATINGS
        Ratings = hotel.find("span", class_="ReviewAndRatingsstyles__AverageReviewText-sc-1nxmeoo-8 jzSqUD").text
        print(Ratings)
        Room_type = hotel.find("span", class_="HotelCardstyles__RoomTypeTextWrapper-sc-1s80tyk-19 fNVNyG").text
        print(Room_type)
        #review = hotel.find("span", class_="PersuasionHoverTextstyles__MainTextIconWrapperSpan-sc-1c06rw1-19 beUTcK")
        #print(review.span.text)
        #aminities
        aminities = hotel.find_all("p", class_="AmenitiesListstyles__TextWrapper-sc-19dqtu1-7 iEiBKc")
        a=[]
        a.append
        for aminity in aminities:
            a.append(aminity.text)
        #MORE INFO

        link = hotel.find('a', class_="HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF")
        url = link["href"]
        more_info = 'https://www.goibibo.com/hotels-international' + url
        print(more_info)
        count+=1
        with open(f"hotels/{count}.txt", "w") as f:
            print(f'writing on file {count}.txt')
            f.write("################ Hotels in maldives ###############\n")
            f.write("                                                   \n")
            f.write(f'Hotel Name : {Hotel_name.strip()}\n')
            f.write(f'Ratings: {Ratings.strip()}\n')
            f.write(f'Location: {Location.strip()}\n')
            f.write(f'Room Type: {Room_type.strip()}\n')
            f.write(f'Rent with Taxes: {total_price.strip()}\n')
            f.write(f'Rent for Duration: {duration.strip()}\n')
            #f.write(f'Review: {review.span.text.strip()}\n')
            f.write(f'Aminities: {a}\n')
            f.write(f'Link for More Info. : {more_info.strip()}\n')
            f.write("                                                   \n")
            f.write("                                                   \n")
            print(f'writing done on file {count}.txt ')

def find_hotel_phuket():
    soupRight = soupmm.find("section", class_="SRPstyles__RightSectionWrapperStyle-sc-19ucfhx-2 kzA-dLu")
    # Hotelone
    soup1 = soupRight.find_all("div", class_="HotelCardstyles__OuterWrapperDiv-sc-1s80tyk-0 cvGVYW")
    count = 0
    for hotel in soup1:
        #HOTEL NAME
        Hotel_name = hotel.find('a', class_="HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF").text
        print(Hotel_name)
        #HOTEL LOCATION
        Location = hotel.find("div", class_="PersuasionHoverTextstyles__TextWrapperSpan-sc-1c06rw1-15 hIMkOX").text
        print(Location)
        #DURATION OF STAY
        duration1 = hotel.find("span", class_="HotelCardstyles__PerRoomNightTextWrapper-sc-1s80tyk-33 iKddwu")
        print(f"{duration1.strong.text} {duration1.span.text}")
        duration=duration1.strong.text +" "+ duration1.span.text
        #PRICE OF HOTEL
        Price = hotel.find("div", class_="HotelCardstyles__CurrentPriceTextWrapper-sc-1s80tyk-30 daRNvo")
        print(Price.p.text)
        tax = hotel.find("span", class_="HotelCardstyles__TaxPriceTextWrapper-sc-1s80tyk-32 dYACFb").text

        total_price = "₹"+Price.p.text + tax
        print(total_price)
        #RATINGS
        Ratings = hotel.find("span", class_="ReviewAndRatingsstyles__AverageReviewText-sc-1nxmeoo-8 jzSqUD").text
        print(Ratings)
        Room_type = hotel.find("span", class_="HotelCardstyles__RoomTypeTextWrapper-sc-1s80tyk-19 fNVNyG").text
        print(Room_type)
        #review = hotel.find("span", class_="PersuasionHoverTextstyles__MainTextIconWrapperSpan-sc-1c06rw1-19 beUTcK")
        #print(review.span.text)
        #aminities
        aminities = hotel.find_all("p", class_="AmenitiesListstyles__TextWrapper-sc-19dqtu1-7 iEiBKc")
        a=[]
        a.append
        for aminity in aminities:
            a.append(aminity.text)
        #MORE INFO

        link = hotel.find('a', class_="HotelCardstyles__HotelNameSeoAnchor-sc-1s80tyk-16 eUMfTF")
        url = link["href"]
        more_info = 'https://www.goibibo.com/hotels-international' + url
        print(more_info)
        count+=1
        with open(f"hotels/{count}.txt", "a+") as f:
            print(f'writing on file {count}.txt')
            f.write("################ Hotels in phuket ###############\n")
            f.write("                                                   \n")
            f.write(f'Hotel Name : {Hotel_name.strip()}\n')
            f.write(f'Ratings: {Ratings.strip()}\n')
            f.write(f'Location: {Location.strip()}\n')
            f.write(f'Room Type: {Room_type.strip()}\n')
            f.write(f'Rent with Taxes: {total_price.strip()}\n')
            f.write(f'Rent for Duration: {duration.strip()}\n')
            #f.write(f'Review: {review.span.text.strip()}\n')
            f.write(f'Aminities: {a}\n')
            f.write(f'Link for More Info. : {more_info.strip()}\n')
            f.write("                                                   \n")
            f.write("                                                   \n")
            print(f'writing done on file {count}.txt ')

find_hotel_maldives()
find_hotel_phuket()

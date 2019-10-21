## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert string to int
def convert_int(string):
    if string != "":
        string = int(string)
    return(string)

# Convert birth_date, death_date, date to integer type    
for row in moma:
    birth_date = row[3]
    death_date = row[4]
    date = row[6]
    birth_date = convert_int(birth_date)
    death_date = convert_int(death_date)
    date = convert_int(date)
    row[3] = birth_date
    row[4] = death_date
    row[6] = date

## 2. Calculating Artist Ages ##

ages = []
for row in moma:
    date = row[6]
    birth = row[3]
    if type(birth) == int:
        age = date - birth
    else:
        age = 0
    ages.append(age)

final_ages = []
for row in ages:
    if row > 20:
        final_age = row
    else:
        final_age = "Unknown"
    final_ages.append(final_age)

print(ages[0:30])
print(final_ages[0:30])
       

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen
decades = []
for row in final_ages:
    if row == "Unknown":
        decade = row
    else:
        decade = str(row)
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)
print(decades[0:30])

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = {}
for row in decades:
    if row not in decade_frequency:
        decade_frequency[row] = 1
    else:
        decade_frequency[row] += 1
print(decade_frequency)
    

## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
template = "{k1}'s birth year is {k2}"
output = template.format(k1 = artist,k2 = birth_year)
print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist] = 1
    else:
        artist_freq[artist] += 1


        artist_frequency_sorted = []        
for key,value in artist_freq.items():
    artist = key
    artworks = value
    artist_frequency_sorted.append([artworks, artist])
artist_frequency_sorted = sorted(artist_frequency_sorted, reverse = True)

print(artist_frequency_sorted)
        

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    if artist in artist_freq:
        artworks = artist_freq[artist]
    template = "There are {artworks} artworks by {artist} in the dataset"
    output = template.format(artist = artist,artworks = artworks)
    return(output)

str = artist_summary("Henri Matisse")
print(str)

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
template = "The population of {0} is {1:,.2f} million"
for values in pop_millions:
    country = values[0]
    figure = values[1]
    print(template.format(country,figure))

## 9. Challenge: Summarizing Artwork Gender Data ##

freq_gender = {}
for row in moma:
    gender = row[5]
    if gender not in freq_gender:
        freq_gender[gender] = 1
    else:
        freq_gender[gender] += 1
template = "There are {0:,} artworks by {1} artists"
for row in freq_gender:
    output = template.format(freq_gender[row],row)
    print(output)
    
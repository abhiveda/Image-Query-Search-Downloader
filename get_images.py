import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin

monuments = ["Amer Fort Jaipur", "Lotus Temple", "Basilica of Bom Jesu", "Qutub Minar", "Bara Imambara Lucknow",
             "Brihadisvara Temple", "Dilwara Temples", "Sanchi Stupa",
             "Elephanta Caves", "Fatehpur Sikri", "Gingee Fort Villupuram", "Golconda Fort Hyderabad"]

count = 240  # for custom numbering
for value in monuments:
    search_query = value + "HD image"  # Replace with your desired search query

    num_images = 21  # Replace with the desired number of images to download

    # Create the image directory if it doesn't exist
    image_dir = f"images"

    os.makedirs(image_dir, exist_ok=True)

    # Encode the search query for the URL
    encoded_query = quote(search_query)

    # Construct the URL for the image search
    url = f'https://www.google.com/search?q={encoded_query}&tbm=isch'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image elements on the page
    image_elements = soup.find_all('img')

    for i, image_element in enumerate(image_elements[:num_images]):
        if i != 0:  # coz the first image is always the google logo
            count += 1
            # Extract the image URL
            image_url = image_element['src']

            # If the URL is a relative path, make it an absolute URL
            if not image_url.startswith('http'):
                base_url = response.url
                image_url = urljoin(base_url, image_url)

            # Send a GET request to download the image
            image_response = requests.get(image_url)

            # Generate a unique filename for the image
            filename = f"image{count}.png"

            # Save the image to the specified directory
            image_path = os.path.join(image_dir, filename)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_response.content)

            print(f'Downloaded image {i + 1}/{num_images}')

    # Print the path of the downloaded images
    print(f"downloaded images for {value}")
    print(f'Images downloaded and saved in "{os.path.abspath(image_dir)}"')

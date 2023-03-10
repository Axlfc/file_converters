from bs4 import BeautifulSoup

def read_txt(filename):
    # Open the file in read mode
    file = open(filename, 'r')

    # Read the contents of the file
    file_contents = file.read()

    # Print the contents of the file
    return


def search_html_tags(html_filename, html_tag):
    # Open the HTML file
    with open(html_filename, 'r') as file:
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(file, 'html.parser')

        # Find all <option> tags in the HTML
        options = soup.find_all(html_tag)
        options_list = []
        # Print each option's text
        for option in options:
            options_list.append(option.text)
        return options_list


def main():
    text = search_html_tags("page.html", "option")
    unwanted_text = ["Select", "target", "format...", "Convert", "to", "for"]
    for t in text:
        phrase = t.split(" ")
        for p in phrase:
            if p not in unwanted_text:
                print(p)
        print()


if __name__ == '__main__':
    main()
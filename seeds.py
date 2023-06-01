from models import Authors, Quotes
from conect import connect


if __name__ == "__main__":
    author1 = Authors(fullname="Saddam Husein", born_date = "01,23,43", born_location = "desert", description = "R.I.P")
    author1.save()

    quote1 = Quotes()
    quote1.author=author1
    quote1.quote = "Salam!"
    quote1.tags = ["tags", "go"]
    quote1.save()



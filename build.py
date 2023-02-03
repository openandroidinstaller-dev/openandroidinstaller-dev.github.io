"""Main script to build the website from jinja templates."""
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader(searchpath="./templates/"),
    autoescape=select_autoescape()
)

if __name__ == "__main__":
    # pages to build
    pages = ["index.html"]

    # Load template files and write the rendered HTML
    for page in pages:
        # render the templates
        template = env.get_template(page)
        output = template.render()

        # replace the paths of the page
        if page == "index.html":
            output = output.replace("index.html", "https://openandroidinstaller.org")
        else:
            output = output.replace("index.html", "/")

        # write to file
        with open(f"{page}", "w") as html_output:
            html_output.write(output)

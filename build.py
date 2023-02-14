"""Main script to build the website from jinja templates."""
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader(searchpath="./templates/"),
    autoescape=select_autoescape()
)

if __name__ == "__main__":
    # pages to build
    pages = [
        "index.html",
        "supported-devices.html",
        "faq.html",
        "download.html",
        "imprint.html",
        "privacy.html",
    ]

    # Load template files and write the rendered HTML
    for page in pages:
        # render the templates
        template = env.get_template(page)
        output = template.render(
            version="v0.3.5-alpha",
            n_supported_devices=52,
        )

        # write to file
        with open(f"public/{page}", "w") as html_output:
            html_output.write(output)

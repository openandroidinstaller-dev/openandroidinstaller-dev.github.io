# Website for the OpenAndroidInstaller project

## Website build workflow

This website is made with Bulma and gets build to a static page via the Python tools `make`, `poetry` and `jinja2`.

To build the website follow the two following steps:

- Install the dependencies:

    ```
    make install
    ```

- Build the website:

    ```
    make website
    ```
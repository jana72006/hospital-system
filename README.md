# Nile Hospital

A polished, responsive hospital website built with Python and Flask as a student project. It brings the original desktop project's main ideas—doctor profiles, appointment requests, a pharmacy, skincare, and an about section—into a single web experience.

## Run locally

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies and start the app:

   ```powershell
   pip install -r requirements.txt
   python app.py
   ```

4. Open <http://127.0.0.1:5000>.

## Tests

Run the automated checks from the project directory:

```powershell
python -m unittest discover -s tests -v
```

## Demo behavior

- Appointment and pharmacy forms validate their selections and show a confirmation.
- Requests are examples only: no real appointment is booked, no order is placed, and no personal or patient information is collected or stored.
- The doctor directory, products, prices, and availability are illustrative project content—not medical advice or a live hospital service.
- The secret key is generated for local development. Set a private `SECRET_KEY` environment variable when deploying the app.

## Publishing

### PythonAnywhere (without Render)

1. Create a free [PythonAnywhere Beginner account](https://www.pythonanywhere.com/registration/register/beginner/).
2. Open a **Bash console** and download the public project:

   ```bash
   git clone https://github.com/jana72006/hospital-system.git
   mkvirtualenv --python=/usr/bin/python3.13 hospital-system-venv
   workon hospital-system-venv
   pip install -r ~/hospital-system/requirements.txt
   ```

3. In **Web**, select **Add a new web app**, then **Manual configuration** and the same Python version as your virtual environment. Your public website address will be shown on that page.
4. In the web app's **Virtualenv** section, enter `~/.virtualenvs/hospital-system-venv`.
5. Open the **WSGI configuration file** linked on the Web page. Replace its contents with the example from `pythonanywhere_wsgi.py`, changing `YOUR_PYTHONANYWHERE_USERNAME` to your username. Generate a private key in the Bash console with `python -c "import secrets; print(secrets.token_hex(32))"` and replace `REPLACE_WITH_A_RANDOM_SECRET` in the WSGI configuration. **Do not put the real key in GitHub or share it.**
6. Select **Reload** in the Web tab and visit the public website address shown there.

After later GitHub updates, run `cd ~/hospital-system && git pull` in the Bash console and select **Reload** again. PythonAnywhere free accounts limit the number of web apps and restrict outbound internet access; this project does not require server-side external network requests.

### Optional: Render

The repository also includes `render.yaml` for deployment to Render. The PythonAnywhere steps above do not require Render or GitHub Pages.

## Project structure

```text
app.py
templates/
  index.html
static/
  styles.css
requirements.txt
pythonanywhere_wsgi.py
render.yaml
tests/
  test_app.py
```

# Guideline

This provide some guide for coding.

## Flask and Python2.7

This app use flask framework.

```python
from flask import Flask
app = Flask(__name__)
```

The `flask` framework provide the glue for writing code. All `url` is handle by `app.route`.

```python
@app.route('/')
@app.route('/rumijawi')
def rumijawi():
 return render_template('rumijawi.html',latest_changes=latest_changes)
```

This mean all `url` at `/` or `/rumijawi` will use function `rumijawi()`. The function `rumijawi` will render `rumijawi.html`.

This is confusing.

The last line of a function will render an html page.

The sequences is

```plantuml
url -> app.route
app.route -> html :render
html -> app.route :post
app.route -> html :process
html -> user :display
```
So, there is;
* `app.route` : `/rumijawi`
* `template html` : `rumijawi.html`
* `function` : process input from rumijawi.html

`rumijawi.html` will have form for input. This input will be passed to another `route` such as `/translate`. This `/translate` url will have a mapping on the `app.route('/translate')`.

We have `/rumijawi` route.

```python
@app.route('/rumijawi')
def rumijawi():
 return render_template('rumijawi.html',latest_changes=latest_changes)
```

This will render `rumijawi.html`.

`rumijawi.html` will have form for user input.

```html
      <div class="col-sm-9">
        <h1>&nbsp;</h1>
        <h1>&nbsp;</h1>
        <form action="/transliterate" method="post">
          <input name="rumi" type="text" placeholder="tulis perkataan rumi di sini">
          <!-- <input type="submit" value="transliterate"></input> -->
          <button class="btn btn-primary" name="_submit" type="submit" value="transliterate">transliterate</button>
        </form>
      </div>
```

Here is the key. When the user submit, the framework will go to route `/translate`. And the route `/translate` is a function that will process the input and render the result.

```python
@app.route('/transliterate', methods = ['POST'])
def transliterate():
    rumi = request.form['rumi']

    rumi.lower().strip()

    if rumi in rjDict1:
     if rumi in rjDict2 and rumi in rjDict3:
      return render_template('transliterate.html', rumi = rumi,
          jawi = rjDict1[rumi], jawi2 = rjDict2[rumi], jawi3 = rjDict3[rumi],
          latest_changes=latest_changes)
     elif rumi in rjDict2:
      return render_template('transliterate.html', rumi = rumi, jawi = rjDict1[rumi],
          jawi2 = rjDict2[rumi], latest_changes=latest_changes)
     else:
      return render_template('transliterate.html', rumi = rumi,
          jawi = rjDict1[rumi],latest_changes=latest_changes)
    else:
     guest1 = edits1(rumi)
     guest2 = []
     for c in guest1:
      if c in rjDict1:
       guest2.append(c)
     return render_template('not_found_transliterasi.html', rumi = rumi,
        guesses = guest2,latest_changes=latest_changes)
    # return pass
# set the secret key.  keep this really secret:
```

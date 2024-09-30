## K13: Template for Success
### Due: 2024-10-02w EOB


Your Trio Mission:

_Step 0: Come together. "Form like Voltron." Learn each others' names. Introduce Duckies..._

1. Peruse your last few work submissions with an eye toward...
   * assessing each others' coding styles, workflow preferences
   * taking only the best (cleanest, most expressive, most robust) code forward
   * deepening your understanding of anything covered thus far

1. Write a Flask app with an `/wdywtbwygp` route, which will use a template to generate an HTML page with
   * an appropriate title,
   * a descriptive heading,
   * TNPG+roster,
   * and a tablified version of the occupations data, along with
   * a randomly selected occupation shown at the top (each page refresh should yield a newly-chosen occupation).
1. Read the "egoless programming" excerpt. Discuss with teammates. (Outside class.)
1. *Grow your codebase* to incorporate this functionality:
   * For each occupation, find a link that would be helpful to get started in that field.
   * Add that link to the `occupations.csv` file.
   * Include the link in your python dictionary (_Note: you'll have to store the percentage and the link as values attached to each name._)
   * Configure your app to publish each link alongside its occupation. (You know, to help your users on their way to their new job.)
1. Stretch/flex goal if you want it... wave team flag to signal readiness :)

Guidelines:
  - Store your occupations data as a python dictionary.
  - Note anything notable in `notes.txt` in app's root directory. Include section labelled `EGO` for any responses you would like to *share*...
  - _PLAN FIRST_ so as to maximize your valuable time. Re-use code where possible. (Do not carry forward garbage...)
  - _Reminder:_ include heading as comment in your html and python files.

<br>

DELIVERABLES:
* In your heading, replace your name with your TNPG and roster.
* Save to workshop under __`13_tempwork`__. Structure:

```
path/to/myworkshop/13_tempwork$ tree
.
├── app.py
├── data
│   └── occupations.csv
├── notes.txt
└── templates
    └── tablified.html
```


<br>

[jinja2 docs](https://jinja.palletsprojects.com/en/3.1.x/templates/)

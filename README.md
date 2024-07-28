![Project status](https://img.shields.io/badge/version-0.1-green)
![Python version](https://img.shields.io/badge/requires-python_3.7-blue)

# :notebook: **OnePager** :notebook:

Welcome to the official repository for the **OnePager** library. **OnePager** is still under development and is therefore likely to undergo some minor changes over the next few months.

To install **OnePager** simply create a *virtual environment* (optional) and run `pip install onepager`.

## Table of Contents :bookmark_tabs:

- [What is OnePager?](#what-is-onepager-bulb)
- [Why use OnePager?](#why-use-onepager-heart)
- [Why Pico.css?](#why-picocss-two-hearts)
- [Create your first OnePager document](#create-your-first-onepager-document-pencil)
- [Offline version](#offline-version-open_file_folder)
- [Roadmap](#roadmap-date)
- [License](#contributing-to-pandas)

## What is OnePager? :bulb:

**OnePager** allows you to generate simple and easy-to-navigate documentation for all your projects.

All you have to do is create a document and start writing some custom *markdown* syntax. Run `onepager name_of_your_document.md` and **OnePager** will automatically convert this document into a beautiful *html* page.

Special thanks to my workmate **Evan** who gave me the idea of starting this project.

## Why use **OnePager**? :heart:

* Easy to deploy and use daily
* Mobile-friendly documents
* Cleaner and more visually appealing than traditional Word documents
* Easy bookmarking in browsers for centralized documentation
* Familiar Markdown syntax
* Colleagues can access documentation without editing capabilities (edits require modifying the corresponding Markdown file and running the Python script)

## Why Pico.css? :two_hearts:

[**Pico.css**](https://picocss.com/) is a fantastic CSS framework balancing ease of use with creative freedom. While less feature-rich than frameworks like [**Bulma**](https://bulma.io/), **Pico** offers a wide range of options with a lightweight footprint.

Like other *minimal CSS frameworks*, Pico handles many background styling tasks, freeing you to focus on content.

## Create your first OnePager document :pencil:

For **OnePager** to work, follow these simple steps:

1. **First line of your markdown file:** This line <ins>should always adhere to the following structure</ins>:

`[title],[owner 1],[owner 2 (optional)],[owner 3 (optional)],etc..`

Example:

```markdown
This is a document,Julien,Fiona
```

2.  **Collapsible sections**: Each section starts with `BEGIN,[section title]` and ends with `END`.

Example:

```markdown
BEGIN,This is a section about pizzas

Pizzas are **awesome**

END
```

Next simply paste the following code into a file named `test.md`:

```markdown
This is a document,Julien,Fiona

Hi, I like junk food!

BEGIN,Pizza

Pizzas are **awesome**

END
```

Now run the following command:

```
onepager test.md
```

This should create an *html* file named *test.html* that looks like this:

![example](example.gif)

## Offline version :open_file_folder:

:warning: Currently, an internet connection is required for documents created with **OnePager** to render properly. :warning:

**Coming soon!** Support for offline documents is in development.

## Roadmap :date:

* Offline mode support :construction_worker:
* Support for additional *minimal CSS frameworks* such as [**Milligram**](https://milligram.io/)  :construction_worker:

## License :cop:

[MIT](https://opensource.org/license/mit)

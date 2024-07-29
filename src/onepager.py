import mistune
import sys 
import os
from datetime import datetime
from typing import List, Set, Dict, Tuple

class OnePager: 

    def __init__(self):
        self.file_name: str = sys.argv[1]
        self.css: str = "https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
        self.last_updated: str = datetime.now().strftime("%Y-%m-%d")
        self.first_line: str = ""
        self.title: str = ""
        self.html_boilerplate: str = """
            <!DOCTYPE html>
            <html lang="en" data-theme="dark">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>{{document_title}}</title>
                <link rel="stylesheet" href={{css_framework}}>
            </head>
            <body>
                <main class="container">
                    {{markdown_file}}
                </main>
            </body>
            </html>
        """
    
    def fetchMarkdown(self) -> str:
        with open(self.file_name, "r") as file:
            fetched_md: str = file.readlines()
        self.first_line = fetched_md[0]
        return fetched_md

    def getHeader(self) -> str:
        first_line_as_list: List[str] = self.first_line.split(",")
        self.title: str = first_line_as_list[0]

        parsed_header: str = ""
        parsed_header += f'<div class="header"><h1>{first_line_as_list[0]}</h1></div>'
        if len(first_line_as_list) > 2:
            parsed_header += "<p>Owners:</p>"
        else:
            parsed_header += "<p>Owner:</p>"
        parsed_header += "<ul>" 
        for line in first_line_as_list[1:]:
            parsed_header += f'<li>{line}</li>'
        parsed_header += "</ul>"
        parsed_header += f"<p>Last updated: <kbd>{self.last_updated}</kbd></p>" 
        parsed_header += "<br>"
        return parsed_header

    def getBody(self,fetched_md) -> str:
        parsed_body: str = ""
        for line in fetched_md[1:]:
            if line.startswith("BEGIN"):
                section_title: str = line.split(",")[1]
                new_section: str = f'<details><summary role="button">{section_title}</summary>'
                parsed_body += new_section
            elif line.startswith("END"):
                parsed_body += "</details>"
            else:
                parsed_body += f"\n {line} "
        return parsed_body 

    def convertToHTML(self) -> str:
        md_as_list: str = self.fetchMarkdown()
        document_header: str = self.getHeader()
        document_body: str = self.getBody(md_as_list)
        full_document: str = document_header + document_body
        md_to_html: str = mistune.html(
            full_document
        )
        html_final: str = (
            self.html_boilerplate
            .replace(
                "{{document_title}}",
                self.title
            )
            .replace(
                "{{markdown_file}}",
                md_to_html
            )
            .replace(
                "{{css_framework}}",
                self.css
            )
            .replace(
                "<code>",
                "<pre><code>"
            )
            .replace(
                "</code>",
                "</pre></code>"
            )
            .replace(
                "??!",
                "<kbd>"
            )
            .replace(
                "!??",
                "</kbd>"
            )
        )
        return html_final
    
    def saveFile(self):
        html_final: str = self.convertToHTML()
        html_file_name: str = f"{self.file_name.split('.')[-2]}.html"
        with open(html_file_name,"w") as file:
            file.write(html_final)

def runOnePager():
    op = OnePager()
    try:
        op.saveFile()
    except Exception as e:
        print(e)

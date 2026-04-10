# https://www.codewars.com/kata/54eecc187f9142cc4600119e/train/python

class HTMLGen:
    def a(self, content: str) -> str:
        return f"<a>{content}</a>"

    def b(self, content: str) -> str:
        return f"<b>{content}</b>"

    def p(self, content: str) -> str:
        return f"<p>{content}</p>"

    def body(self, content: str) -> str:
        return f"<body>{content}</body>"

    def div(self, content: str) -> str:
        return f"<div>{content}</div>"

    def span(self, content: str) -> str:
        return f"<span>{content}</span>"

    def title(self, content: str) -> str:

        return f"<title>{content}</title>"

    def comment(self, content: str) -> str:
        return f"<!--{content}-->"

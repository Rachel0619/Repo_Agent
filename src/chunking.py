import re
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def sliding_window(seq, size, step):
    if size <= 0 or step <= 0:
        raise ValueError("size or step can't be smaller than 0")
    result = []
    n = len(seq)
    for i in range(0, n, step):
        chunk = seq[i:i+size]
        result.append({"start": i, "chunk": chunk})
        if i+size >= n:
            break
    return result

def split_markdown_by_level(text, level=2):
    """
    Split markdown text by a specific header level.
    
    :param text: Markdown text as a string
    :param level: Header level to split on
    :return: List of sections as strings
    """
    # This regex matches markdown headers
    # For level 2, it matches lines starting with "## "
    header_pattern = r'^(#{' + str(level) + r'} )(.+)$'
    pattern = re.compile(header_pattern, re.MULTILINE)

    # Split and keep the headers
    parts = pattern.split(text)
    
    sections = []
    for i in range(1, len(parts), 3):
        # We step by 3 because regex.split() with
        # capturing groups returns:
        # [before_match, group1, group2, after_match, ...]
        # here group1 is "## ", group2 is the header text
        header = parts[i] + parts[i+1]  # "## " + "Title"
        header = header.strip()

        # Get the content after this header
        content = ""
        if i+2 < len(parts):
            content = parts[i+2].strip()

        if content:
            section = f'{header}\n\n{content}'
        else:
            section = header
        sections.append(section)
    
    return sections

def llm(prompt, model='gpt-4o-mini'):
    openai_client = OpenAI()
    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai_client.responses.create(
        model=model,
        input=messages
    )

    return response.output_text

def intelligent_chunking(text):
    prompt_template = """
        Split the provided document into logical sections
        that make sense for a Q&A system.

        Each section should be self-contained and cover
        a specific topic or concept.

        <DOCUMENT>
        {document}
        </DOCUMENT>

        Use this format:

        ## Section Name

        Section content with all relevant details

        ---

        ## Another Section Name

        Another section content

        ---
    """.strip()
    prompt = prompt_template.format(document=text)
    response = llm(prompt)
    sections = response.split('---')
    sections = [s.strip() for s in sections if s.strip()]
    return sections
from tkinter import ttk, RAISED

from src.connection.handle_wiki import get_topics_by_chapter_id


class WikiChapter(ttk.Frame):
    def __init__(self, container, chapter, show_home):
        super().__init__(container)

        self.parent = container

        print(chapter)

        chapter_id = chapter['id']
        self.topics = get_topics_by_chapter_id(chapter_id)

        print(self.topics)

        self.create_widgets(chapter, self.topics)

    def create_widgets(self, chapter, topics):
        chapter_name = chapter['name']

        title = ttk.Label(
            self,
            text=chapter_name
        )
        title.grid(column=0, sticky="EW")

        title_separator = ttk.Separator(
            self
        )
        title_separator.grid(column=0, columnspan=1, sticky="EW")

        for topic in topics:
            topic_name = topic['name']
            topic_description = topic['description']

            name = ttk.Label(
                self,
                relief=RAISED,
                text=topic_name
            )
            name.grid(column=0, sticky="EW")

            description = ttk.Label(
                self,
                text=topic_description
            )
            description.grid(column=0, sticky="EW")

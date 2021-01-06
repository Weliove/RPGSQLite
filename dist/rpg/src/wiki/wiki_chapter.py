from tkinter import ttk, RAISED, font

from src.wiki.wiki import Wiki


class WikiChapter(ttk.Frame):
    def __init__(self, container, chapter, wiki: Wiki):
        super().__init__(container)

        self.parent = container
        self.chapter = chapter
        self.wiki = wiki

        wiki.last_chapter = chapter

        print(chapter)

        chapter_id = chapter['id']
        self.topics = self.wiki.get_topics(chapter_id)

        print(self.topics)

        self.create_widgets(chapter, self.topics)

        self.create_buttons()

    def create_widgets(self, chapter, topics):
        chapter_name = chapter['name']
        chapter_description = chapter['description']

        topic_description_list = []

        title = ttk.Label(
            self,
            text=chapter_name
        )
        title.grid(column=0, sticky="EW")

        title_separator = ttk.Separator(
            self
        )
        title_separator.grid(column=0, columnspan=1, sticky="EW")

        if len(chapter_description) > 0:
            description = ttk.Label(
                self,
                text=chapter_description,
                font=font.Font(size=11)
            )
            description.grid(column=0, sticky='EW')

        for topic in topics:
            topic_name = topic['name']
            topic_description = topic['description']

            name = ttk.Label(
                self,
                relief=RAISED,
                text=topic_name
            )
            name.grid(column=0, sticky="EW")

            t_description = ttk.Label(
                self,
                text=topic_description
            )
            t_description.grid(column=0, sticky="EW")

            topic_description_list.append(t_description)

        def reconfigure_labels(event):
            title.configure(wraplength=self.winfo_width() - 25)

            if len(chapter_description) > 0:
                description.configure(wraplength=self.winfo_width() - 25)

            for local_topic_description in topic_description_list:
                local_topic_description.configure(wraplength=self.winfo_width() - 25)

        self.bind("<Configure>", reconfigure_labels)

    def create_buttons(self):
        wiki_separator = ttk.Separator(
            self
        )
        wiki_separator.grid(column=0, columnspan=1, sticky="EW")

        chapter_button = ttk.Button(
            self,
            text='Add Topic',
            command=lambda: self.parent.create_frame('create_topic', self.chapter),
            cursor='hand2'
        )
        chapter_button.grid(column=0, sticky="EW")

        back_button = ttk.Button(
            self,
            text='← Back',
            command=lambda: self.parent.create_frame('section', self.wiki.last_section),
            cursor='hand2'
        )
        back_button.grid(column=0, sticky='EW')

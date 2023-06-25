import sqlite3
class database:
    def __init__(self):
        self.connection = sqlite3.connect('DataBase/database.db')
        self.cur = self.connection.cursor()
    async def get_link_id(self, link):
        return self.cur.execute('SELECT id FROM links WHERE link == ?', (link,)).fetchone()
    async def add_link(self, link):
        self.cur.execute('INSERT INTO links (link) VALUES (?)', (link,))
        self.connection.commit()
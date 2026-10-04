import sqlite3
import heuristics
conn = sqlite3.connect('aruuz.db')
c = conn.cursor()
def get_code(taqti_str):
    chunks = [x.strip() for x in taqti_str.split('+')]
    code = ''
    from araab import Araab
    for chunk in chunks:
        stripped = Araab.remove_araab(chunk.replace('\u06BE', '').replace('\u06BA', ''))
        n = len(stripped)
        if n == 1: code += heuristics.length_one_scan(chunk)
        elif n == 2: code += heuristics.length_two_scan(chunk)
        elif n == 3: code += heuristics.length_three_scan(chunk)
        elif n == 4: code += heuristics.length_four_scan(chunk)
        elif n == 5: code += heuristics.length_five_scan(chunk)
        else: code += '=' * (n // 2) + ('-' if n % 2 else '')
    return code

c.execute("SELECT Taqti FROM mastertable WHERE Word='زندگانی'")
print('زندگانی:', get_code(c.fetchone()[0]))
c.execute("SELECT Taqti FROM mastertable WHERE Word='آئس فیکٹری'")
print('آئس فیکٹری:', get_code(c.fetchone()[0]))

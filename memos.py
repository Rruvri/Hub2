from datetimetracking import *

class MasterMemos:
    def __init__(self):
        self.collections = []

    def create_memos_collection(self):
        name = input("Enter title for memo list: ")
        self.collections.append(MemosCol(name))

class MemosCol:
    def __init__(self, name, memos_list=[]):
         self.name = name
         self.memos_list = memos_list
    
    def create_memo(self):
        content = input("Enter memo content: ")
        notes = input("Enter further notes if required, [return] to continue: ")
        if notes == '':
            notes == None
        due_date = input("Enter due date if needed, format dd/mm/yy")
        if due_date == '':
            due_date = None
        due_date = datestr_to_dt(due_date)
        self.memos_list.append(Memo(content, notes, due_date))

    def view_memos_col(self):
        if self.memos_list:
            for memo in self.memos_list:
                print(f'|{memo.content}|')
                if memo.due_date:
                    print(memo.due_date)
                if memo.notes:
                    print(f'\n{memo.notes}')

    


class Memo:
    def __init__(self, content, notes=None, due_date=None):
        self.content = content
        self.notes = notes
        self.due_date = due_date

    

def get_memo_from_readme():
    with open('README.txt', 'rb') as f:
        readlines = f.readlines()
        titles = []
        for line in readlines:
            titles.append(line)
        print(titles)
        
            


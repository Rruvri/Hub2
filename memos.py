from datetimetracking import *
from sysfuncs import clear_console, menu_hold

class MasterMemos:
    def __init__(self):
        self.collections = {}

    def create_memos_collection(self):
        name = input("Enter title for memo list: ")
        self.collections[name] = MemosCol(name)

    
    @menu_hold
    def view_collections(self):
        

        '''
        if specified == None:
            #specified = input('Enter memos collection name, or [return] to view all: ')
            if not self.collections:
                print('No memos yet!')
                return
            index = 0
            for memcol in self.collections:
                index +=1
                print(f'[{index}] {memcol}')
            choice = input('Enter collection number to access: ')
            choice_list = self.collections.keys()
            clear_console()
            self.collections[choice_list[int(choice)-1]].interact()
        '''
        #else:
            #if specified == 'all':
        print('\n== Memos ==')
        if self.collections:
            for col in self.collections:
                self.collections[col].view_memos_col()
            print('\n')
                    #add hold fn

            #if specified == '':
             #   specified = 'all'
            #if specified != '' and specified != 'all':
            #else:
             #   specified = specified.title()
              #  return self.collections[specified].view_memos_col()
        '''
        #elif specified == 'all':
        print('\n== Memos ==')
        if self.collections:
            for col in self.collections.keys():
                self.collections[col].view_memos_col()
                #add hold fn
        '''
    '''
    def view_all(self):
        for col in self.collections:
            print(col)
    '''

    def interact_choice(self):
        if not self.collections:
            print('No memos yet!')
            return
        index = 0
        for memcol in self.collections:
            index +=1
            print(f'[{index}] {memcol}')
        choice = int(input('Enter collection number to access: '))
        
        choice_list = list(self.collections.keys())
        
        clear_console()
        self.collections[choice_list[choice-1]].interact()
        
        #choice = (input("Enter memos collection name: ")).title()
        #return self.collections[choice].interact()
        
        
    
    def reset(self):
        self = self.__init__() 


class MemosCol:
    def __init__(self, name, memos_list=[]):
         self.name = name
         self.memos_list = memos_list
    
    def create_memo(self):
        content = input("Enter memo content: ")
        #add a short form function, for i.e. grocery lists
        notes = input("Enter further notes if required, [return] to continue: ")
        if notes == '':
            notes == None
        due_date = input("Enter due date if needed, format dd/mm/yy")
        if due_date == '':
            due_date = None
        else:
            due_date = datestr_to_dt(due_date)
        self.memos_list.append(Memo(content, notes, due_date))

    def view_memos_col(self):
        print(f'\n[{self.name}]')
        if self.memos_list:
            index = 1
            for memo in self.memos_list:
                main_body = f'{index}] {memo.content}'
                if memo.due_date:
                    print(main_body + f' | {memo.due_date}')
                else:
                    print(main_body)

                if memo.notes:
                    print(f'    -> {memo.notes}')
                index += 1
                #print('\n')
        else:
            print(' -> Empty!')
    
    def interact(self):
        menu_check = True
        while menu_check:
            self.view_memos_col()
            print("\nOptions:")
            menu = input('[c]reate a memo, [e]dit/delete a memo, or [return] to exit')
            if menu == '':
                menu_check = False
            elif menu == 'c':
                self.create_memo()
            elif menu == 'e':
                select_choice = input('Enter memos number: ')
                edit_delete = input("Enter new content, or [return] to delete: ")
                if edit_delete == '':
                    self.memos_list.pop(int(select_choice)-1)                    
                else:
                    self.memos_list[int(select_choice)-1].content = edit_delete
            clear_console()


    


    


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
        
            


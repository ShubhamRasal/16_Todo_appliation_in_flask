import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('functions\\todo.db')
        self.create_user_table()
        self.create_to_do_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_to_do_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
          "id" INTEGER PRIMARY KEY,
          "Title" TEXT,
          "Description" TEXT,
          "_is_deleted" boolean DEFAULT 0,
          "CreatedOn" Date DEFAULT CURRENT_DATE,
          "DueDate" Date
        );

        """

        self.conn.execute(query)
#Schema Ends


class ToDoModel:
   

    def __init__(self):
        self.conn = sqlite3.connect('functions\\todo.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def list_items(self, where_clause=""):
        query='''select * from Todo where _is_deleted != 1'''+where_clause
        #print (query)
        cur = self.conn.cursor()
        cur.execute(query)
        result_set = cur.fetchall()
        return result_set

    def sql_edit_insert(self,var):
        #print(var)
        query='''insert into Todo(Title,Description,DueDate) values (?,?,?)'''
        cur = self.conn.cursor()
        cur.execute(query,var)
        self.conn.commit()
        
    def sql_delete(self,ID):
        print("Inside sql_delete",ID)
        print("Type",type(ID))
        query='''UPDATE Todo SET _is_deleted=1 where id=?'''
        print("Query",query)
        cur = self.conn.cursor()
        cur.execute(query,ID)
        self.conn.commit()  

    def sql_edit(self,var):
        query='''UPDATE Todo SET Title=?,Description =?,DueDate= ? where id=?'''
        cur = self.conn.cursor()
        cur.execute(query,var)
        self.conn.commit()      
    

#end TodoModel

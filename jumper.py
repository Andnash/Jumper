
class Jumper:


    def show_jumper(self):
        mistake_lvl = self.mistake_lvl
        cur_show = ''

        if mistake_lvl == 0:

            cur_show = ("""  
                  _____
                ./_____\.
                 \ | | /
                  \| |/
                   |0|
                   V|V
                   / \ """)
            


        elif mistake_lvl == 1:
            cur_show = ("""
                | _____
                |/_____\.
                   | | /
                   | |/
                  <|0|
                    |V
                   / \ """)
            

        
        elif mistake_lvl == 2:
            cur_show = ("""
                | _____ |
                |/_____\|
                   | |
                   | |
                  <|0|>
                    |
                   / \ """)
            


        elif mistake_lvl == 3:
            cur_show = ("""
                | __|__ |
                |/__|__\|
                     |
                     |
                  \ O|>  ----< Help! Help! >
                    | 
                   / \ """)
            
            


        elif mistake_lvl == 4:
            cur_show = ("""
                | ^|^|^ |
                |/_| |_\|
                
                
                
                  \ O /  ----< AAAAAAAAAHHHHH!!!!! >
                    |
                   / \ """)

        print(cur_show)
            
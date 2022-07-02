## al ingresar los usuarios se debe almacenar la informacion 4.3

import menu as mn
import usuario_nuevo as us
import list_user as ls
def main():
    while True:
       res=mn.menu()
       if res ==1:
         us.user_new(res)
       else:
         ls.list_user(res)
main()
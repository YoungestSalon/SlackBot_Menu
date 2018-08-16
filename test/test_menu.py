from menu import Menu_choice

def lunch_is_Korean_food():
    m = Menu_choice()
    assert "한식" == m.run("점심")
    

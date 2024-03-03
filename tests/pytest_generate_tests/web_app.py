class WebApp:
    def __init__(self, user_role):
        self.user_role = user_role

    def can_edit_content(self):
        return self.user_role in ('admin', 'editor')

    def can_view_content(self):
        return True
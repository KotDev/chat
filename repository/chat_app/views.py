from flask.views import View
from flask import render_template

class BaseView(View):

    def dispatch_request(self):
        pass

class TemplateView(View):

    def dispatch_request(self):
        pass


class ShowRoom(BaseView, TemplateView):

    def dispatch_request(self):

        super(ShowRoom, self).dispatch_request()

        return render_template('room.html', room='room1')

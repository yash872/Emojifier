from django.shortcuts import render
from django.views.generic import TemplateView, View
from services.emojifier import api
from keras import backend as K


class Index(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        content = request.POST['content']
        try:
            emoji = api.predict(content)
        except:
            return render(request, self.template_name)

        context = {
            "content" : content,
            "emoji" : emoji
        }
        return render(request, self.template_name, context)


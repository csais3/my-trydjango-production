from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'Title: "({title})" is already in use. Please pick another title.')

#class ArticleForm(forms.Form):
    # title = forms.CharField(max_length=50)
    # content = forms.CharField()

    # # def clean_title(self):
    # #     cleaned_data = self.cleaned_data
    # #     print(cleaned_data)
    # #     title = cleaned_data.get('title')
    # #     print(title)
    # #     return title

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     print('cleaned data: ',cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'the office':
    #         self.add_error('title', 'This title is taken')
    #     return cleaned_data
    
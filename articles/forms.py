from django import forms
from .models import Article



class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Article.objects.filter(title__icontains = title)
        if qs.exists():
            self.add_error('title', 'this title already exists')

        content = cleaned_data.get('content')
        return cleaned_data



class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')

        if title == "office":
            self.add_error('title', 'the title cannot be done')
        
        return cleaned_data

        

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title= cleaned_data.get('title')

    #     if title=="office":
    #         raise forms.ValidationError('this is the clean_title version')
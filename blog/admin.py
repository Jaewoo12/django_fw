from django.contrib import admin
from .models import Post,Comment

# admin page 출력되는 내용을 customize
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','count_text']
    list_display_links = ['title']

    def count_text(self, post):
        return '{}글자'.format(len(post.text))
    count_text.short_description = '글내용 글자수'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
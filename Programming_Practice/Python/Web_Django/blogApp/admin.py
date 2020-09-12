from django.contrib import admin
from blogApp.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date', )  # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 설정
    search_fields = ('title', 'content') # 검색박스를 표시하고 입력된 단어는 해당 컬럼에서 검색하도록 지정
    prepopulated_fields = {'slug' : ('title', )} # title 필드를 통해 미리 채워지도록 지정


admin.site.register(Post, PostAdmin)

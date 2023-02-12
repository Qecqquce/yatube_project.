from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = ('group',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
class GroupAdmin(admin.ModelAdmin):
    ...


admin.site.register(Post, PostAdmin)
admin.site.register(Group,GroupAdmin)
